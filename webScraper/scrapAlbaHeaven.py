import requests
from bs4 import BeautifulSoup
import csv


def save_to_csv(title, jobs):
    file = open(f"{title}.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["city", "company", "task",
                     "time", "pay", "regDate"])
    for job in jobs:
        writer.writerow([job["city"], job["company"], job["task"],
                        job["time"], job["pay"], job["regDate"]])
    return


mainURL = "http://www.alba.co.kr/"


def scrapURLs(mainURL):
    response_text = requests.get(mainURL).text
    soup = BeautifulSoup(response_text, "html.parser")
    superBrand = soup.find("div", {"id": "MainSuperBrand"})
    anchors = superBrand.find_all("a", {"class": "goodsBox-info"})
    result = []
    for anc in anchors:
        URL = anc["href"]
        title = anc.find("span", {"class": "title"}).text
        result.append([title, URL])
    return result


def getDetail(URLs):
    for URL in URLs:
        jobs_text = requests.get(URL[1]).text
        soup_detail = BeautifulSoup(jobs_text, "html.parser").find("tbody")
        jobsTr = soup_detail.find_all("tr", {"class": ""})
        result = []
        for tr in jobsTr:
            city = ""
            company = ""
            task = ""
            time = ""
            pay = ""
            regDate = ""
            cityTd = tr.find("td", {"class": "local"})
            if cityTd is not None:
                city = cityTd.text
            companySpan = tr.find("span", {"class": "company"})
            if companySpan is not None:
                company = companySpan.text
            taskSpan = tr.find("span", {"class": "title"})
            if taskSpan is not None:
                task = taskSpan.text
            timeSpan = tr.find("span", {"class": "time"})
            if timeSpan is not None:
                time = timeSpan.text
            payTd = tr.find("td", {"class": "pay"})
            if payTd is not None:
                pay = payTd.text
            regDateTd = tr.find("td", {"class": "regDate"})
            if regDateTd is not None:
                regDate = regDateTd.text
            result.append({"city": city, "company": company, "task": task,
                          "time": time, "pay": pay, "regDate": regDate})
        save_to_csv(URL[0], result)


detailURLs = scrapURLs(mainURL)
alba = getDetail(detailURLs)

# print(alba)

#testURL = detailURL[0]
