# GPT Assisted

import requests
from bs4 import BeautifulSoup



def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citation_needed_links = soup.find_all('a', href="/wiki/Wikipedia:Citation_needed")
    return len(citation_needed_links)

def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citation_needed_links = soup.find_all('a', href="/wiki/Wikipedia:Citation_needed")

    report = ""
    for link in citation_needed_links:
        parent_paragraph = link.find_parent('p')
        if parent_paragraph:
            report += parent_paragraph.get_text() + "\n---\n"

    return report.strip()


url = "https://en.wikipedia.org/wiki/Lands_of_the_Crown_of_Saint_Stephen"

print(get_citations_needed_count(url))
print(get_citations_needed_report(url))