import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Set your target directory
DOWNLOAD_DIR = r"D:\Desktop\Economic_Surveys"

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

BASE_URL = "https://www.indiabudget.gov.in/budget2023-24/economicsurvey/allpes.php"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def download_file(url, folder_path, filename):
    try:
        response = requests.get(url, headers=HEADERS, stream=True)
        response.raise_for_status()
        file_path = os.path.join(folder_path, filename)
        
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Successfully downloaded: {filename}")
    except Exception as e:
        print(f"Failed to download {url}. Error: {e}")

def main():
    print(f"Fetching links from {BASE_URL}...")
    try:
        response = requests.get(BASE_URL, headers=HEADERS)
        response.raise_for_status()
    except Exception as e:
        print(f"Could not reach the main website. Error: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    
    for link in links:
        href = link.get('href')
        year_text = link.text.strip()
        
        if href and ("budget" in href.lower() or "economicsurvey" in href.lower()):
            year_page_url = urljoin(BASE_URL, href)
            print(f"\nChecking {year_text} page: {year_page_url}")
            
            try:
                year_response = requests.get(year_page_url, headers=HEADERS)
                year_response.raise_for_status()
                year_soup = BeautifulSoup(year_response.text, 'html.parser')
                
                year_folder = os.path.join(DOWNLOAD_DIR, year_text)
                if not os.path.exists(year_folder):
                    os.makedirs(year_folder)
                
                pdf_links = year_soup.find_all('a', href=True)
                full_pdf_url = None
                
                for pdf_link in pdf_links:
                    pdf_href = pdf_link.get('href')
                    
                    if not pdf_href.lower().endswith('.pdf'):
                        continue
                        
                    # Extract attributes to check for "full document" clues
                    link_text = pdf_link.get_text(strip=True).lower()
                    download_attr = pdf_link.get('download', '').lower()
                    
                    # Heuristics to identify the complete survey
                    if ('complete' in link_text or 
                        'full' in link_text or 
                        'download economic survey' in link_text or 
                        'complete' in download_attr or 
                        'echapter.pdf' in pdf_href.lower()):
                        
                        full_pdf_url = urljoin(year_page_url, pdf_href)
                        break # Stop looking at other PDFs on this page once the full one is found
                
                if full_pdf_url:
                    filename = full_pdf_url.split('/')[-1]
                    print(f"Found Full PDF: {filename} - Downloading...")
                    download_file(full_pdf_url, year_folder, filename)
                else:
                    print(f"No complete PDF file identified directly on the {year_text} index page.")
                    
            except Exception as e:
                print(f"Could not process page for {year_text}. Error: {e}")

if __name__ == "__main__":
    main()