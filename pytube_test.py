from pytube import YouTube

url = "https://www.youtube.com/watch?v=moyV8-g-SwM&ab_channel=%E9%9B%99%E4%B8%8B%E5%B7%B4IndieMusic"
# YouTube(url).streams.first().download()
yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
print(yt.streams)

