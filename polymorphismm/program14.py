# Q14. Create Media with play().
# Derive Audio, Video, and Podcast.
# Override play() according to media type.

class Media:
    def play(self):
        pass


class Audio(Media):
    def play(self):
        print("Playing Audio")


class Video(Media):
    def play(self):
        print("Playing Video")


class Podcast(Media):
    def play(self):
        print("Playing Podcast")


media_list = [Audio(), Video(), Podcast()]

for media in media_list:
    media.play()