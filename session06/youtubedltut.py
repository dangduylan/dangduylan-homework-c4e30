from youtube_dl import YoutubeDL

# #downloadvideo
# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=WHK5p7JL7g4'])

#downloadaudio
# options = {'format': 'bestaudio/audio'}
# dl = YoutubeDL(options)
# dl.download(['https://www.youtube.com/watch?v=oKAu2taqZFk'])

#searchandthendownloadthefirstvideo
# options = {
#     'default_search': 'ytsearch',
#     'max_downloads': 1
# }
# dl = YoutubeDL(options)
# dl.download(['Đừng ai nhắc về anh ấy'])

#searchandthendownloadthefirstaudio
# options = {
#     'default_search': 'ytsearch',
#     'max_downloads': 1,
#     'format': 'bestaudio/audio'
# }
# dl = YoutubeDL(options)
# dl.download(['anh nhà ở đâu đấy'])