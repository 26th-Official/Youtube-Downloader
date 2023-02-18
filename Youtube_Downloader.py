from pytube import Playlist
from pytube.helpers import safe_filename 
p = Playlist('https://youtube.com/playlist?list=PLbjn7kaP877u1sX4zl081V8jUeSHDY18G')

count = 1
error = []
for video in p.videos:
    try:
        print(f'Downloading: {count}')
        name = safe_filename(video.title)
        video.streams.filter(progressive=True, file_extension='mp4', res="720p").first().download(output_path=r"D:\Tutorial\Blender Drivers",filename=name[:30]+".mp4",filename_prefix=f"{count}_")
        count+=1
    except:
        error.append(name)
        print("Error Happened")
        continue
    
print(error)

