from pytube import YouTube

def download(url):
  """
  Download the video url as mp4 fomrat.
  """
    video = YouTube(url)
    audio = video.streams.filter(file_extension='mp4').first()
    try:
        audio.download()
    except Exception as e:
        print(f"Download failed, Error{str(e)}")


if __name__ == '__main__':
    urls = [ #List of URLs
        
    ]
    for i, url in enumerate(urls):
        print(f"Start downloading({i+1}/{len(urls)})...")
        download(url)
        print(f"Downloading completed {i+1}/{len(urls)}")
