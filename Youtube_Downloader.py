from pytube import Playlist
from pytube.helpers import safe_filename 
p = Playlist('https://youtube.com/playlist?list=PLnIP3P5w0BIEq5OaRAy5nzqOx3VkAliVT')

count = 1
error = []
for video in p.videos:
    try:
        print(f'Downloading: {count}')
        name = safe_filename(video.title)
        video.streams.filter(res="240p").first().download(output_path="C:\\Users\\26tho\\Desktop\\OC\\",filename=name[:30]+".mp4",filename_prefix=f"{count}_")
        count+=1
    except:
        error.append(name)
        print("Error Happened")
        continue
    
print(error)

