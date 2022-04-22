import requests

indeed_url = 'https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=100&l&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=6a7446eb57ad8e77'

indeed_result = requests.get(indeed_url)

print(indeed_result.text)
