import bs4
import requests
from bs4 import BeautifulSoup

indeed_url = "https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=100&l&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=6a7446eb57ad8e77"

indeed_result = requests.get(indeed_url)
indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')
indeed_pagination = indeed_soup.find("div", { "class": "pagination" })
indeed_pagination_list = indeed_pagination.find("ul", { "class": "pagination-list" })

spans = []

for page in indeed_pagination_list:
    span = page.find("span")

    if type(span) == bs4.element.Tag:
        spans.append(page.find("span"))
