# 🏗️ UI Architecture & Site Mapping: Econ Entrance Hub

## 1. Project Objective & Build Logic
**Role:** Expert Frontend Developer & Architect.
**Task:** Build a multi-page static website (HTML/Tailwind CSS) that acts as a navigational hub for economics entrance exam resources. 
**Context:** You have access to a parent directory containing two raw asset folders: `Special/` and `Econ-entrance-more-resources/`. 
**Action:** 1. Create a new directory named `site_build/`.
2. Generate the necessary `.html` files inside `site_build/`.
3. Construct relative links in the HTML files that point back to the raw assets in `Special/` and `Econ-entrance-more-resources/`, OR write a script/instruction to copy those assets into `site_build/assets/` to ensure deployment works smoothly.

---

## 2. Global UI / UX Design System
* **Framework:** Tailwind CSS (via CDN).
* **Layout:**
  * **Top Navigation Bar:** Sticky at the top. Contains the logo ("Econ Entrance Hub"), links to the 5 main subject categories, and external links to the CBT and Doubts websites.
  * **Main Content Area:** Max-width container (`max-w-7xl mx-auto`), well-padded, using a clean `bg-slate-50` background.
  * **Global Sticky Audio Player:** Fixed to the `bottom-0`. This player is included only on the main index page (it should disappear when navigating to other routes). It loads audio files from the `Special/` folder.
* **Component Styles:**
  * **Cards:** White background, rounded corners (`rounded-xl`), subtle shadow (`shadow-md`), hover effect (`hover:shadow-lg hover:-translate-y-1 transition`).
  * **Buttons:** Indigo/Blue primary colors (`bg-indigo-600 hover:bg-indigo-700 text-white`).

---

## 3. Page Routing & Asset Mapping

The site will consist of a main landing page and 5 dedicated category pages.

### 📄 1. `index.html` (The Main Landing Page)
* **Hero Section:** Title, Subtitle, and CTAs for the external CBT/Doubts sites.
* **The "Spotlight" Section:** A grid of highly visual cards highlighting the best resources from the `Special/` directory:
  * Image Card: *International Trade* (`Special/International Trade.png`)
  * Image Card: *Optimization* (`Special/optimization.png`)
  * Image Card: *Keynesian Shocks* (`Special/(Shocks in Keynesian)SHIFTS IN THE IS CURVE.png`)
  * Link Card: *Notebook Compilations* (`Special/Notebook lm links compilation.md`)
* **Category Hub:** 5 prominent cards linking to the HTML pages detailed below.

### 📄 2. `indian-economy.html`
* **Header:** "Indian Economy & Economic Development"
* **Content Grid:**
  * **Exam Docs:** Link to items in `Econ-entrance-more-resources/CUET Indian Econ Docs/` and `IIT JAM Indian Econ Docs/`.
  * **Module Cheat Sheets:** List the 5 Word documents from the `Indian Eco different Sectors...` folder.
  * **Visual Jargon:** Display thumbnails for `Jargon Development Econ.png`, `Jargon PUBLIC ECONOMICS.png`, and the `notebook All...` PNGs.
  * **Economic Surveys:** A dedicated list/table linking to the 2016-2025 PDFs in `Econ-entrance-more-resources/Economic_Surveys/`.

### 📄 3. `macroeconomics.html`
* **Header:** "Macroeconomics & International Finance"
* **Content Grid:**
  * **IS-LM & AS-AD:** Embed or link to `SHIFTS IN THE IS CURVE.png.png` and `The 'Great Inversion'...png`.
  * **Mundell-Fleming (GIFs):** Embed the animated GIFs (`mundell_fleming_detailed.gif`, `Flexible_ER_cases.gif`, etc.) so they play on the page.
  * **Theory:** Links to `International Trade Theory.png` and `Adaptive and Rational expectations.png`.

### 📄 4. `microeconomics.html`
* **Header:** "Microeconomics"
* **Content Grid:**
  * **Core Theory:** Cards linking to `consumer theory concepts.png`, `Production theory Theorems.png`.
  * **Market Structures:** Embed `Cheat Sheet of Geometric Properties for Market Structures.png` and `Duopoly Cheat Sheet...png`.
  * **Welfare:** Link to `Deadweight loss Price subsidy...png`.

### 📄 5. `math-and-optimization.html`
* **Header:** "Mathematical Economics & Optimization"
* **Content Grid:**
  * **Math GIFs:** Embed `minkowski_sweep.gif` and `quasi _concave_convex_dynamic.gif`.
  * **Cheat Sheets:** Grid of links/thumbnails for `Sequences.png`, `Series.png`, `PnC.png`, and `concavity vs quasi.png`.

### 📄 6. `history-and-tools.html`
* **Header:** "History of Economic Thought & Study Tools"
* **Content Grid:**
  * **Economists:** Link to `All Economists' Theories.docx` and `Many Economists' Theories.png`.
  * **Study Tools:** Link to `notebook all econ plans.png` and the interactive Markdown files.

---

## 4. Implementation Rules for the CLI
1. **Do not hallucinate files:** Only create HTML links and image `src` tags for the exact filenames provided in the context.
2. **Handle spaces in filenames:** Ensure file paths with spaces (e.g., `International Trade.png`) are properly URL-encoded (e.g., `International%20Trade.png`) in the HTML `href` and `src` attributes.
3. **Write modular code:** Keep the Tailwind classes clean and readable. Use semantic HTML tags (`<header>`, `<main>`, `<section>`, `<footer>`).