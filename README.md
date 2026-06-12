# 🎓 Econ Entrance Hub (India)

**[🌐 Click here to visit the Live Website!](https://rishavdaredevil.github.io/Econ-entrance-compiled-resources/)**

Welcome to my personal, curated collection of resources for Master's in Economics Aspirants in India! 

This repository serves as a central hub for students preparing for **ISI MSQE, CUET PG, and IIT JAM**. It compiles high-yield study materials, visual cheat sheets, audio notes, and deep-research documents to streamline your exam preparation.

---

## 🌐 The Econ Entrance Ecosystem

This project is part of a three-tier study ecosystem designed to cover all aspects of exam prep:

1. **📚 The Resource Hub (This Repository):**
   The primary static site hosting categorized study materials, visual aids, and interactive notebooks. **[Visit Site](https://rishavdaredevil.github.io/Econ-entrance-compiled-resources/)**
2. **💻 CBT Mock Tests Platform:**
   A platform to practice Previous Year Questions (PYQs) using an interactive, simulated Computer-Based Test (CBT) interface. It tracks your attempt statistics and time spent on each question alongside the official exam PDFs.
3. **💬 Doubts & Explanations Repository:**
   A unified portal hosting 31+ detailed explanation papers for ISI MSQE, CUET PG, and IIT JAM. It features personal doubts encountered while solving PYQs and their comprehensive explanations.

⭐ **If you find this ecosystem helpful for your preparation, please consider giving the repository a star!** ⭐

---

## 📦 What's Inside?

The repository contains an exhaustive classification of materials across five major domains:

### 1. Indian Economy & Economic Development
* **Deep Research Docs:** Comprehensive timelines, recent data policy analysis, and revision guides for CUET & IIT JAM.
* **Sector-wise Modules:** Detailed cheat sheets covering Fiscal Policy, Macroeconomic Indicators, Monetary Policy, Agriculture, Demographics, and Industrial Policy.
* **Visual Cheat Sheets:** Grids of important committees, acts, schemes, and development economics jargon.
* **Economic Surveys:** A complete archive of Economic Surveys from 2016 to 2025.

### 2. Macroeconomics & International Finance
* **Mundell-Fleming Model:** Animations (GIFs) illustrating perfectly mobile vs. immobile capital, along with a custom Python simulation script (`Visualising Mundell Fleming.py`).
* **Macro Models & Expectations:** Visualizations of the 2008 Liquidity Trap, Adaptive vs. Rational Expectations, and the 'Great Inversion' AS Curve.
* **International Trade Theory:** Trade theory overviews, BP curve derivations, and Indian international trade summaries.

### 3. Microeconomics
* **Core Theory:** Visual guides for consumer theory, production theorems, and labor supply graphs.
* **Market Structures & Welfare:** Cheat sheets for geometric properties of monopolies and duopolies, as well as deadweight loss analyses for subsidies, price floors, and quotas.

### 4. Math & Optimization
* **Math Visualizations:** Animated visualizations of Minkowski sweeps, convex sets, and quasi-concavity.
* **Optimization Cheat Sheets:** Guides for sequences, series, permutations & combinations (PnC), and Figure 2 geometry translations.

### 5. History of Economic Thought & Study Tools
* **Economists & Theories:** Detailed documents and mappings of major economists and their respective theories.
* **Podcasts & Audio Notes:** Custom audio overviews on Major Economists, Books and Authors, and India's $45 Trillion Heist. (Includes an integrated persistent audio player on the main hub).
* **Interactive Notebooks:** Links to Notebook LM compilations equipped with quizzes and flashcards for active recall.

---

## 🛠️ Technical Details & Deployment

* **Tech Stack:** HTML, Tailwind CSS, and FontAwesome.
* **Site Architecture:** A lightweight static site generated into the `site_build/` directory.
* **Deployment:** Hosted on **GitHub Pages**, automatically deployed via a GitHub Actions workflow (`.github/workflows/deploy.yml`) triggered upon pushing to the `master` branch.

### Local Setup

To preview the site locally:

1. Clone the repository.
2. Run the build script to compile the assets:
   ```bash
   ./build.sh
   ```
3. Serve the `site_build` directory locally using Python's built-in HTTP server. To start the server on a specific port (e.g., port 8000), run:
   ```bash
   python3 -m http.server 8000 --directory site_build
   ```
4. Open your browser and navigate to `http://localhost:8000`.

---

*Happy studying, and best of luck with your entrance exams!* 🎯

⭐ **Don't forget to star the project if it helped you!** ⭐