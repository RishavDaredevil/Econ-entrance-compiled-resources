# Update Math Resources Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add missing math visualization (GIF) and cheat sheets (PNGs) to `site_build/math-and-optimization.html`.

**Architecture:** Update the existing Tailwind CSS grid layout in the HTML file to include new resource cards.

**Tech Stack:** HTML, Tailwind CSS.

---

### Task 1: Add missing GIF to "Math Visualizations"

**Files:**
- Modify: `site_build/math-and-optimization.html`

- [ ] **Step 1: Locate the "Math Visualizations" section and add the new GIF card.**

The new card for `Importance for conditions Like convex set & Quasi concave functions.gif` should be added to the grid.

```html
<div class="bg-white p-4 rounded-xl shadow-md text-center">
    <img src="Econ-entrance-more-resources/Math%20Viz/Importance%20for%20conditions%20Like%20convex%20set%20&%20Quasi%20concave%20functions.gif" class="w-full h-auto mb-2 rounded border border-slate-100" alt="Convex Set & Quasi Concave Functions">
    <p class="font-bold text-sm">Convex Set & Quasi Concave Functions</p>
</div>
```

- [ ] **Step 2: Verify the change manually by checking the HTML structure.**

- [ ] **Step 3: Commit.**

```bash
git add site_build/math-and-optimization.html
git commit -m "feat: add convex set & quasi concave functions GIF to math visualizations"
```

---

### Task 2: Add missing PNGs to "Cheat Sheets"

**Files:**
- Modify: `site_build/math-and-optimization.html`

- [ ] **Step 1: Locate the "Cheat Sheets" section and add the new PNG cards.**

Add `Figure_2.png`, `translations_corrected.png`, and `optimization.png`.

```html
<div class="bg-white p-4 rounded-xl shadow-md text-center">
    <a href="Econ-entrance-more-resources/Math%20Viz/Figure_2.png" target="_blank">
        <img src="Econ-entrance-more-resources/Math%20Viz/Figure_2.png" class="w-full h-32 object-cover mb-2 rounded" alt="Figure 2">
        <p class="font-bold text-sm text-indigo-600 hover:underline">Figure 2</p>
    </a>
</div>
<div class="bg-white p-4 rounded-xl shadow-md text-center">
    <a href="Econ-entrance-more-resources/Math%20Viz/translations_corrected.png" target="_blank">
        <img src="Econ-entrance-more-resources/Math%20Viz/translations_corrected.png" class="w-full h-32 object-cover mb-2 rounded" alt="Translations Corrected">
        <p class="font-bold text-sm text-indigo-600 hover:underline">Translations Corrected</p>
    </a>
</div>
<div class="bg-white p-4 rounded-xl shadow-md text-center">
    <a href="Econ-entrance-more-resources/Math%20Viz/optimization.png" target="_blank">
        <img src="Econ-entrance-more-resources/Math%20Viz/optimization.png" class="w-full h-32 object-cover mb-2 rounded" alt="Optimization">
        <p class="font-bold text-sm text-indigo-600 hover:underline">Optimization</p>
    </a>
</div>
```

- [ ] **Step 2: Verify the change manually by checking the HTML structure.**

- [ ] **Step 3: Commit.**

```bash
git add site_build/math-and-optimization.html
git commit -m "feat: add Figure 2, translations corrected, and optimization cheat sheets"
```
