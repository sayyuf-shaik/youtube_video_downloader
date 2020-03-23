import pytube

link ='https://youtu.be/SsRXJnzas2s'
yt = pytube.YouTube(link)
stream = yt.streams.all()
for i in stream:
    print(i)
for i in pytube.request.get(url=link, streaming=True):
    print(i)
finished = stream[0].download()
print(finished)
print('Download is complete')

