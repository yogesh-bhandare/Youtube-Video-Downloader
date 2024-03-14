import os
from pytube import YouTube, Playlist


# Download Youtube Video Function
def download_vid(url,resolution='1080p',out_path="./"):
    yt = YouTube(url)
    stream = yt.streams.filter(res=f"{resolution}").first()
    if stream:
        print(f"\nStarted Downloading.....")
        stream.download(output_path=out_path)
        print(f"\nDownloaded {yt.title} at {resolution} resoultion.")
    else:
        print(f"\nNo resoultion {resolution} available for {yt.title}.")



# Download Youtube Video Playlist Function
def download_playlist(url,resolution='1080p',out_path="./"):
    yt_playlist = Playlist(url)
    for video in yt_playlist.video_urls:
        yt_p = YouTube(video)
        stream_p = yt_p.streams.filter(res=f"{resolution}").first()
        if stream_p:
            print(f"\nStarted Downloading.....")
            stream_p.download(output_path=out_path)
            print(f"\nDownloaded {yt_p.title} at {resolution} resoultion.")
        else:
            print(f"\nNo resoultion {resolution} available for {yt_p.title}. Skipping")
    print(f"All videos downloaded from {yt_playlist.title} playlist.")


# Rename mp4 to mp3 Function
def rename_mp4_to_mp3(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".mp4"):
            new_filename = os.path.splitext(filename)[0] + ".mp3"
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))


# Download Song Function
def download_music(url, out_path="./"):
    yt_music = YouTube(url)
    music_stream = yt_music.streams.filter(only_audio=True).first()
    if music_stream:
        print(f"Started Downloading.....")
        music_stream.download(output_path=out_path)
        print(f"\nSong Downloaded Successfully: {yt_music.title}.")
        
        downloaded_file_path = os.path.join(out_path, yt_music.title + ".mp4")
        if os.path.exists(downloaded_file_path):
            rename_mp4_to_mp3(out_path)
    else:
        print(f"\nNo audio stream available for {yt_music.title}")


# Download Songs Playlist Function
def download_songs_playlist(url, out_path="./"):
    yt_music_pl = Playlist(url)
    for music in yt_music_pl:
        yt_music = YouTube(music)
        music_stream = yt_music.streams.filter(only_audio=True).first()
        if music_stream:
            print(f"Started Downloading.....")
            music_stream.download(output_path=out_path)
            print(f"\nSong Downloaded Succesfully: {yt_music.title}.")

            downloaded_file_path = os.path.join(out_path, yt_music.title + "mp4")
            if os.path.exists(downloaded_file_path):
                rename_mp4_to_mp3(out_path)

        else:
            print(f"\nNo audio stream available for {yt_music.title}")
    else:
        print(f"\nAll songs downloaded from {yt_music_pl.title} playlist.")


# Download Youtube videos and assign index 
def index_download_playlist(url, resolution='1080p', out_path="./"):
    yt_playlist = Playlist(url)
    cnt = 1
    for video_url in yt_playlist.video_urls[:3]:
        yt_video = YouTube(video_url)
        stream = yt_video.streams.filter(res=f"{resolution}").first()
        if stream:
            print(f"\nStarted Downloading {yt_video.title}...")

            temp_filename = f"temp_{cnt}.mp4" 
            stream.download(output_path=out_path, filename=temp_filename)

            new_filename = f"{cnt}_{yt_video.title.replace('|', '_').replace('&', '-').replace(' ', '_')}.mp4"
            os.rename(os.path.join(out_path, temp_filename), os.path.join(out_path, new_filename))

            print(f"Downloaded {yt_video.title} at {resolution} resolution.")
            cnt += 1
        else:
            print(f"\nNo resolution {resolution} available for {yt_video.title}. Skipping.")

    print(f"\nAll videos downloaded from the playlist.")


def main():
    while(True):
        print(f"\n-----------YB Youtube Video Downloader-----------")
        print(f"----------------------MENU-----------------------")
        print(f"1. Download Youtube Video.")
        print(f"2. Download Youtube Video Playlist.")
        print(f"3. Download Music.")
        print(f"4. Download Music Playlist.")
        print(f"5. Index and Download Playlist.")
        print(f"6. Exit.")
        choice = int(input("Enter your choice >> "))

        match choice:
            case 1:
                vid_url = input("Enter video URL to download: ")
                res = input("Enter Resolution (1080p,720p...): ")
                path = input("Enter the desired path to save the video: ").strip() or './'
                download_vid(vid_url,res,path)
            case 2:
                pl_url = input("Enter Video Playlist URL to be downloaded: ")
                res = input("Enter Resoultion (1080p,720p...): ")
                path = input("Enter the desired path to save playlist: ").strip() or './'
                download_playlist(pl_url,res,path)
            case 3:
                song_url = input("Enter song URL to download: ")
                path = input("Enter the desired path to save song: ").strip() or './'
                download_music(song_url,path)
            case 4:
                song_pl_url = input("Enter song playlist url to download: ")
                path = input("Enter the desired path to save songs palylist: ").strip() or './'
                download_songs_playlist(song_pl_url,path)
            case 5:
                in_pl_url = input("Enter Video Playlist URL to be downloaded: ")
                res = input("Enter Resoultion (1080p,720p...): ")
                path = input("Enter the desired path to save playlist: ").strip() or './'
                download_playlist(in_pl_url,res,path)                
            case 6:
                break
            case _:
                print("Invalid choice please enter valid choice")



if __name__ == "__main__":
    main()

