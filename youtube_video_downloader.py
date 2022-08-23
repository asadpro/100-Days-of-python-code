# languages = ['Python', 'Java', 'JavaScript']
# Enumerate is built-in python method which create a numerical list
# enumerated = enumerate(languages,start=1) # Create a enumerate and start counting from 1.
# enumerate_toList = list(enumerated)
# for count, item in enumerate_toList:
#     print(count, item)


# # ⛵⛵⛵⛵⛵ Creating youtube video downloader
from pytube import YouTube

# youtube = YouTube("https://www.youtube.com/watch?v=OKuiyX5k6zg&list=WL&index=67&t=3410s&ab_channel=WsCubeTech")
youtube = YouTube("https://www.youtube.com/watch?v=VPtG296lBbk&list=WL&index=71&t=632s&ab_channel=MemoonaMuslima")
# youtube = YouTube("https://www.youtube.com/watch?v=8ext9G7xspg&t=16s&ab_channel=freeCodeCamp.org")
# print(youtube.thumbnail_url)

# print(youtube.title)
# print(youtube.thumbnail_url)
# print(youtube.age_restricted)
# print(youtube.streams)

all_streams = (
    youtube.streams.asc()
)  # Save the resolution streams in a variable in ascending order

# The below code will only store those streams which are available in both audio and video format to download.
# all_streams = youtube.streams.filter(progressive=True)

# Download by resolution.
# stream_2 = youtube.streams.get_by_resolution(resolution='720p')

enumerate_stream = enumerate(
    all_streams, start=1
)  # Create an enumerate and start from 1.
list_stream = list(enumerate_stream)  # Convert enumerate into list.

for count, item in list_stream:
    print(count, item)

download = int(input("Resolution to download Video: "))
all_streams[download].download()
print("Successfully!!!")

# 🌎🌎🌎🌎🌎 Python playlist downloader 🌎🌎🌎🌎🌎
# from pytube import Playlist

# playlist = Playlist(
#     "https://www.youtube.com/watch?v=Gj6V-xZgtlQandlist=PLRza9ng-gU7xKHgkttUffXAkvhrv_ydqf"
# )

# print(playlist.title)

# # In order to download full playlist we need to iterate through every video inside playlist and download them one by one using for loop.
# for video in playlist.videos[0:2]:
#     video.streams.first().download()

# from pytube import YouTube

# python_project = YouTube('https://www.youtube.com/watch?v=8ext9G7xspgandt=16s',on_complete_callback="Download has been completed!!!")

# stream_options = python_project.streams.get_highest_resolution()

# stream_options.download()

# x = int(input()) #1
# y = int(input()) #1
# z = int(input()) #1
# n = int(input()) #2 

# variable = [[x,y,z] for num in n for num2 in [x,y,z]]

# # Print the below string in reverse order.

# from pytube import YouTube
# youtube = YouTube(url='https://www.youtube.com/watch?v=wfN_U_-8AVk')

# enumarate_list = enumerate(youtube.streams.filter(progressive=True))
# for num , stream in enumarate_list:
#     print(num, stream)

# download = int(input('Which one you would like to download?: '))

# youtube.streams.filter(progressive=True)[download].download()

# 🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋🎋
# Using seedr api

# Import the lib
# from seedr import SeedrAPI

# # Create API client
# seedr = SeedrAPI(email="asadjani202@gmail.com", password="ak91249124")

# # Add a torrent
# output = seedr.add_torrent("https://www.1377x.to/torrent/3286747/UDEMY-CRASH-COURSE-ELECTRONICS-AND-PCB-DESIGN-FTU/#")

# print(output)



