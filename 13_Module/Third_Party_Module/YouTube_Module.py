from pytube import YouTube

def download_video(url, path="https://www.youtube.com/watch?v=iraezTzB938"):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()

        # Download the video to the specified path
        stream.download(output_path=path)

        print(f"Downloaded: {yt.title}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_path = input("Enter the download path (leave empty for current directory): ") or "."

    download_video(video_url, download_path)