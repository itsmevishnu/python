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
    urls = [ #List of Malayalam devotional songs.
        'https://youtu.be/D3cEUoSod9k',
        'https://youtu.be/0K8gmJCj-1I',
        'https://youtu.be/IMezEbCPPSQ',
        'https://youtu.be/jt5W7RQnQDo',
        'https://youtu.be/wgJ7VI7RRHk',
        'https://youtu.be/kQeXk8jNMko',
        'https://youtu.be/an9pxTo2Gp0',
        'https://youtu.be/QmKx22P9_pg',
        'https://youtu.be/xzcH3ngHN48',
        'https://youtu.be/TkTDTeLlOXg'
        'https://youtu.be/m_dZizhORWQ',
        'https://youtu.be/0UeoMg5RSQ8',
        'https://youtu.be/iPIBP_-LViE',
        'https://youtu.be/BFH1RXvnSlg',
        'https://youtu.be/bw2-12Kxkng',
        'https://youtu.be/RsXU4k6TiFU',
        'https://youtu.be/wnmkQ5FNNbY',
        'https://youtu.be/QG9Xworv8WM',
        'https://youtu.be/pBDbc24ncOM',
        'https://youtu.be/Wu2k9gqSi3g',
        'https://youtu.be/McgEYZyJ0A4',
        'https://youtu.be/BJhueyYfXOs',
        'https://youtu.be/SFcpGNNWTrE',
        'https://youtu.be/PlF7dISAl4U',
        'https://youtu.be/tiw2Dzthdn8',
        'https://youtu.be/zYxauyaLBFA',
        'https://youtu.be/nb6iCZofGlk',
        'https://youtu.be/KfJK9Jeb45U',
        'https://youtu.be/Q9z15hIv_5w',
        'https://youtu.be/zp__gjGnA4A',
        'https://youtu.be/t-N7HQ6JEeo',
        'https://youtu.be/DP3OYrGqpU0',
        'https://youtu.be/00xHiZ7u0YU'
    ]
    for i, url in enumerate(urls):
        print(f"Start downloading({i+1}/{len(urls)})...")
        download(url)
        print(f"Downloading completed {i+1}/{len(urls)}")
