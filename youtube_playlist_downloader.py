import os
from pytube import YouTube, Playlist
# import validators

# Download Youtube Video Function
def download_vid(url,resolution='1080p',out_path="./"):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(res=f"{resolution}").first()
        if stream:
            print(f"\nStarted Downloading.....")
            stream.download(output_path=out_path)
            print(f"Downloaded {yt.title} at {resolution} resoultion.")
        else:
            print(f"No resoultion {resolution} available for {yt.title}.")
    except Exception as e:
        print(f"An error occured: {e}")


# Download Youtube Video Playlist Function
def download_playlist(url,resolution='1080p',out_path="./"):
    try:
        yt_playlist = Playlist(url)
        for video in yt_playlist.video_urls:
            yt_p = YouTube(video)
            stream_p = yt_p.streams.filter(res=f"{resolution}").first()
            if stream_p:
                print(f"\nStarted Downloading.....")
                stream_p.download(output_path=out_path)
                print(f"Downloaded {yt_p.title} at {resolution} resoultion.")
            else:
                print(f"No resoultion {resolution} available for {yt_p.title}. Skipping")
        print(f"All videos downloaded from {yt_playlist.title} playlist.")
    except Exception as e:
        print(f"An error ocuured while downloading playlist: {e}")


# Rename mp4 to mp3 Function
def rename_mp4_to_mp3(directory):
    try:
        for filename in os.listdir(directory):
            if filename.endswith(".mp4"):
                new_filename = os.path.splitext(filename)[0] + ".mp3"
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
    except Exception as e:
        print(f"An error occured while renameing: {e}")


# Download Song Function
def download_music(url, out_path="./"):
    try: 
        yt_music = YouTube(url)
        music_stream = yt_music.streams.filter(only_audio=True).first()
        if music_stream:
            print(f"\nStarted Downloading.....")
            music_stream.download(output_path=out_path)
            print(f"Song Downloaded Successfully: {yt_music.title}.")
            
            downloaded_file_path = os.path.join(out_path, yt_music.title + ".mp4")
            if os.path.exists(downloaded_file_path):
                rename_mp4_to_mp3(out_path)
        else:
            print(f"No audio stream available for {yt_music.title}")
    except Exception as e:
        print(f"An error occured: {e}")


# Download Songs Playlist Function
def download_songs_playlist(url, out_path="./"):
    try:
        yt_music_pl = Playlist(url)
        for music in yt_music_pl:
            yt_music = YouTube(music)
            music_stream = yt_music.streams.filter(only_audio=True).first()
            if music_stream:
                print(f"\nStarted Downloading.....")
                music_stream.download(output_path=out_path)
                print(f"Song Downloaded Succesfully: {yt_music.title}.")

                downloaded_file_path = os.path.join(out_path, yt_music.title + "mp4")
                if os.path.exists(downloaded_file_path):
                    rename_mp4_to_mp3(out_path)

            else:
                print(f"No audio stream available for {yt_music.title}")
        else:
            print(f"All songs downloaded from {yt_music_pl.title} playlist.")
    except Exception as e:
        print(f"An error occured while downloading music playlist: {e}")


# Download Youtube videos and assign index 
def index_download_playlist(url, resolution='1080p', out_path="./"):
    try:
        yt_playlist = Playlist(url)
        cnt = 1
        for video_url in yt_playlist.video_urls:
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
                print(f"No resolution {resolution} available for {yt_video.title}. Skipping.")

        print(f"All videos downloaded from the playlist.")
    except Exception as e:
        print(f"An error occured: {e}")

# Expection Handling
# def url_check(vid_url):
#     if not validators.url(vid_url):
#         raise ValueError(f"Invalid URL. Please enter a valid URL.")

def res_validation(res):
    valid_res = ["1080p60","1080p", "720p", "480p", "360p", "240p", "144p"]
    if res not in valid_res:
        raise ValueError(f"Invalid Resoultion. Please enter a valid Resoultion.")

def path_validation(path):
    if not os.path.isdir(path):
        raise ValueError(f"Invalid Path. Please enter a valif Path.")
    

def main():
    while(True):
        print(f"\n-----------YB-Youtube-Video-Downloader-----------")
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
                try:
                    vid_url = input("Enter video URL to download: ")
                    # url_check(vid_url)
                    res = input("Enter Resolution (1080p,720p...): ")
                    res_validation(res)
                    path = input("Enter the desired path to save the video: ").strip() or './'
                    path_validation(path)
                    download_vid(vid_url,res,path)
                except ValueError as ve:
                    print(ve)
                except Exception as e:
                    print(f"\nAn error occured: {e}\nPlease check entered details.")
            case 2:
                try:
                    pl_url = input("Enter Video Playlist URL to be downloaded: ")
                    
                    res = input("Enter Resoultion (1080p,720p...): ")
                    res_validation(res)
                    path = input("Enter the desired path to save playlist: ").strip() or './'
                    path_validation(path)
                    download_playlist(pl_url,res,path)
                except ValueError as ve:
                    print(ve)
                except Exception as e:
                    print(f"\nAn error occured: {e}\nPlease check entered details.")
            case 3:
                try:
                    song_url = input("Enter song URL to download: ")

                    path = input("Enter the desired path to save song: ").strip() or './'
                    path_validation(path)
                    download_music(song_url,path)
                except ValueError as ve:
                    print(ve)
                except Exception as e:
                    print(f"\nAn error occured: {e}\nPlease check entered details.")
            case 4:
                try:
                    song_pl_url = input("Enter song playlist url to download: ")
                    path = input("Enter the desired path to save songs palylist: ").strip() or './'
                    path_validation(path)
                    download_songs_playlist(song_pl_url,path)
                except ValueError as ve:
                    print(ve)
                except Exception as e:
                    print(f"\nAn error occured: {e}\nPlease check entered details.")
            case 5:
                try:
                    in_pl_url = input("Enter Video Playlist URL to be downloaded: ")
                    res = input("Enter Resoultion (1080p,720p...): ")
                    res_validation(res)
                    path = input("Enter the desired path to save playlist: ").strip() or './'
                    path_validation(path)
                    download_playlist(in_pl_url,res,path)
                except ValueError as ve:
                    print(ve)
                except Exception as e:
                    print(f"\nAn error occured: {e}\nPlease check entered details.")                
            case 6:
                break
            case _:
                print("Invalid choice please enter valid choice")



if __name__ == "__main__":
    main()

