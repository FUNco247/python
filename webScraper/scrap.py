import urllib
import requests
from bs4 import BeautifulSoup
from save import save_to_csv

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

def get_all_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        html = requests.get(f"{indeed_URL}&start={page*limit}").text
        soup = BeautifulSoup(html, "html.parser")
        tds = soup.find_all("td",attrs={"class":"resultContent"})
        for td in tds:
            anchor = td.find("a") 
            title = anchor.text
            link = f'https://www.indeed.com/viewjob?{anchor.get("href").split("?")[1]}'
            company = td.find("span",attrs={"class":"companyName"}).text
            jobs.append({"company":company, "title" : title, "link" : link})
    return jobs

jobs = get_all_indeed_jobs(get_indeed_pages(indeed_URL))

save_to_csv(jobs)