from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
import moviepy.config as mpy_config
import pysrt
mpy_config.change_settings({
    "IMAGEMAGICK_BINARY": "C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"
})

""" clip1 = ImageClip("./src/3.webp").set_duration(2)
clip2 = ImageClip("./src/4.webp").set_duration(2) """
clip3 = VideoFileClip("./data/vid/1.mp4")
clip4 = VideoFileClip("./data/vid/2.mp4")
clip5 = VideoFileClip("./data/vid/3.mp4")

audio = AudioFileClip("./data/audio/1.mp3")


finalvideo = concatenate_videoclips([clip3, clip4, clip5])
finalvideo = finalvideo.loop(duration=audio.duration) #condicional para ver quien es mas largo
finalvideo.audio = CompositeAudioClip([audio])

subs = pysrt.open("./data/subtitles/1.srt", encoding='utf-8')

# Convertir los subtítulos a formato MoviePy (start_time, end_time, text)
subtitles_data = [
    ((sub.start.ordinal / 1000, sub.end.ordinal / 1000), sub.text) for sub in subs
]

bloque_ancho = finalvideo.w
bloque_alto = 220  # altura estándar para todos los subtítulos
bloque_y = finalvideo.h - 300  # distancia desde arriba (ajústalo si quieres más arriba/abajo)

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
            size=(finalvideo.w * 0.9, bloque_alto)
        ).set_position("center")
    ])
)

finalvideo = CompositeVideoClip([
    finalvideo,
    subtitles.set_position(("center", bloque_y))
])

finalvideo.write_videofile("asda.mp4", fps=24)

