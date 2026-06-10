# Project Goal: Build a Modern "Master's in Economics Entrance Hub" Landing Page

## Objective
Act as an expert frontend developer. Your task is to generate a single, highly polished static HTML file (`index.html`) using **Tailwind CSS (via CDN)**. This page will serve as the main landing hub for aspirants preparing for Master's in Economics entrance exams in India (CUET PG, IIT JAM, etc.).

## Tech Stack
* **HTML5**
* **Tailwind CSS** (Include via `<script src="https://cdn.tailwindcss.com"></script>`)
* **FontAwesome** or Heroicons (for UI icons)
* **Vanilla JS** (embedded within `<script>` tags only if necessary for basic interactions like toggling modals or audio).
* **Zero build tools:** Deliver a clean, ready-to-deploy static `index.html` file.

## Design Aesthetic
* **Vibe:** Academic, modern, organized, and clean. 
* **Color Palette:** Professional tones. Use Tailwind's `slate` or `gray` for backgrounds, and `blue` or `indigo` for primary accents and buttons.
* **Responsiveness:** Must look excellent on both mobile devices and desktop screens.

---

## Page Structure & Requirements

### 1. Header & Hero Section
* **Title:** "Econ Entrance Hub"
* **Subtitle:** "The ultimate, curated collection of visual cheat sheets, audio notes, and deep-research docs for CUET PG & IIT JAM."
* **Primary CTA Buttons (Side-by-Side):**
    * Button 1: "Attempt CBT Mock Tests" -> links to `https://econ-entrance-cbt-tests.pages.dev/` (Style as solid primary color).
    * Button 2: "Doubts & Explanations" -> links to `http://econ-entrance-doubts-and-explanations.pages.dev/` (Style as outlined primary color).

### 2. The "Special Spotlight" (Visual Cards Grid)
* Create a responsive grid (`grid-cols-1 md:grid-cols-2 lg:grid-cols-3`).
* Design these as **beautiful, elevated cards** with hover effects (`hover:-translate-y-1 hover:shadow-lg transition-all`).
* Each card should represent a key visual resource from the `Special/` directory.
* **Card structure:** Thumbnail/Icon at the top, Title, brief description, and a button to "View/Download".
* **Include these specific items as cards:**
    * "International Trade" (`Special/International Trade.png`)
    * "Optimization Cheat Sheet" (`Special/optimization.png`)
    * "Many Economists' Theories" (`Special/Many Economists' Theories.png`)
    * "Shocks in Keynesian IS Curve" (`Special/(Shocks in Keynesian)SHIFTS IN THE IS CURVE.png`)
    * "Interactive Study Notebooks" (`Special/Notebook lm links compilation.md`) - Note: Open in new tab.

### 3. Deep Dive Categories (Category Grid Layout)
* Below the special spotlight, create a section titled "Explore All Resources".
* Use a staggered grid or clean list of stylized cards that point to the sub-directories.
* **Categories to include:**
    * **Indian Economy:** Link to `Econ-entrance-more-resources/CUET Indian Econ Docs/` and `IIT JAM Indian Econ Docs/`
    * **Math & Visualizations:** Mention GIFs and graphs. Link to `Econ-entrance-more-resources/Math Viz/`
    * **Economic Surveys (2016-2025):** Link to `Econ-entrance-more-resources/Economic_Surveys/`
    * **Micro/Macro Concept Vault:** Link to `Econ-entrance-more-resources/Econ images/`

### 4. The Sticky Audio Player (Crucial Feature)
* Implement a modern, **sticky audio player fixed to the bottom of the viewport** (`fixed bottom-0 left-0 w-full z-50`).
* It should look like a sleek podcast player panel with a dark background (`bg-slate-900 text-white`).
* **Layout:**
    * Left side: Currently playing title.
    * Center: The standard HTML `<audio controls>` element styled cleanly (or custom styled controls if you can achieve it via Vanilla JS, otherwise native is fine if it looks neat).
    * Right side: A dropdown `<select>` menu allowing the user to switch between tracks, plus a dynamic "Download" link for the selected track.
* **Audio Tracks to include in the dropdown (from the `Special/` directory):**
    1.  "Major Economists and their Economic Theories" (`Special/Major_Economists_and_their_Economic_Theories.m4a`)
    2.  "India’s $45 Trillion Heist and Recovery" (`Special/India’s_$45_Trillion_Heist_and_Recovery.m4a`)
    3.  "Books and Authors" (`Special/(More)Books_and_authors.m4a`)

### 5. Footer
* Keep it simple. Include GitHub link (`https://github.com/RishavDaredevil/Econ-entrance-compiled-resources`) and a copyright/open-source notice.

## Output Constraints
* Ensure all file paths explicitly match the provided `Special/` and `Econ-entrance-more-resources/` directory structures so that when I drop this `index.html` file into the root of my repository, the links work immediately.
* Provide the complete HTML code in a single code block.