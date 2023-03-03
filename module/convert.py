import moviepy.editor  as mp

class MPEdit:
    def convert_mp4_to_mp3(self,file_path,videoMP3):
        video = mp.VideoFileClip(file_path)
        video.audio.write_audiofile(videoMP3)



