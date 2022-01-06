import os

for i in range(480,501):
# Absolute path of a file
    old_name = r"D:\Series\[AnimeRG] Naruto Shippuden (Complete Series 001-500) Naruto Shippuuden [720p] [HEVC] [x265] [Batch] [pseudo]\Season 21 (Episodes 480-500)\[SubtitleTools.com] [Crunchyroll] Naruto Shippuden - "+str(i)+".srt"
    new_name = r"D:\Series\[AnimeRG] Naruto Shippuden (Complete Series 001-500) Naruto Shippuuden [720p] [HEVC] [x265] [Batch] [pseudo]\Season 21 (Episodes 480-500)\[AnimeRG] Naruto Shippuden - "+str(i)+" [720p] [x265] [pseudo].srt"

# Renaming the file
    os.rename(old_name, new_name)



