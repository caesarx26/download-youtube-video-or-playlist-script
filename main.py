from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp

# path for windows download folder
DOWNLOADS_PATH = fr"{os.environ['UserProfile']}\Downloads"


# function to download YouTube video and convert to audio if desired
# by default will download in current directory and not convert to audio
def download_youtube_video(url: str, video_output_path: str = "", convert_to_audio: bool = False):
    # seeing if the file path is valid or exists first to put the video download in
    if video_output_path != "" and not os.path.exists(video_output_path):
        raise Exception("Invalid output folder path!")

    # seeing if url for video is valid to create object
    try:
        # creating YouTube video object
        youtube_video = YouTube(url)
        print("Downloading: " + str(youtube_video.title) + "\n")
    except:
        raise Exception("Invalid video url!")

    # video url was valid need to try to download stream of the video
    try:
        print('Downloading video ...\n')
        stream = youtube_video.streams.first()
        stream.download(output_path=video_output_path)
        print('Done downloading video!\n')
    except:
        raise Exception("Error occurred while downloading video!")

    # check if we need to convert the video file to an audio file
    if convert_to_audio:
        # setting path of the video clip
        path_of_video_clip = fr"{video_output_path}\{stream.default_filename}"
        if video_output_path == '':
            path_of_video_clip = stream.default_filename

        # converting the video file to an audio file
        print("Converting video to audio ...")
        successful = convert_video_to_audio(path_of_video_clip, output_path=video_output_path, video_title=stream.title)
        if not successful:
            raise Exception("Error occurred while converting video file!")
        print('Done converting video to mp3!')

        # try to delete video file after converting to audio file
        try:
            os.remove(path_of_video_clip)
        except:
            raise Exception("Error occurred while deleting video file!")


# function to download YouTube playlist and convert each video to an audio file is so desired
# by default will download in current directory and not convert to audio
def download_youtube_playlist(url: str, video_output_path: str = "", convert_to_audio: bool = False):
    # seeing if the file path is valid or exists first to put the video download in
    if video_output_path != "" and not os.path.exists(video_output_path):
        raise Exception("Invalid output folder path!")

    # seeing if url for playlist is valid to create object
    try:
        # creating YouTube video object
        youtube_playlist = Playlist(url)
        print("Downloading: " + str(youtube_playlist.title) + "\n")
    except:
        raise Exception("Invalid playlist url!")

    # downloading all the videos in the playlist
    for youtube_video in youtube_playlist.videos:

        print("Downloading: " + str(youtube_video.title) + "\n")

        # playlist url was valid need to try to download streams of the videos
        try:
            print('Downloading video ...\n')
            stream = youtube_video.streams.first()
            stream.download(output_path=video_output_path)
            print('Done downloading video!\n')
        except:
            raise Exception("Error occurred while downloading video!")

        # check if we need to convert the video file to an audio file
        if convert_to_audio:
            # setting path of the video clip
            path_of_video_clip = fr"{video_output_path}\{stream.default_filename}"
            if video_output_path == '':
                path_of_video_clip = stream.default_filename

            # converting the video file to an audio file
            print("Converting video to audio ...")
            successful = convert_video_to_audio(path_of_video_clip, output_path=video_output_path,
                                                video_title=stream.title)
            if not successful:
                raise Exception("Error occurred while converting video file!")
            print('Done converting video to mp3!')

            # try to delete video file after converting to audio file
            try:
                os.remove(path_of_video_clip)
            except:
                raise Exception("Error occurred while deleting video file!")


# function to convert a video file to an audio file mp3
# will return true if successful otherwise false
def convert_video_to_audio(video_path, output_path='', video_title='temp'):
    try:
        clip = mp.VideoFileClip(video_path)
        # setting path of audio file
        path_of_audio_file = fr"{output_path}\{video_title}.mp3"
        if output_path == '':
            path_of_audio_file = video_title + ".mp3"
        # writing the audio file
        clip.audio.write_audiofile(path_of_audio_file)
        # wait till audio file is written then close clip and then can delete video in functions above
        clip.close()
    except:
        print("Error: could not convert video file to audio file")
        return False
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # welcome message
    print("--------------- Running Youtube video and playlist downloader script ---------------")
    # testing download YouTube video function by putting in download path
    test_url1 = 'https://www.youtube.com/watch?v=81m8_5mccgA&list=PL65E33789AA7052BC&index=9'
    test_url2 = 'https://www.youtube.com/watch?v=XzOvgu3GPwY&ab_channel=TaylorSwiftVEVO'

    # testing download YouTube video by putting in current path
    # download_youtube_video(test_url1, convert_to_audio=True)
    # # testing download YouTube video by putting in download folder
    # download_youtube_video(test_url2, video_output_path=DOWNLOADS_PATH, convert_to_audio=True)

    # testing download youtube playlist
    test_playlist_url = 'https://www.youtube.com/watch?v=EsSOv7Skl-0&list=PLEQbUq-H7Uczc3eSVDGrCnl62wzGqRzql&ab_channel=JScar'
    download_youtube_playlist(test_playlist_url, video_output_path=DOWNLOADS_PATH, convert_to_audio=True)
