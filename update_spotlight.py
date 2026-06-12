import re

files_to_update = ['index.html', 'site_build/index.html']

new_spotlight = """        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 items-start" id="spotlight-grid">
            
            <!-- Card 1: Economists' Theories -->
            <div class="bg-white rounded-xl shadow-md border-t-4 border-indigo-600 overflow-hidden flex flex-col transition-all">
                <div class="p-5">
                    <h3 class="text-lg font-bold text-slate-900 mb-2">Economists' Theories</h3>
                    <p class="text-sm text-slate-600 mb-4">Glimpse: Chronological mapping of major economists.</p>
                    <button onclick="toggleCard(this)" class="text-indigo-600 font-medium text-sm hover:underline">Show Glimpse ▾</button>
                </div>
                <div class="hidden flex-col p-5 border-t border-slate-100 bg-slate-50">
                    <img src="Special/Many Economists' Theories.png" alt="Many Economists' Theories" class="w-full rounded mb-4 shadow-sm">
                    <a href="history-and-tools.html" class="block w-full text-center py-2 bg-indigo-600 text-white hover:bg-indigo-700 rounded-lg font-medium transition-colors text-sm">
                        Explore More in History
                    </a>
                </div>
            </div>

            <!-- Card 2: Five Year Plans -->
            <div class="bg-white rounded-xl shadow-md border-t-4 border-indigo-600 overflow-hidden flex flex-col transition-all">
                <div class="p-5">
                    <h3 class="text-lg font-bold text-slate-900 mb-2">India's Five Year Plans</h3>
                    <p class="text-sm text-slate-600 mb-4">Glimpse: Infographic of all the five-year plans of India and what each entailed.</p>
                    <button onclick="toggleCard(this)" class="text-indigo-600 font-medium text-sm hover:underline">Show Glimpse ▾</button>
                </div>
                <div class="hidden flex-col p-5 border-t border-slate-100 bg-slate-50">
                    <img src="Econ-entrance-more-resources/Econ images/notebook all econ plans.png" alt="Five Year Plans" class="w-full rounded mb-4 shadow-sm">
                    <a href="history-and-tools.html" class="block w-full text-center py-2 bg-indigo-600 text-white hover:bg-indigo-700 rounded-lg font-medium transition-colors text-sm">
                        Explore More in History
                    </a>
                </div>
            </div>

            <!-- Card 3: International Trade Theory -->
            <div class="bg-white rounded-xl shadow-md border-t-4 border-indigo-600 overflow-hidden flex flex-col transition-all">
                <div class="p-5">
                    <h3 class="text-lg font-bold text-slate-900 mb-2">International Trade</h3>
                    <p class="text-sm text-slate-600 mb-4">Glimpse: Key international trade theories.</p>
                    <button onclick="toggleCard(this)" class="text-indigo-600 font-medium text-sm hover:underline">Show Glimpse ▾</button>
                </div>
                <div class="hidden flex-col p-5 border-t border-slate-100 bg-slate-50">
                    <img src="Special/International Trade.png" alt="International Trade" class="w-full rounded mb-4 shadow-sm">
                    <a href="macroeconomics.html" class="block w-full text-center py-2 bg-indigo-600 text-white hover:bg-indigo-700 rounded-lg font-medium transition-colors text-sm">
                        Explore More in Macroeconomics
                    </a>
                </div>
            </div>

            <!-- Card 4: Optimization -->
            <div class="bg-white rounded-xl shadow-md border-t-4 border-indigo-600 overflow-hidden flex flex-col transition-all">
                <div class="p-5">
                    <h3 class="text-lg font-bold text-slate-900 mb-2">Optimization</h3>
                    <p class="text-sm text-slate-600 mb-4">Glimpse: Geometric properties and optimization.</p>
                    <button onclick="toggleCard(this)" class="text-indigo-600 font-medium text-sm hover:underline">Show Glimpse ▾</button>
                </div>
                <div class="hidden flex-col p-5 border-t border-slate-100 bg-slate-50">
                    <img src="Special/optimization.png" alt="Optimization Cheat Sheet" class="w-full rounded mb-4 shadow-sm">
                    <a href="math-and-optimization.html" class="block w-full text-center py-2 bg-indigo-600 text-white hover:bg-indigo-700 rounded-lg font-medium transition-colors text-sm">
                        Explore More in Math & Viz
                    </a>
                </div>
            </div>

            <!-- Card 5: Keynesian IS Shocks -->
            <div class="bg-white rounded-xl shadow-md border-t-4 border-indigo-600 overflow-hidden flex flex-col transition-all">
                <div class="p-5">
                    <h3 class="text-lg font-bold text-slate-900 mb-2">Keynesian IS Shocks</h3>
                    <p class="text-sm text-slate-600 mb-4">Glimpse: Shifts in the IS curve.</p>
                    <button onclick="toggleCard(this)" class="text-indigo-600 font-medium text-sm hover:underline">Show Glimpse ▾</button>
                </div>
                <div class="hidden flex-col p-5 border-t border-slate-100 bg-slate-50">
                    <img src="Special/(Shocks in Keynesian)SHIFTS IN THE IS CURVE.png" alt="Shocks in Keynesian IS Curve" class="w-full rounded mb-4 shadow-sm">
                    <a href="macroeconomics.html" class="block w-full text-center py-2 bg-indigo-600 text-white hover:bg-indigo-700 rounded-lg font-medium transition-colors text-sm">
                        Explore More in Macroeconomics
                    </a>
                </div>
            </div>
            
        </div>"""

for file_path in files_to_update:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Try to find the section
        # We need to find the start of the grid
        grid_start = content.find('<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6')
        if grid_start == -1:
            print(f"Could not find start of grid in {file_path}")
            continue
            
        # The section ends at </section>
        section_end = content.find('</section>', grid_start)
        if section_end == -1:
            print(f"Could not find end of section in {file_path}")
            continue
            
        # Extract the content from grid_start up to the last </div> before </section>
        # Let's just find the last </div> before section_end
        last_div_end = content.rfind('</div>', grid_start, section_end) + 6
        
        # We replace the text
        new_content = content[:grid_start] + new_spotlight + content[last_div_end:]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Successfully updated {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
