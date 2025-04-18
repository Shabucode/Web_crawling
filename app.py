import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def crawl_site(start_url, max_pages=10):
    visited = set()
    to_visit = [start_url]

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)
        if url in visited:
            continue

        try:
            print(f"Visiting: {url}")
            response = requests.get(url)
            visited.add(url)

            soup = BeautifulSoup(response.text, 'html.parser')
            # print(soup)
            for link in soup.find_all('a', href=True):
                href = link['href']
                # Make full URL
                full_url = urljoin(url, href)
                # Check if it's the same domain
                if urlparse(full_url).netloc == urlparse(start_url).netloc:
                    if full_url not in visited and full_url not in to_visit:
                        to_visit.append(full_url)

        except Exception as e:
            print(f"Error visiting {url}: {e}")

    print("\nCrawling complete.")
    print(f"Visited {len(visited)} pages.")