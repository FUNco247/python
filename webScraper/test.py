import urllib
import requests
from bs4 import BeautifulSoup

limit = 50
indeed_URL = f"https://www.indeed.com/jobs?as_and=python&limit={limit}"
def get_indeed_pages(URL): 
    req = requests.get(URL)
    text_result = req.text
    soup = BeautifulSoup(text_result, "html.parser")
    pagination = soup.find("div", {"class":"pagination"})
    links = pagination.find_all("a")
    pages = []
    for link in links[:-1]: # [:-1] mean except lastone
        pages.append(int(link.find("span").text))
    last_page = max(pages)
    return last_page

print(get_indeed_pages(indeed_URL))