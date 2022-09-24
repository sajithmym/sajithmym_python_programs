from moviepy.editor import *
from tkinter import filedialog as Sajith
import os

print('~ '*35)
print('\t - Welcome to Dise Simulator -')
print('~ '*35,'\n')

try:
    InItial = os.getcwd()
    p=Sajith.askopenfilename(initialdir=InItial,title="Choose a MP4 video",filetypes=(("mp4 files",".mp4"),("all files","*.*")))
    IMPORT = VideoFileClip(p)

    Name = input("Enter file name to Save :- ")
    IMPORT.write_gif(f"{Name}.gif")
except Exception as x:
    print('---->',x,'<----')
else:
    print('~ '*35)
    print('\t - Welcome to Video to Gif converter -')
    print('~ '*35,'\n')

input()