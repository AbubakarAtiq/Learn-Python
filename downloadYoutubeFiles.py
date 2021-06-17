from pytube import YouTube
data=str("\tVersion 0.0.1\n\tProgram made to install youtube videos from their URL, Enjoy")
print(data)
link=input("Enter URL:")
video=YouTube(link)
stream=video.streams.get_highest_resolution()
stream.download()
