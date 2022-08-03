from googlesearch import search
from pytube import YouTube


#NEed to increase audio quality and convert to audio only file


song = input()
str.capitalize(song)
Quarry = song + ' song'
print(Quarry)
songList = []
songListCorrect = []

for j in search(Quarry, tld="co.in", num=10, stop=10, pause=2):
    if 'youtube' in j:
        songList.append(j)

for i in songList:
    yt = YouTube(i)
    desc = yt.description
    if 'by YouTube' in desc:
        songListCorrect.append(i)

link = songListCorrect[0]
yt = YouTube(link)

stream = yt.streams.first()

stream.download()

print('All done')