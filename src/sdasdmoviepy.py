from moviepy.editor import *

clip1 = ImageClip("./src/3.webp").set_duration(2)
clip2 = ImageClip("./src/4.webp").set_duration(2)
clip3 = VideoFileClip("./data/vid/1.mp4")
clip4 = VideoFileClip("./data/vid/2.mp4")
clip5 = VideoFileClip("./data/vid/3.mp4")


final = concatenate_videoclips([clip3, clip4, clip5])
final.write_videofile("asda.mp4", fps=24)