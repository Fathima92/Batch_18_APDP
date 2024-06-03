# Adaptee
class Mp3Player:
    def play_mp3(self, filename):
        print(f"Playing MP3 file: {filename}")

class Mp4Player:
    def play_mp4(self, filename):
        print(f"Playing MP4 file: {filename}")

class VlcPlayer:
    def play_vlc(self, filename):
        print(f"Playing VLC file: {filename}")
    
#Target
class MediaPlayer:
    def play(self, audio_type, filename):
        raise NotImplementedError("This method should be overridden.")

# Adapter
class MediaAdapter(MediaPlayer):
    def __init__(self, audio_type):
        if audio_type == "mp4":
            self.advanced_player = Mp4Player()
        elif audio_type == "vlc":
            self.advanced_player = VlcPlayer()
    
    def play(self, audio_type, filename):
        if audio_type == "mp4":
            self.advanced_player.play_mp4(filename)
        elif audio_type == "vlc":
            self.advanced_player.play_vlc(filename)


#Client Code 
class AudioPlayer(MediaPlayer):
    def play(self, audio_type, filename):
        if audio_type == "mp3":
            mp3_player = Mp3Player()
            mp3_player.play_mp3(filename)
        elif audio_type in ["mp4", "vlc"]:
            adapter = MediaAdapter(audio_type)
            adapter.play(audio_type, filename)
        else:
            print(f"Invalid media. {audio_type} format not supported")

# Using the Adapter
audio_player = AudioPlayer()
audio_player.play("mp3", "song.mp3")
audio_player.play("mp4", "video.mp4")
audio_player.play("vlc", "movie.vlc")
audio_player.play("avi", "my_movie.avi")
