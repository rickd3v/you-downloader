from pytube import YouTube

video_link = input('Enter Youtube Link: ')
print('Downloading...')
yt = YouTube(video_link)
yt.streams.get_audio_only().download()
print("Audio Downloaded Successfully")
