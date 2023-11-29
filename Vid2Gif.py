from moviepy.editor import VideoFileClip

videoClip = VideoFileClip('kiss_kiss.mp4')

videoClip.write_gif('kiss_kiss.gif')

print("GIF done successfully!")