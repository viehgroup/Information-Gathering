import bs4
import requests
import os


url = input("Enter a url(https://www.example.com): ")
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text,"html.parser")
#print(soup.prettify())

for links in soup.find_all('a'):
    link = links.get("href")
    if link[0:3] == "../" and link != "#":
        print(url+link[2:len(link)])
    elif link[0] == "/" and link != "#":
        print(url+link)