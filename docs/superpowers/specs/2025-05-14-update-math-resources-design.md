# Design Doc: Update Math Resources Page
Date: 2025-05-14

## Goal
Add missing math visualizations and cheat sheets to `site_build/math-and-optimization.html`.

## Proposed Changes

### 1. Math Visualizations Section
- Add `Importance for conditions Like convex set & Quasi concave functions.gif`.
- Path: `Econ-entrance-more-resources/Math Viz/Importance%20for%20conditions%20Like%20convex%20set%20&%20Quasi%20concave%20functions.gif`
- Layout: standard card layout, added to the `grid md:grid-cols-2` (which might need to be adjusted or just let it flow). Actually, with 3 items, a 3-column grid on larger screens might be better, or just let it wrap.

### 2. Cheat Sheets Section
- Add `Figure_2.png`.
- Add `translations_corrected.png`.
- Add `optimization.png`.
- Path: `Econ-entrance-more-resources/Math Viz/Figure_2.png`
- Path: `Econ-entrance-more-resources/Math Viz/translations_corrected.png`
- Path: `Econ-entrance-more-resources/Math Viz/optimization.png`
- Layout: standard card layout with a link to the full image.

## Technical Details
- Use Tailwind CSS classes consistent with the existing page.
- Ensure all file names are correctly URL-encoded in the `src` and `href` attributes.
- Maintain responsive grid behavior.

## Verification Plan
- Manually inspect the HTML structure.
- Check that paths match the directory structure.
