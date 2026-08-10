import os

notes_dir = "notes"

pdf_links = {
    "Quick revision sequence and series.pdf": "https://drive.google.com/file/d/1tsvYgy-pwQ6ddH75wWRrxx4MYENK_kPm/view",
    "redo macroeconomics pt1_20260713_cleaned.pdf": "https://drive.google.com/file/d/16Kzj-OW3zMM_3YfHG8_dbOfDwYgTFaPy/view",
    "Single variable calc.pdf": "https://drive.google.com/file/d/1UY4fbRV4nrUBF7Ixk2YjS0RbFosQEpPc/view",
    "redo Matrices_20260713_cleaned.pdf": "https://drive.google.com/file/d/1FFyyDXA7sXA6mlHL3Nqxv6mQHIsp8Mz6/view",
    "mathematical logic_20260713_cleaned.pdf": "https://drive.google.com/file/d/1kCoIxt1OfjyETv0ioXosX7nDwyr35sW4/view",
    "redo macroeconomics pt2_20260713_cleaned.pdf": "https://drive.google.com/file/d/1Ap4yBAlIIlCm3Lb4HaMsx5HskmLyH_nf/view",
    "welfare theory + game theory + market dynamics (all Competition) + public goods_20260712_cleaned.pdf": "https://drive.google.com/file/d/1Y0CDILuT5X5oB5KldV08kHpXHw5An3vc/view",
    "consumer theory_20260712_cleaned.pdf": "https://drive.google.com/file/d/1k6d4ZXxSDorfracnbyiGzrTVpjJZbcJA/view",
    "function miscellaneous set theory question.pdf": "https://drive.google.com/file/d/1VuHvru-Iv2oyEUeeAgelV6p8-lHHMkry/view",
    "continuity and differentiability_20260711.pdf": "https://drive.google.com/file/d/1heM0oQbGBSNGfWdcNPssBmuUkY9wAQE5/view",
    "handwritten MIT probability notes_20260711_cleaned.pdf": "https://drive.google.com/file/d/19GI6qK6n8km8GJGwCVC-E5Fc7ame_lWD/view",
    "handwritten math Ecopoint notes_20260711_cleaned.pdf": "https://drive.google.com/file/d/1OAjb0bNhXija-lEvAhCAqybzlMJ75gUC/view",
    "seq and series_20260711_cleaned.pdf": "https://drive.google.com/file/d/1GzXGSh1LMtJkPeZBzGF7jcjA71-NXUFb/view",
    "ISI previous 10 year doubts_20260711_cleaned.pdf": "https://drive.google.com/file/d/1KKyidM9EtIY35odPG4T_qc1dNe8eH9kc/view",
    "optimisation_20260711_cleaned.pdf": "https://drive.google.com/file/d/1_34_7DlCUhyjcSI2CXZS1GDxBExD2muX/view"
}

categories = {
    "Mathematics & Statistics": [],
    "Microeconomics": [],
    "Macroeconomics": [],
    "Past Year Questions & Doubts": []
}

for f in sorted(pdf_links.keys()):
    lower_f = f.lower()
    if 'isi' in lower_f or 'doubt' in lower_f:
        categories["Past Year Questions & Doubts"].append(f)
    elif 'macro' in lower_f:
        categories["Macroeconomics"].append(f)
    elif 'consumer theory' in lower_f or 'welfare theory' in lower_f or 'game theory' in lower_f or 'micro' in lower_f:
        categories["Microeconomics"].append(f)
    else:
        categories["Mathematics & Statistics"].append(f)

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Notes</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body class="bg-slate-50 font-sans text-slate-800">
    <!-- Top Navigation -->
    <nav class="sticky top-0 bg-white/90 backdrop-blur-md border-b border-slate-200 z-40">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16">
                <div class="flex">
                    <div class="flex-shrink-0 flex items-center">
                        <a href="../index.html" class="font-bold text-xl text-indigo-600">Econ Entrance Hub</a>
                    </div>
                </div>
                <div class="hidden sm:ml-6 sm:flex sm:space-x-8 items-center">
                    <a href="index.html" class="text-sm font-medium text-indigo-600 border-b-2 border-indigo-600 h-full flex items-center">My Notes</a>
                    <a href="../indian-economy.html" class="text-sm font-medium text-slate-500 hover:text-slate-900">Indian Economy</a>
                    <a href="../macroeconomics.html" class="text-sm font-medium text-slate-500 hover:text-slate-900">Macro</a>
                    <a href="../microeconomics.html" class="text-sm font-medium text-slate-500 hover:text-slate-900">Micro</a>
                    <a href="../math-and-optimization.html" class="text-sm font-medium text-slate-500 hover:text-slate-900">Math</a>
                    <a href="../history-and-tools.html" class="text-sm font-medium text-slate-500 hover:text-slate-900">History & Tools</a>
                </div>
            </div>
        </div>
    </nav>
    <main class="max-w-7xl mx-auto px-4 py-12">
        <h1 class="text-3xl font-bold text-slate-900 mb-2 flex items-center gap-3">
            <i class="fa-solid fa-book-open text-indigo-500"></i> My Notes
        </h1>
        <p class="text-slate-600 mb-8">Downloadable categorized PDF notes from my prep.</p>
"""

for cat_name, cat_files in categories.items():
    if not cat_files:
        continue
    
    html_content += f"""
        <h2 class="text-2xl font-semibold text-slate-800 mb-4 mt-8 border-b border-slate-200 pb-2">{cat_name}</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
"""
    for f in cat_files:
        link = pdf_links[f]
        display_name = f.replace('_cleaned.pdf', '').replace('.pdf', '').replace('_20260711', '').replace('_20260712', '').replace('_20260713', '').replace('_', ' ').title()
        
        if f == "redo macroeconomics pt1_20260713_cleaned.pdf":
            display_name = "Macroeconomics Pt 1 (Till Growth Models)"
        elif f == "redo macroeconomics pt2_20260713_cleaned.pdf":
            display_name = "Macroeconomics Pt 2 (Open Macro)"
        
        html_content += f"""            <a href="{link}" target="_blank" class="group block p-4 bg-white hover:bg-indigo-50 rounded-lg border border-slate-200 shadow-sm transition-colors flex items-start gap-4">
                <div class="w-10 h-10 bg-indigo-100 rounded-full flex items-center justify-center text-indigo-600 shrink-0 group-hover:bg-indigo-600 group-hover:text-white transition-colors">
                    <i class="fa-solid fa-file-pdf"></i>
                </div>
                <div class="overflow-hidden">
                    <h4 class="font-bold text-slate-800 truncate" title="{f}">{display_name}</h4>
                    <p class="text-xs text-slate-500 mt-1">View on Google Drive</p>
                </div>
            </a>
"""
    html_content += """        </div>\n"""

html_content += """    </main>
</body>
</html>
"""

with open(os.path.join(notes_dir, 'index.html'), 'w') as f:
    f.write(html_content)
print("notes/index.html generated with Google Drive links!")
