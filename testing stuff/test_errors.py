from pytube import YouTube
from pytube import Playlist

print("---------------------------------------------------------------------------------")
print("Downloading a video: ")
print("\n\n")
# creating YouTube object for the video of a wrong link to get an error
try:
    test_video = YouTube('aaa')
    # printing title of video
    print("title: " + test_video.title)
except:
    print('invalid video link')

print("---------------------------------------------------------------------------------")
print("Downloading playlist of videos: ")
print("\n")
# creating playlist object of an invalid playlist link to get an error need to get title
try:
    p = Playlist('hhh')
    p.title
except:
    print('invalid playlist link')

# passing single video link to get error instead
try:
    p = Playlist('https://www.youtube.com/watch?v=ULCIHP5dc44')
    print(p.title)
except:
    print('invalid playlist link')


