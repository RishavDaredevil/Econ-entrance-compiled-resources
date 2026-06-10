# Update History and Tools Page Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Update `site_build/history-and-tools.html` to include new history resources and podcasts, and remove the sticky audio player.

**Architecture:** Surgical HTML/CSS updates to an existing static page.

**Tech Stack:** HTML5, Tailwind CSS, FontAwesome.

---

### Task 1: Update Economists & Theories Section

**Files:**
- Modify: `site_build/history-and-tools.html`

- [ ] **Step 1: Add Books & Authors Resources**
Insert two new cards into the "Economists & Theories" section grid.

```html
                <div class="bg-white p-4 rounded-xl shadow-md flex items-center gap-4 hover:shadow-lg transition">
                    <div class="bg-indigo-100 text-indigo-600 p-4 rounded-lg flex-shrink-0">
                        <i class="fa-solid fa-file-word text-2xl"></i>
                    </div>
                    <div>
                        <a href="Econ-entrance-more-resources/CUET%20Indian%20Econ%20Docs/CUET%20Deep%20Research%20Docs/CUET%20PG%20Economics%20Books,%20Authors%20&%20International%20trade%20theory.docx" class="font-bold text-lg text-indigo-600 hover:underline">Books, Authors & Trade Theory</a>
                        <p class="text-sm text-slate-500">CUET PG Research Doc</p>
                    </div>
                </div>

                <div class="bg-white p-4 rounded-xl shadow-md text-center hover:shadow-lg transition">
                    <a href="Econ-entrance-more-resources/Econ%20images/Imprtant%20Books%20and%20Authors.png" target="_blank">
                        <img src="Econ-entrance-more-resources/Econ%20images/Imprtant%20Books%20and%20Authors.png" class="w-full h-32 object-cover mb-2 rounded" alt="Important Books and Authors">
                        <p class="font-bold text-sm text-indigo-600 hover:underline">Important Books and Authors PNG</p>
                    </a>
                </div>
```

### Task 2: Add Podcasts & Audio Notes Section

**Files:**
- Modify: `site_build/history-and-tools.html`

- [ ] **Step 1: Insert New Section**
Add the "Podcasts & Audio Notes" section after the "Study Tools & Planning" section.

```html
        <section class="mb-12">
            <h2 class="text-2xl font-bold mb-4">Podcasts & Audio Notes</h2>
            <div class="grid md:grid-cols-1 gap-4">
                <!-- India's $45 Trillion Heist -->
                <div class="bg-white p-4 rounded-xl shadow-md flex items-center justify-between hover:shadow-lg transition">
                    <div class="flex items-center gap-4">
                        <div class="bg-indigo-100 text-indigo-600 p-3 rounded-full">
                            <i class="fa-solid fa-podcast text-xl"></i>
                        </div>
                        <div>
                            <h4 class="font-bold text-slate-800">India's $45 Trillion Heist and Recovery</h4>
                            <p class="text-xs text-slate-500">Audio Podcast</p>
                        </div>
                    </div>
                    <div class="flex items-center gap-3">
                        <a href="Econ-entrance-more-resources/Great_audio_Podcasts/India’s_$45_Trillion_Heist_and_Recovery.m4a" download class="bg-slate-100 hover:bg-slate-200 text-slate-600 p-2 rounded-lg transition" title="Download">
                            <i class="fa-solid fa-download"></i>
                        </a>
                    </div>
                </div>

                <!-- Major Economists -->
                <div class="bg-white p-4 rounded-xl shadow-md flex items-center justify-between hover:shadow-lg transition">
                    <div class="flex items-center gap-4">
                        <div class="bg-indigo-100 text-indigo-600 p-3 rounded-full">
                            <i class="fa-solid fa-podcast text-xl"></i>
                        </div>
                        <div>
                            <h4 class="font-bold text-slate-800">Major Economists and their Economic Theories</h4>
                            <p class="text-xs text-slate-500">Audio Podcast</p>
                        </div>
                    </div>
                    <div class="flex items-center gap-3">
                        <a href="Econ-entrance-more-resources/Great_audio_Podcasts/Major_Economists_and_their_Economic_Theories.m4a" download class="bg-slate-100 hover:bg-slate-200 text-slate-600 p-2 rounded-lg transition" title="Download">
                            <i class="fa-solid fa-download"></i>
                        </a>
                    </div>
                </div>

                <!-- (More) Books and Authors -->
                <div class="bg-white p-4 rounded-xl shadow-md flex items-center justify-between hover:shadow-lg transition">
                    <div class="flex items-center gap-4">
                        <div class="bg-indigo-100 text-indigo-600 p-3 rounded-full">
                            <i class="fa-solid fa-podcast text-xl"></i>
                        </div>
                        <div>
                            <h4 class="font-bold text-slate-800">(More) Books and Authors</h4>
                            <p class="text-xs text-slate-500">Audio Podcast</p>
                        </div>
                    </div>
                    <div class="flex items-center gap-3">
                        <a href="Econ-entrance-more-resources/Great_audio_Podcasts/(More)Books_and_authors.m4a" download class="bg-slate-100 hover:bg-slate-200 text-slate-600 p-2 rounded-lg transition" title="Download">
                            <i class="fa-solid fa-download"></i>
                        </a>
                    </div>
                </div>
            </div>
        </section>
```

### Task 3: Remove Sticky Audio Player

**Files:**
- Modify: `site_build/history-and-tools.html`

- [ ] **Step 1: Delete Audio Player HTML and Script**
Remove the entire `<!-- Sticky Audio Player -->` block and the `<!-- Audio Player Logic -->` script block.

### Task 4: Verification

- [ ] **Step 1: Verify Links and Layout**
Check that all new links point to the correct files and the layout is consistent.

Run: `ls site_build/history-and-tools.html` (Verify file exists and can be opened in browser if possible, but for CLI we just check the content).
Verify by reading the file and checking the injected HTML.
