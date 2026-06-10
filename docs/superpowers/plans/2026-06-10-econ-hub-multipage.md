# Econ Entrance Hub Multi-Page Pivot Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Pivot the architecture to a multi-page static site in a `site_build/` directory with interactive spotlight cards and 5 dedicated category pages.

**Architecture:** A static site generated inside `site_build/`. Assets from `Stuff to add in directory/` will be copied here. Each `.html` page will include the global Top Navigation and the Sticky Audio Player. The Spotlight cards on the landing page will use Vanilla JS to expand inline and show a preview, rather than opening images in a new tab, with an "Explore More" link routing to the appropriate category page.

**Tech Stack:** HTML5, Tailwind CSS (CDN), Vanilla JS, Bash (for asset copying).

---

### Task 1: Setup `site_build` and Assets

**Files:**
- Create: `build.sh`

- [ ] **Step 1: Write a build script to set up directories and copy assets**

```bash
#!/bin/bash
mkdir -p site_build
cp -r "Stuff to add in directory/Special" "site_build/"
cp -r "Stuff to add in directory/Econ-entrance-more-resources" "site_build/"
echo "Assets copied to site_build successfully."
```

- [ ] **Step 2: Run the script**

```bash
chmod +x build.sh
./build.sh
```

- [ ] **Step 3: Commit**

```bash
git add build.sh site_build/
git commit -m "chore: setup site_build directory and copy assets"
```

---

### Task 2: Refactor `index.html` Landing Page

**Files:**
- Modify: `site_build/index.html`

- [ ] **Step 1: Copy existing index.html to site_build**

```bash
cp index.html site_build/index.html
```

- [ ] **Step 2: Add Top Navigation**

*Replace the `<body>` tag and insert the nav just before the Hero `<header>` in `site_build/index.html`:*

```html
<body class="bg-slate-50 text-slate-800 font-sans pb-24"> <!-- pb-24 for sticky player space -->
    
    <!-- Top Navigation -->
    <nav class="sticky top-0 bg-white/90 backdrop-blur-md border-b border-slate-200 z-40">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16">
                <div class="flex">
                    <div class="flex-shrink-0 flex items-center">
                        <a href="index.html" class="font-bold text-xl text-indigo-600">Econ Entrance Hub</a>
                    </div>
                </div>
                <div class="hidden sm:ml-6 sm:flex sm:space-x-8 items-center">
                    <a href="indian-economy.html" class="text-sm font-medium text-slate-500 hover:text-slate-900">Indian Economy</a>
                    <a href="macroeconomics.html" class="text-sm font-medium text-slate-500 hover:text-slate-900">Macro</a>
                    <a href="microeconomics.html" class="text-sm font-medium text-slate-500 hover:text-slate-900">Micro</a>
                    <a href="math-and-optimization.html" class="text-sm font-medium text-slate-500 hover:text-slate-900">Math</a>
                    <a href="history-and-tools.html" class="text-sm font-medium text-slate-500 hover:text-slate-900">History & Tools</a>
                </div>
            </div>
        </div>
    </nav>
```

- [ ] **Step 3: Rewrite Spotlight Cards for Interactive Expansion**

*Replace the entire `<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">` block in `site_build/index.html` with this interactive version:*

```html
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" id="spotlight-grid">
            
            <!-- Card 1 -->
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

            <!-- Card 2 -->
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

            <!-- Card 3 -->
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

            <!-- Card 4 -->
            <div class="bg-white rounded-xl shadow-md border-t-4 border-indigo-600 overflow-hidden flex flex-col transition-all">
                <div class="p-5">
                    <h3 class="text-lg font-bold text-slate-900 mb-2">Economists' Theories</h3>
                    <p class="text-sm text-slate-600 mb-4">Glimpse: Mapping of major economists.</p>
                    <button onclick="toggleCard(this)" class="text-indigo-600 font-medium text-sm hover:underline">Show Glimpse ▾</button>
                </div>
                <div class="hidden flex-col p-5 border-t border-slate-100 bg-slate-50">
                    <img src="Special/Many Economists' Theories.png" alt="Many Economists' Theories" class="w-full rounded mb-4 shadow-sm">
                    <a href="history-and-tools.html" class="block w-full text-center py-2 bg-indigo-600 text-white hover:bg-indigo-700 rounded-lg font-medium transition-colors text-sm">
                        Explore More in History
                    </a>
                </div>
            </div>
            
        </div>
```

- [ ] **Step 4: Add Toggle Script**

*Insert this script right before `<!-- Audio Player Logic -->` at the bottom of `site_build/index.html`:*

```html
    <!-- Card Toggle Logic -->
    <script>
        function toggleCard(btn) {
            const previewDiv = btn.parentElement.nextElementSibling;
            if (previewDiv.classList.contains('hidden')) {
                previewDiv.classList.remove('hidden');
                previewDiv.classList.add('flex');
                btn.textContent = 'Hide Glimpse ▴';
            } else {
                previewDiv.classList.add('hidden');
                previewDiv.classList.remove('flex');
                btn.textContent = 'Show Glimpse ▾';
            }
        }
    </script>
```

- [ ] **Step 5: Link Categories correctly**
*Update the 4 category links in the "Explore All Resources" section of `site_build/index.html` to point to the new HTML pages:*
1. Indian Economy -> `indian-economy.html`
2. Math & Visualizations -> `math-and-optimization.html`
3. Economic Surveys -> `indian-economy.html` (or a dedicated page if needed, pointing to Indian Economy for now).
4. Micro/Macro Concept Vault -> `microeconomics.html`

- [ ] **Step 6: Commit**
```bash
git add site_build/index.html
git commit -m "feat: implement interactive spotlight cards and site routing"
```

---

### Task 3: Create `indian-economy.html`

**Files:**
- Create: `site_build/indian-economy.html`

- [ ] **Step 1: Write HTML**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Indian Economy - Econ Entrance Hub</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body class="bg-slate-50 text-slate-800 font-sans pb-24">
    
    <!-- Top Navigation -->
    <nav class="sticky top-0 bg-white/90 backdrop-blur-md border-b border-slate-200 z-40">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16">
                <div class="flex items-center">
                    <a href="index.html" class="font-bold text-xl text-indigo-600">Econ Entrance Hub</a>
                </div>
                <div class="hidden sm:flex sm:space-x-8 items-center">
                    <a href="indian-economy.html" class="text-sm font-medium text-indigo-600 border-b-2 border-indigo-600 h-full flex items-center">Indian Economy</a>
                    <a href="macroeconomics.html" class="text-sm font-medium text-slate-500 hover:text-slate-900">Macro</a>
                    <a href="microeconomics.html" class="text-sm font-medium text-slate-500 hover:text-slate-900">Micro</a>
                    <a href="math-and-optimization.html" class="text-sm font-medium text-slate-500 hover:text-slate-900">Math</a>
                    <a href="history-and-tools.html" class="text-sm font-medium text-slate-500 hover:text-slate-900">History & Tools</a>
                </div>
            </div>
        </div>
    </nav>

    <main class="max-w-7xl mx-auto px-4 py-12">
        <h1 class="text-4xl font-extrabold text-slate-900 mb-8">Indian Economy & Economic Development</h1>
        
        <section class="mb-12">
            <h2 class="text-2xl font-bold mb-4">Deep Research Docs</h2>
            <div class="bg-white p-6 rounded-xl shadow-md">
                <a href="Econ-entrance-more-resources/CUET Indian Econ Docs/CUET Deep Research Docs/" target="_blank" class="text-indigo-600 hover:underline block mb-2"><i class="fa-solid fa-folder"></i> CUET Deep Research Docs</a>
                <a href="Econ-entrance-more-resources/IIT JAM Indian Econ Docs/" target="_blank" class="text-indigo-600 hover:underline block"><i class="fa-solid fa-folder"></i> IIT JAM Indian Econ Docs</a>
            </div>
        </section>

        <section class="mb-12">
            <h2 class="text-2xl font-bold mb-4">Economic Surveys (2016-2025)</h2>
            <div class="bg-white p-6 rounded-xl shadow-md">
                <a href="Econ-entrance-more-resources/Economic_Surveys/" target="_blank" class="text-indigo-600 hover:underline block mb-2"><i class="fa-solid fa-folder"></i> Browse All Economic Surveys</a>
            </div>
        </section>
    </main>

    <footer class="py-8 text-center text-slate-500 text-sm border-t border-slate-200 mt-8 mb-20">
        <a href="index.html" class="text-indigo-600 hover:underline">&larr; Back to Hub</a>
    </footer>

</body>
</html>
```

- [ ] **Step 2: Append Sticky Player**
*Copy the `<!-- Sticky Audio Player -->` and `<script>` logic from `site_build/index.html` and insert it before the closing `</body>` in `indian-economy.html`.*

- [ ] **Step 3: Commit**

```bash
git add site_build/indian-economy.html
git commit -m "feat: add indian economy category page"
```

---

### Task 4: Create `macroeconomics.html`

**Files:**
- Create: `site_build/macroeconomics.html`

- [ ] **Step 1: Write HTML**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Macroeconomics - Econ Entrance Hub</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body class="bg-slate-50 text-slate-800 font-sans pb-24">
    
    <nav class="sticky top-0 bg-white/90 backdrop-blur-md border-b border-slate-200 z-40">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16">
                <div class="flex items-center">
                    <a href="index.html" class="font-bold text-xl text-indigo-600">Econ Entrance Hub</a>
                </div>
                <div class="hidden sm:flex sm:space-x-8 items-center">
                    <a href="indian-economy.html" class="text-sm font-medium text-slate-500 hover:text-slate-900">Indian Economy</a>
                    <a href="macroeconomics.html" class="text-sm font-medium text-indigo-600 border-b-2 border-indigo-600 h-full flex items-center">Macro</a>
                    <a href="microeconomics.html" class="text-sm font-medium text-slate-500 hover:text-slate-900">Micro</a>
                    <a href="math-and-optimization.html" class="text-sm font-medium text-slate-500 hover:text-slate-900">Math</a>
                    <a href="history-and-tools.html" class="text-sm font-medium text-slate-500 hover:text-slate-900">History & Tools</a>
                </div>
            </div>
        </div>
    </nav>

    <main class="max-w-7xl mx-auto px-4 py-12">
        <h1 class="text-4xl font-extrabold text-slate-900 mb-8">Macroeconomics & International Finance</h1>
        
        <section class="mb-12">
            <h2 class="text-2xl font-bold mb-4">IS-LM & Shocks</h2>
            <div class="grid md:grid-cols-2 gap-6">
                <div class="bg-white p-4 rounded-xl shadow-md text-center">
                    <img src="Econ-entrance-more-resources/Econ images/(Shocks In Classical)SHIFTS IN THE IS CURVE.png.png" class="w-full h-auto mb-2 rounded" alt="Classical IS">
                    <p class="font-bold text-sm">Classical IS Shifts</p>
                </div>
                <div class="bg-white p-4 rounded-xl shadow-md text-center">
                    <img src="Special/(Shocks in Keynesian)SHIFTS IN THE IS CURVE.png" class="w-full h-auto mb-2 rounded" alt="Keynesian IS">
                    <p class="font-bold text-sm">Keynesian IS Shifts</p>
                </div>
            </div>
        </section>

        <section class="mb-12">
            <h2 class="text-2xl font-bold mb-4">Mundell-Fleming (Animated)</h2>
            <div class="grid md:grid-cols-2 gap-6">
                <div class="bg-white p-4 rounded-xl shadow-md text-center">
                    <img src="Econ-entrance-more-resources/Econ images/mundell_fleming_detailed.gif" class="w-full h-auto mb-2 rounded border border-slate-100" alt="Mundell Fleming">
                    <p class="font-bold text-sm">Detailed Model</p>
                </div>
                <div class="bg-white p-4 rounded-xl shadow-md text-center">
                    <img src="Econ-entrance-more-resources/Econ images/Flexible_ER_cases.gif" class="w-full h-auto mb-2 rounded border border-slate-100" alt="Flexible ER">
                    <p class="font-bold text-sm">Flexible Exchange Rates</p>
                </div>
            </div>
        </section>
    </main>

    <footer class="py-8 text-center text-slate-500 text-sm border-t border-slate-200 mt-8 mb-20">
        <a href="index.html" class="text-indigo-600 hover:underline">&larr; Back to Hub</a>
    </footer>
</body>
</html>
```

- [ ] **Step 2: Append Sticky Player**
*Copy the `<!-- Sticky Audio Player -->` and `<script>` logic from `site_build/index.html` and insert it before the closing `</body>` in `macroeconomics.html`.*

- [ ] **Step 3: Commit**

```bash
git add site_build/macroeconomics.html
git commit -m "feat: add macroeconomics category page"
```

---

### Task 5: Complete other category pages (Micro, Math, History)

**Files:**
- Create: `site_build/microeconomics.html`
- Create: `site_build/math-and-optimization.html`
- Create: `site_build/history-and-tools.html`

- [ ] **Step 1: Write basic HTML wrappers with Nav and Footer for the remaining 3 pages**
Use the same structure as Task 4, updating the Title, H1, and active Nav state. Link to a few key images from `Econ-entrance-more-resources/` in each according to the Site Map doc. Make sure to append the Audio Player to all 3.

- [ ] **Step 2: Commit**

```bash
git add site_build/*.html
git commit -m "feat: add remaining category pages"
```