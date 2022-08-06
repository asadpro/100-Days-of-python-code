# languages = ['Python', 'Java', 'JavaScript']
# Enumerate is built-in python method which create a numerical list
# enumerated = enumerate(languages,start=1) # Create a enumerate and start counting from 1.
# enumerate_toList = list(enumerated)
# for count, item in enumerate_toList:
#     print(count, item)


# # ⛵⛵⛵⛵⛵ Creating youtube video downloader
# from pytube import YouTube

# youtube = YouTube("https://youtu.be/EAYlckSaviI")

# # print(youtube.title)
# # print(youtube.thumbnail_url)
# # print(youtube.age_restricted)
# # print(youtube.streams)

# all_streams = (
#     youtube.streams.asc()
# )  # Save the resolution streams in a variable in ascending order

# # The below code will only store those streams which are available in both audio & video format to download.
# # all_streams = youtube.streams.filter(progressive=True)

# # Download by resolution.
# # stream_2 = youtube.streams.get_by_resolution(resolution='720p')

# enumerate_stream = enumerate(
#     all_streams, start=1
# )  # Create an enumerate and start from 1.
# list_stream = list(enumerate_stream)  # Convert enumerate into list.

# for count, item in list_stream:
#     print(count, item)

# download = int(input("Resolution to download Video: "))
# all_streams[download].download()
# print("Successfully!!!")

# 🌎🌎🌎🌎🌎 Python playlist downloader 🌎🌎🌎🌎🌎
from pytube import Playlist

playlist = Playlist(
    "https://www.youtube.com/watch?v=Gj6V-xZgtlQ&list=PLRza9ng-gU7xKHgkttUffXAkvhrv_ydqf"
)

print(playlist.title)

# In order to download full playlist we need to iterate through every video inside playlist and download them one by one using for loop.
for video in playlist.videos[0:2]:
    video.streams.first().download()
