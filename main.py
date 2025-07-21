from bs4 import BeautifulSoup

with open('index.html','r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content,'lxml')
    # tag = soup.find('h2')#searches for the first element alone
    # subtitles = soup.find_all('h2')#searches for the all
    # print(subtitles)
    
    # for s_title in subtitles:
    #     print(s_title.text)
    course_cards = soup.find_all('div',class_='module')
    for h3 in course_cards:
        print(h3.h3.text)