from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

print(html_text)
#
# soup = BeautifulSoup(html_text, 'lxml')
# # jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
# # print(jobs)
# job = soup.find('li', class_ = "clearfix job-bx wht-shd-bx")
# # print(job)
# # joblist-comp-name
# company_name = job.find('h3', class_ = "joblist-comp-name" ).text.replace(' ','')
# skills = job.find('span', class_="srp-skills").text.replace(' ', '')
# published_date = job.find('span', class_="sim-posted").span.text
# # print(skills)
# # print(company_name)
# # print(published_date)
#
# print(f'''
# Company Name: {company_name}
# Required Skills: {skills}
# Time: {published_date}
# ''')