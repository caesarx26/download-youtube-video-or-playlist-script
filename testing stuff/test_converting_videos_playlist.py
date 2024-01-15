from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp

# testing downloading a video
print("---------------------------------------------------------------------------------")
print("Downloading a video: ")
print("\n\n")
# creating youtube object for the video
test_video = YouTube('https://www.youtube.com/watch?v=81m8_5mccgA&list=PL65E33789AA7052BC&index=9')
# printing title of video
print("title: " + test_video.title)

# seeing which streams of the video are mp4 by filtering the streams
print("streams: " + str(test_video.streams.filter(file_extension='mp4')))

# getting the first stream of the video that was filtered as a mp4 file
stream = test_video.streams.filter(file_extension='mp4').first()
# downloading that stream of the video
output_path_for_download = f"{os.environ['UserProfile']}\Downloads"
print(output_path_for_download)
stream.download(output_path=output_path_for_download)
print("done downloading and putting in download folder")
print("\n\n")

# converting that mp4 audio only file to a mp3 file
print('Converting to audio file')
print(stream.default_filename)
path_of_video_clip = f"{os.environ['UserProfile']}\Downloads\{stream.default_filename}"
print(path_of_video_clip)
clip = mp.VideoFileClip(path_of_video_clip)
path_of_audio_clip = f"{os.environ['UserProfile']}\Downloads\{test_video.title}.mp3"
clip.audio.write_audiofile(path_of_audio_clip)
# wait til audio file is written then close clip and then can delete video
clip.close()
print("\n\n")

# deleting mp4 file of video that was downloaded because only needed it to convert to an audio file
print("Deleting video clip that was downloaded")
print(path_of_video_clip)
os.remove(path_of_video_clip)
print("Done deleting video clip!")
print("\n\n\n")

# testing downloading whole playlist of videos
print("---------------------------------------------------------------------------------")
print("Downloading playlist of videos: ")
print("\n")
# creating playlist object
p = Playlist('https://www.youtube.com/watch?v=n2rVnRwW0h8&list=PLD551D1F4DAA8D1FA')
# for each video in the playlist we will download them and convert them to an mp3
for video in p.videos:
    # getting the first stream of the video that is mp4
    video_stream = video.streams.filter(file_extension='mp4').first()
    # then we will download that stream and put the mp4 file in the downloads folder
    path = f"{os.environ['UserProfile']}\Downloads"
    video_stream.download(output_path=path)

    # then we convert the video file to an audio file and download the audio as a mp3
    path_of_video = f"{os.environ['UserProfile']}\Downloads\{video_stream.default_filename}"
    print(path_of_video)
    clip = mp.VideoFileClip(path_of_video)
    path_of_audio = f"{os.environ['UserProfile']}\Downloads\{video.title}.mp3"
    clip.audio.write_audiofile(path_of_audio)
    # wait tile audio file is written then close clip
    clip.close()

    # then we delete the video file because we only want the audio
    os.remove(path_of_video)
