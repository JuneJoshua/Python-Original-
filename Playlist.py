def song_playlist(songs, max_size):
    playlist = []
    cargoHold = 0
    if songs[0][2] > max_size:
        return playlist
    playlist.append(songs[0][0])
    cargoHold += songs[0][2]
    del songs[0]
     
    while len(songs) > 0:
        shortS = min(songs, key = lambda t: t[2])
        shortL = shortS[2]
        shortNobody = shortS[0]
         
        if cargoHold + shortL <= max_size:
            playlist.append(shortNobody)
            cargoHold += shortL
        songs.remove(shortS)
    return playlist
    
playlist = ([("Nobody", 3.32, 5.1), ("I don't know", 3.42, 5.3), ("Prince", 3.49, 5.4), ("Time Lapse", 4.15, 6.1)])
playlist_1 = ([("Shampoo", 4.35, 6.5), ("All Mine", 3.24, 5.0), ("Rey's Theme", 3.11, 4.9), ("The Imperial March", 3.04, 4.1), ("Cover Up", 3.25, 4.9)])
max_size = 30
songs = playlist + playlist_1
play = song_playlist(songs, max_size)
print(play)
