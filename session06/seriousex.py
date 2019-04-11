from bs4 import BeautifulSoup
import requests

url='https://www.apple.com/itunes/charts/songs/'

response = requests.get(url)

soup = BeautifulSoup(response.content,'html.parser')
# all_songs = soup.find('section',{'class':"section chart-grid"}).find('div',{'class':"section-content"}).find('ul').find_all('li')
all_songs = soup.find('div',id = 'main').find_all('li')
songs_crawled = []

for v in all_songs:
    song = {}
    song['Name'] = v.h3.a.string
    song['Artist'] = v.h4.a.string
    songs_crawled.append(song)

import xlwt
from xlwt import Workbook
wb = Workbook()

sheet1 = wb.add_sheet('iTunes Charts')
sheet1.write(0,0,'Rank')
sheet1.write(0,1,'Name of song')
sheet1.write(0,2,'Artist')

rank = 1
for s in songs_crawled:
    sheet1.write(rank,0,rank)
    sheet1.write(rank,1,s['Name'])
    sheet1.write(rank,2,s['Artist'])
    rank += 1

wb.save('iTunes Charts')

#part2
from youtube_dl import YoutubeDL

for s in songs_crawled:
    options = {
    'default_search':'ytsearch',
    'max_downloads':1
}
    dl = YoutubeDL(options)
    dl.download([s['Artist'] +'-'+ s['Name']])