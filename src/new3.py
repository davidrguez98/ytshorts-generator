from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
import moviepy.config as mpy_config
import pysrt
mpy_config.change_settings({
    "IMAGEMAGICK_BINARY": "C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"
})

import new1

clip1 = VideoFileClip("./data/vid/3-1.mp4")
clip2 = VideoFileClip("./data/vid/3-2.mp4")

audio = AudioFileClip("./data/audio/3.mp3")

subtitle_srt = pysrt.open("./data/subtitles/3.srt", encoding='utf-8')

def main_new3():

    new1.video_creator_new()
    new1.audio_creator_new(audio)
    new1.subtitles_new(subtitle_srt)
    new1.video_copilation.write_videofile("./videos/new3.mp4", fps=24)