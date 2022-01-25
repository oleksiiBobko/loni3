from requests_html import HTMLSession
from bs4 import BeautifulSoup

session = HTMLSession();

response = session.get("https://github.com/oleksiiBobko?tab=repositories")

soup = BeautifulSoup(response.text, "lxml")
for url in soup.find_all(class_="wb-break-all"):
    print(url.a.text.replace("\n", " ").strip())


# import requests
# from bs4 import BeautifulSoup
#
# base_url = 'http://www.nytimes.com'
# r = requests.get(base_url)
# soup = BeautifulSoup(r.text, "lxml")
#
# for story_heading in soup.find_all(class_="story-heading"): 
#     if story_heading.a: 
#         print(story_heading.a.text.replace("\n", " ").strip())
#     else: 
#         print(story_heading.contents[0].strip())