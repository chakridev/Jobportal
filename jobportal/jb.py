# jp.py
 
import requests
from bs4 import BeautifulSoup
 
#job = input('Enter job Tilte:')
#location = input('Enter Location:')
 
#print(job)
 
 
 
#url = 'https://www.indeed.co.in/jobs?q=python+developer&amp;l=Bengaluru&amp;sort=date'
 
#url ='https://www.indeed.co.in/jobs?q='+job+'&amp;l='+location+'&amp;sort=date'
 
 
 
titles  =[]
links = []
companies = []
summaries  = []
 
dates =[]
 
 
def job_data(url,items):
 
    res = requests.get(url).content
    soup = BeautifulSoup(res,'html.parser')
    data = soup.find_all('div',class_='jobsearch-SerpJobCard')
 
    for i in data:
 
        title = i.find('h2',class_='title')
 
        if items[0] in title.text:
            company = i.find('span',class_='company')
            link = title.find('a')
            summary  =i.find('div',class_='summary')
 
            date = i.find('span',class_='date')
 
            titles.append(title.text.strip())
            links.append('https://www.indeed.co.in'+link['href'])
            companies.append(company.text.strip())
            dates.append(date.text.strip())
            summaries.append(summary.text.strip())
 
            # print('\nJob Title:',title.text)
            # #print('posted:',date.text)
            # print('Company Name:',company.text)
            # print('Job Summary:',summary.text)
            # print('posted:',date.text)
            # print('https://www.indeed.co.in'+link['href'])
            # print(10*'*****')
 
    return titles,companies,summaries,dates,links
 
#job_data(url)