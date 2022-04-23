import bs4
import requests
from bs4 import BeautifulSoup

indeed_url = 'https://kr.indeed.com/jobs?q=python&limit=50&radius=100&start=50'

indeed_result = requests.get(indeed_url)
indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')
indeed_pagination_li_list = indeed_soup.find("div", { "class": "pagination" }).find("ul", { "class": "pagination-list" }).find_all("li")

links = []

for page_item in indeed_pagination_li_list:
    a_tag = page_item.find("a")

    if a_tag != -1 and a_tag != None:
        content = a_tag.string

        if content != None:
            links.append(content)

    elif a_tag == None:
        content = page_item.string
        links.append(content)

max_page = links[-1]
