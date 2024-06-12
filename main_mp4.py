from pytube import YouTube

video_link = input('Enter Youtube Link: ')
print('Downloading...')
yt = YouTube(video_link)
yt.streams.get_highest_resolution().download()
print("Video Downloaded Successfully")
