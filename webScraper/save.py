import csv

def save_to_csv (jobs):
    file = open("jobs.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["Company", "Title", "Link"])
    for job in jobs:
        writer.writerow([job["company"], job["title"], job["link"]])
    return