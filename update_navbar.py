import os

files_to_update = ['index.html']
site_build_dir = 'site_build'
if os.path.exists(site_build_dir):
    for f in os.listdir(site_build_dir):
        if f.endswith('.html'):
            files_to_update.append(os.path.join(site_build_dir, f))

for file_path in files_to_update:
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if My Notes is already in the navbar
    if '>My Notes</a>' in content and 'href="notes/"' in content:
        print(f"Skipping {file_path}, already has My Notes link.")
        continue
    
    # We want to insert the My Notes link before the Indian Economy link in the navbar
    # The Indian Economy link looks like: <a href="indian-economy.html"...>Indian Economy</a>
    # We can split on '<a href="indian-economy.html"' and insert our link before it.
    
    # BUT, we only want to do this in the navbar section. To be safe, let's just find the first occurrence 
    # of '<a href="indian-economy.html"' which is typically the navbar. 
    # Or, replace all occurrences that match the navbar structure?
    # Actually, in the HTML, there are links to indian-economy.html in the navbar and in the categories section.
    # Navbar link usually has 'text-sm font-medium'
    
    search_str = '<a href="indian-economy.html" class="text-sm font-medium'
    
    if search_str in content:
        my_notes_link = '<a href="notes/" class="text-sm font-medium text-slate-500 hover:text-slate-900">My Notes</a>\n                    '
        content = content.replace(search_str, my_notes_link + search_str, 1) # Replace only the first occurrence (navbar)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path}")
    else:
        print(f"Could not find navbar link in {file_path}")
