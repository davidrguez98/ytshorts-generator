from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
import moviepy.config as mpy_config
import pysrt
mpy_config.change_settings({
    "IMAGEMAGICK_BINARY": "C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"
})

clip1 = VideoFileClip("./data/vid/1-1.mp4")
clip2 = VideoFileClip("./data/vid/1-2.mp4")

audio = AudioFileClip("./data/audio/1.mp3")

subtitle_srt = pysrt.open("./data/subtitles/1.srt", encoding='utf-8')

video_copilation = None

def video_creator_new():

    global video_copilation

    video_copilation = concatenate_videoclips([clip1, clip2])

def audio_creator_new(audio):

    global video_copilation

    video_copilation = video_copilation.loop(duration=audio.duration)
    video_copilation = video_copilation.set_audio(audio)

def subtitles_new(subtitle_srt):

    global video_copilation

    subtitles_data = [
        ((sub.start.ordinal / 1000, sub.end.ordinal / 1000), sub.text) for sub in subtitle_srt
    ]

    bloque_ancho = video_copilation.w
    bloque_alto = 220  # altura estándar para todos los subtítulos
    bloque_y = video_copilation.h - 300  # distancia desde arriba (ajústalo si quieres más arriba/abajo)

    subtitles = SubtitlesClip(
        subtitles_data,
        lambda txt: CompositeVideoClip([
            # Fondo del bloque (seminegro, semitransparente)
            ColorClip(size=(bloque_ancho, bloque_alto), color=(0, 0, 0))
            .set_opacity(0)
            .set_duration(3),  # será reemplazado automáticamente por la duración del texto

            # Texto centrado en el bloque
            TextClip(
                txt,
                fontsize=40,
                font="Arial-Black",
                color="yellow",
                stroke_color="black",
                stroke_width=2,
                method="caption",
                align="center",
                size=(video_copilation.w * 0.9, bloque_alto)
            ).set_position("center")
        ])
    )

    video_copilation = CompositeVideoClip([
        video_copilation,
        subtitles.set_position(("center", bloque_y))
    ])


def main_new1():

    global video_copilation
    
    video_creator_new()
    audio_creator_new(audio)
    subtitles_new(subtitle_srt)
    video_copilation.write_videofile("./videos/new1.mp4", fps=24)
