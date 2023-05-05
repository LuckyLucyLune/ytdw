import argparse
from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip

print (""" 

$$\     $$\ $$$$$$$$\ $$$$$$$\  $$\      $$\ 
\$$\   $$  |\__$$  __|$$  __$$\ $$ | $\  $$ |
 \$$\ $$  /    $$ |   $$ |  $$ |$$ |$$$\ $$ |
  \$$$$  /     $$ |   $$ |  $$ |$$ $$ $$\$$ |
   \$$  /      $$ |   $$ |  $$ |$$$$  _$$$$ |
    $$ |       $$ |   $$ |  $$ |$$$  / \$$$ |
    $$ |       $$ |   $$$$$$$  |$$  /   \$$ |
    \__|       \__|   \_______/ \__/     \__|
                                             
                                             
                                             

""")

# Parse command line arguments
parser = argparse.ArgumentParser(description='Download and cut a YouTube video to a specific time range.')
parser.add_argument('url', help='URL of the YouTube video')
parser.add_argument('start_time', type=int, help='Start time of the cut (in seconds)')
parser.add_argument('end_time', type=int, help='End time of the cut (in seconds)')
args = parser.parse_args()

# Download YouTube video using pytube
yt = YouTube(args.url)
video = yt.streams.get_highest_resolution()
video.download()

# Cut video using moviepy
filename = video.default_filename
clip = VideoFileClip(filename).subclip(args.start_time, args.end_time)
clip.write_videofile("cut_video.mp4")
