import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons

class MundellFlemingSim:
    def __init__(self):
        # Initial Parameters
        self.Y = np.linspace(0, 200, 200)
        self.lm_slope = 0.5
        self.bp_slope = 0.0  # Starts at Perfect Mobility
        
        # Base Intercepts (Pre-shock)
        self.is_intercept_base = 100
        self.lm_intercept_base = -20
        self.bp_intercept_base = 30
        
        # Shocks (Controlled by Sliders)
        self.g_shock = 0
        self.m_shock = 0
        
        # Settings
        self.mobility = 'Perfect' # Perfect, High, Low
        self.regime = 'Floating'  # Fixed, Floating

        # Setup Plot
        self.fig, self.ax = plt.subplots(figsize=(10, 7))
        plt.subplots_adjust(left=0.1, bottom=0.35)
        self.setup_widgets()
        self.update(None)

    def solve_intersection(self, m1, c1, m2, c2):
        # Solve for Y where m1*Y + c1 = m2*Y + c2
        if m1 == m2: return None # Parallel
        Y_sol = (c2 - c1) / (m1 - m2)
        r_sol = m1 * Y_sol + c1
        return Y_sol, r_sol

    def update(self, val):
        self.ax.clear()
        self.ax.set_xlim(0, 200)
        self.ax.set_ylim(0, 100)
        self.ax.grid(True, alpha=0.3)
        self.ax.set_title(f"Mundell-Fleming: {self.regime} Rate, {self.mobility} Mobility")
        self.ax.set_xlabel("Income (Y)")
        self.ax.set_ylabel("Interest Rate (r)")

        # 1. Update Parameters based on Widgets
        self.g_shock = self.s_fiscal.val
        self.m_shock = self.s_money.val
        
        # Mobility Logic
        if self.mobility == 'Perfect':
            self.bp_slope = 0
        elif self.mobility == 'Imperfect (High)':
            self.bp_slope = 0.2  # Flatter than LM (0.5)
        elif self.mobility == 'Imperfect (Low)':
            self.bp_slope = 0.8  # Steeper than LM (0.5)

        # 2. Define Curves (Short Run)
        # IS: r = -0.5Y + (Base + G_Shock)
        is_slope = -0.5
        is_int_sr = self.is_intercept_base + self.g_shock
        
        # LM: r = 0.5Y + (Base + M_Shock)
        lm_int_sr = self.lm_intercept_base - self.m_shock # Money supply increase lowers intercept

        # BP: r = slope*Y + Base
        # Note: BP intercept usually doesn't shift with G or M directly in simple models
        bp_int = self.bp_intercept_base

        # 3. Solve Short Run Equilibrium (IS = LM)
        Y_sr, r_sr = self.solve_intersection(is_slope, is_int_sr, self.lm_slope, lm_int_sr)
        
        # 4. Calculate BP at Short Run Y
        r_bp_at_sr = self.bp_slope * Y_sr + bp_int
        
        # Determine Surplus or Deficit
        bp_gap = r_sr - r_bp_at_sr
        status = "Balance"
        if bp_gap > 0.5: status = "Surplus"
        elif bp_gap < -0.5: status = "Deficit"

        # 5. Calculate Final Equilibrium (The Adjustment)
        Y_final, r_final = Y_sr, r_sr
        is_int_final = is_int_sr
        lm_int_final = lm_int_sr
        
        if self.regime == 'Fixed':
            # CB defends peg. 
            # If Surplus -> Buy FX, Sell Dom -> M increases -> LM Shifts Right
            # If Deficit -> Sell FX, Buy Dom -> M decreases -> LM Shifts Left
            # Target: IS (Shocked) intersects BP.
            Y_final, r_final = self.solve_intersection(is_slope, is_int_sr, self.bp_slope, bp_int)
            # Recalculate LM to pass through this point: r = 0.5Y + C => C = r - 0.5Y
            lm_int_final = r_final - self.lm_slope * Y_final
            
        elif self.regime == 'Floating':
            # Market adjusts Exchange Rate.
            # If Surplus -> Appreciation -> NX falls -> IS Shifts Left
            # If Deficit -> Depreciation -> NX rises -> IS Shifts Right
            # Target: LM (Shocked) intersects BP.
            Y_final, r_final = self.solve_intersection(self.lm_slope, lm_int_sr, self.bp_slope, bp_int)
            # Recalculate IS to pass through this point: r = -0.5Y + C => C = r + 0.5Y
            is_int_final = r_final - is_slope * Y_final

        # 6. Plotting
        # Plot Lines
        self.ax.plot(self.Y, is_slope*self.Y + is_int_sr, label='IS (Short Run)', color='blue', linestyle='--')
        self.ax.plot(self.Y, self.lm_slope*self.Y + lm_int_sr, label='LM (Short Run)', color='red', linestyle='--')
        self.ax.plot(self.Y, self.bp_slope*self.Y + bp_int, label='BP', color='green', linewidth=2)
        
        # Plot Final Curves (Ghost lines)
        if self.regime == 'Fixed':
            self.ax.plot(self.Y, self.lm_slope*self.Y + lm_int_final, label='LM (Final)', color='red', alpha=0.3)
        else:
            self.ax.plot(self.Y, is_slope*self.Y + is_int_final, label='IS (Final)', color='blue', alpha=0.3)

        # Plot Points
        self.ax.scatter([Y_sr], [r_sr], color='orange', s=100, zorder=5, label=f'Short Run ({status})')
        self.ax.scatter([Y_final], [r_final], color='black', s=100, zorder=5, label='Final Eq')
        
        # Arrows
        self.ax.annotate('', xy=(Y_final, r_final), xytext=(Y_sr, r_sr),
                         arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))

        self.ax.legend(loc='upper left')
        self.fig.canvas.draw_idle()

    def setup_widgets(self):
        # Sliders
        ax_fiscal = plt.axes([0.15, 0.2, 0.65, 0.03])
        ax_money = plt.axes([0.15, 0.15, 0.65, 0.03])
        
        self.s_fiscal = Slider(ax_fiscal, 'Fiscal (G)', -40, 40, valinit=0)
        self.s_money = Slider(ax_money, 'Money (M)', -40, 40, valinit=0)
        
        self.s_fiscal.on_changed(self.update)
        self.s_money.on_changed(self.update)
        
        # Radio Buttons
        ax_radio_mob = plt.axes([0.02, 0.4, 0.12, 0.15])
        self.radio_mob = RadioButtons(ax_radio_mob, ('Perfect', 'Imperfect (High)', 'Imperfect (Low)'))
        self.radio_mob.on_clicked(self.set_mobility)
        
        ax_radio_reg = plt.axes([0.02, 0.6, 0.12, 0.15])
        self.radio_reg = RadioButtons(ax_radio_reg, ('Floating', 'Fixed'))
        self.radio_reg.on_clicked(self.set_regime)

    def set_mobility(self, label):
        self.mobility = label
        self.update(None)

    def set_regime(self, label):
        self.regime = label
        self.update(None)

if __name__ == '__main__':
    sim = MundellFlemingSim()
    plt.show()