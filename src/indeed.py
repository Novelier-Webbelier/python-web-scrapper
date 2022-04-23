import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f'https://kr.indeed.com/jobs?q=python&limit=50&radius=100&start={LIMIT}'

def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination_li_list = soup.find("div", { "class": "pagination" }).find("ul", { "class": "pagination-list" }).find_all("li")

    links = []

    for page_item in pagination_li_list:
        a_tag = page_item.find("a")

        if a_tag != -1 and a_tag != None:
            content = a_tag.string

            if content != None:
                links.append(content)

        elif a_tag == None:
            content = page_item.string
            links.append(content)

    max_page = int(links[-1])

    return max_page

def extract_indeed_jobs(last_page):
    jobs = []

    for page in range(last_page):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        result_contents = soup.find_all("td", { "class": "resultContent" })

        for result_content in result_contents:
            job_obj = {}
            job = result_content.select_one("div:nth-child(1)")
            company = result_content.select_one("div:nth-child(2)")

            job_name = job.find("h2").find("span", { "class" : None }).string
            if job_name == None:
                print(result_content)

            company_name = company.find("span", { "class": "companyName" }).string
            company_location = company.find("div", { "class": "companyLocation" }).string

            job_obj["job_name"] = job_name
            job_obj["company_name"] = company_name
            job_obj["company_location"] = company_location

            jobs.append(job_obj)

    return jobs
