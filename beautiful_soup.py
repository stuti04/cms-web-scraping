# Loading necessary libraries
from bs4 import BeautifulSoup
import requests
import csv

# Get HTML source code for the website
source = requests.get('https://coreyms.com/').text

# Creating a BeautifulSoup object for parsing the HTML site.
soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_data.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Summary', 'Video'])

# Getting article where all the information for the first video is stored.
for article in soup.find_all('article'):

    try:
        title = article.h2.a.text
        print(title)

        summary = article.find('div', class_='entry-content').p.text
        print(summary)

        link = article.find('iframe', class_='youtube-player')['src']

        link_id = link.split('/')[4]
        link_id = link_id.split('?')[0]

        vid_link = f'https://youtube.com/watch?v={link_id}'
        print(vid_link)

        print()
        csv_writer.writerow([title, summary, vid_link])

    except Exception:
        pass
        print()






