from indeed import extract_indeed_pages, extract_indeed_jobs

last_indeed_page = extract_indeed_pages()

print(extract_indeed_jobs(last_indeed_page))
