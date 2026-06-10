# Econ Entrance Hub Landing Page - Design Specification

## Overview
A single, highly polished static HTML file (`index.html`) serving as the main landing hub for Master's in Economics entrance exam preparation resources. Built with HTML5, Tailwind CSS (via CDN), and Vanilla JS.

## Tech Stack
* **Markup:** HTML5
* **Styling:** Tailwind CSS (via CDN: `<script src="https://cdn.tailwindcss.com"></script>`)
* **Icons:** FontAwesome or Heroicons (via CDN)
* **Interactivity:** Vanilla JS within `<script>` tags for audio player state.
* **Build:** Zero build tools; a raw static `index.html`.

## Visual Identity & Theme
* **Default Theme:** Light mode (white background) with high-contrast readable text. No dark mode by default for the main content area.
* **Vibe:** Academic, modern, organized, and clean.
* **Colors:** Slate/gray for typography and secondary elements. Indigo/blue for primary accents and CTA buttons.

## Architecture & Layout

### 1. Header & Hero Section
* **Layout:** Centered and Minimalist.
* **Content:**
    * Title: "Econ Entrance Hub"
    * Subtitle: "The ultimate, curated collection of visual cheat sheets, audio notes, and deep-research docs for CUET PG & IIT JAM."
* **CTAs:** Side-by-side buttons.
    * Primary (Solid): "Attempt CBT Mock Tests" (Link: `https://econ-entrance-cbt-tests.pages.dev/`)
    * Secondary (Outlined): "Doubts & Explanations" (Link: `http://econ-entrance-doubts-and-explanations.pages.dev/`)

### 2. "Special Spotlight" Cards Grid
* **Layout:** Responsive grid (`grid-cols-1 md:grid-cols-2 lg:grid-cols-3`).
* **Style:** Elevated & Academic. White cards with a top colored border (indigo), slightly rounded corners, and a distinct drop shadow (`shadow-md` to `hover:shadow-xl`).
* **Content:**
    * Thumbnail area (gray placeholder or actual image scaled to fit).
    * Title & Description.
    * "View/Download" Button.
* **Specific Resources:**
    * "International Trade" (`Special/International Trade.png`)
    * "Optimization Cheat Sheet" (`Special/optimization.png`)
    * "Many Economists' Theories" (`Special/Many Economists' Theories.png`)
    * "Shocks in Keynesian IS Curve" (`Special/(Shocks in Keynesian)SHIFTS IN THE IS CURVE.png`)
    * "Interactive Study Notebooks" (`Special/Notebook lm links compilation.md` - `target="_blank"`)

### 3. Deep Dive Categories
* **Layout:** "Explore All Resources" section below the spotlight. Staggered grid or list of stylized cards.
* **Categories:**
    * Indian Economy (`Econ-entrance-more-resources/CUET Indian Econ Docs/` & `IIT JAM Indian Econ Docs/`)
    * Math & Visualizations (`Econ-entrance-more-resources/Math Viz/`)
    * Economic Surveys (2016-2025) (`Econ-entrance-more-resources/Economic_Surveys/`)
    * Micro/Macro Concept Vault (`Econ-entrance-more-resources/Econ images/`)

### 4. Sticky Audio Player
* **Layout:** Fixed to bottom of viewport (`fixed bottom-0 left-0 w-full z-50`). Sleek dark background (`bg-slate-900 text-white`).
* **Style:** Custom UI (Playlist style).
* **Components:**
    * Custom play/pause toggle button.
    * Track metadata display (Title).
    * Custom progress bar mapping to the underlying hidden `<audio>` element's time.
    * Dropdown `<select>` to switch between tracks.
    * Dynamic "Download" button mapping to the active track's path.
* **Tracks:**
    1. "Major Economists and their Economic Theories" (`Special/Major_Economists_and_their_Economic_Theories.m4a`)
    2. "India’s $45 Trillion Heist and Recovery" (`Special/India’s_$45_Trillion_Heist_and_Recovery.m4a`)
    3. "Books and Authors" (`Special/(More)Books_and_authors.m4a`)

### 5. Footer
* **Layout:** Simple, centered content.
* **Content:** GitHub repository link and a copyright/open-source notice.

## Data Flow & State Management
* The application is static. All data (file paths, titles) is hardcoded into the HTML structure.
* **Audio Player State:** Vanilla JS will maintain state for the currently selected track index, play/pause status, and current time. It will listen to the native `audio` element events (`timeupdate`, `ended`) to drive the custom UI progress bar, and attach `click` listeners to the custom controls.

## Edge Cases & Error Handling
* Fallback styling for images that fail to load (using standard `alt` tags and background colors on image containers).
* Audio paths must explicitly match the relative paths provided to ensure they work when served from the repository root.

## Testing Strategy
* Manual verification of responsive layout (Mobile, Tablet, Desktop viewports).
* Functional verification of the custom audio player (Play, Pause, Track Switching, Audio Progress updates, Download link updates).
* Link validation ensuring paths correctly match `Special/` and `Econ-entrance-more-resources/` structure.