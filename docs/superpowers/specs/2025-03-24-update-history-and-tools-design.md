# Design Doc: Update History and Tools Page

**Date:** 2025-03-24
**Status:** Draft

## Goal
Update `site_build/history-and-tools.html` to include missing history resources and audio podcasts, and remove the redundant sticky audio player.

## Resources to Add

### 1. Books & Authors
- **Document:** `CUET PG Economics Books, Authors & International trade theory.docx`
  - Path: `Econ-entrance-more-resources/CUET Indian Econ Docs/CUET Deep Research Docs/`
- **Image:** `Imprtant Books and Authors.png`
  - Path: `Econ-entrance-more-resources/Econ images/`

### 2. Audio Podcasts
- `India’s_$45_Trillion_Heist_and_Recovery.m4a`
- `Major_Economists_and_their_Economic_Theories.m4a`
- `(More)Books_and_authors.m4a`
- Path: `Econ-entrance-more-resources/Great_audio_Podcasts/`

## Structural Changes

### Section: Economists & Theories
- Add two new cards to the existing grid.
- One for the Word document (using `fa-file-word` icon).
- One for the PNG image (showing a thumbnail).

### Section: Podcasts & Audio Notes (New)
- Add a new section after "Study Tools & Planning".
- Use a list layout for audio files.
- Each item will include a headphone icon, the title, and a download link.

### Sticky Audio Player
- Remove the sticky audio player and its associated JavaScript logic to simplify the UI and focus on direct access.

## Technical Details
- Use Tailwind CSS for styling, consistent with the existing page.
- Ensure all relative paths are correctly URL-encoded.
- Maintain mobile responsiveness with `grid-cols-1` and `md:grid-cols-2`.

## Success Criteria
- [ ] Books & Authors resources are visible and accessible.
- [ ] Podcasts section is present with all three files.
- [ ] Sticky audio player is completely removed.
- [ ] Page layout remains clean and functional.
