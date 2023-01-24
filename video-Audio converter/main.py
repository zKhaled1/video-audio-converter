import moviepy.editor as mp 
from tkinter.filedialog import *

vid = askopenfilename()
video = mp.VideoFileClip(vid)

aud = video.audio 
aud.write_audiofile("Sample.mp3")
print("Completed!")