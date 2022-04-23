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
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page*LIMIT}")

        if result.status_code == 200:
            print("TEST 1 IS PASSED!")
        else:
            print("TEST 1 IS NOT PASSED!")
