from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
import moviepy.config as mpy_config
import pysrt
mpy_config.change_settings({
    "IMAGEMAGICK_BINARY": "C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"
})

import top3 

clip1 = VideoFileClip("./data/vid/1.mp4")
clip2 = VideoFileClip("./data/vid/2.mp4")
clip3 = VideoFileClip("./data/vid/3.mp4")

audio = AudioFileClip("./data/audio/1.mp3")

subtitle_srt = pysrt.open("./data/subtitles/1.srt", encoding='utf-8')

def main_new2():

    top3.video_creator(clip1, clip2, clip3)
    top3.audio_creator(audio)
    top3.subtitles(subtitle_srt)
    top3.video_copilation.write_videofile("./videos/new2.mp4", fps=24)