from bs4 import BeautifulSoup
import requests
import time

print('Put some skill you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=Python%2C&cboWorkExp1=-1&txtLocation=').text
    # print(html_text[:1000])
    soup = BeautifulSoup(html_text,'lxml')
    # print(soup)
    jobs = soup.find_all('div',class_="srp-listing clearfix")
    # print(jobs)
    for index, job in enumerate (jobs):
        time_posted = job.find('span',class_='posting-time').text
        if '24h' in time_posted:    
            company_name = job.find('span',class_='srp-comp-name').text
            skills=job.find('div',class_='srp-keyskills').text.replace(' ',',')
            more_info = job.a['href']
            if unfamiliar_skill not in skills:
                with open('posts/{index}.txt','w') as f:
                    f.write(f'Company Name:{company_name.strip()}\n')
                    f.write(f'Required Skills:{skills.strip()}\n ')
                    f.write(f'More Info: {more_info}')
                print(f'file saved: {index}')

#jimshapecoding
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 2
        print(f'waiting {time_wait} minutes...')
        time.sleep(time_wait*60)


































# import requests
# from bs4 import BeautifulSoup

# url = 'https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=Python%2C&cboWorkExp1=-1&txtLocation='
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
# }
# html_text = requests.get(url, headers=headers).text
# soup = BeautifulSoup(html_text, 'html5lib')
# job = soup.find('li', class_='srp-listing clearfix')
# print(job)

# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time

# url = 'https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=Python%2C&cboWorkExp1=-1&txtLocation='
# driver = webdriver.Chrome()
# driver.get(url)
# time.sleep(2)  # Wait for JavaScript to load
# html_text = driver.page_source
# driver.quit()

# soup = BeautifulSoup(html_text, 'lxml')
# job = soup.find('li', class_='srp-listing clearfix')
# if job:
#     print(job)
# else:
#     print("No job listing found. Check class name or HTML structure.")