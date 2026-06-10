# Indian Economy Page Update Design

**Goal:** Transform the sparse `site_build/indian-economy.html` into a comprehensive resource hub by listing 21+ specific files previously hidden behind folder links.

## Layout & Sections

1.  **CUET Deep Research Docs** (Word files)
    *   List layout with document icons.
2.  **Sector-wise Modules** (Word files)
    *   List layout focusing on the 5 modules.
3.  **IIT JAM Resources** (Word and PDF files)
    *   List layout including the poverty PDF.
4.  **Visual Cheat Sheets** (PNG/GIF files)
    *   Grid layout with thumbnails (if possible) or stylized cards.
5.  **Economic Surveys** (PDF files)
    *   Direct links to 2022-23, 2023-24, and 2024-25 PDFs.

## Tech Stack
*   HTML5
*   Tailwind CSS (via CDN)
*   FontAwesome (for icons)

## Navigation
*   Preserve existing top navigation.
*   Preserve "Back to Hub" footer.

## Testing Strategy
*   Verify that all paths are correct relative to `site_build/`.
*   Verify file existence using `ls`.
