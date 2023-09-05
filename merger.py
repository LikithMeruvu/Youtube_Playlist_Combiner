import os
import subprocess

# Create a list to store video file paths
video_files = []

# Loop through the downloaded videos in the 'downloads' directory
for filename in os.listdir('downloads'):
    if filename.endswith('.mp4'):
        # Get the video file path
        video_path = os.path.join('downloads', filename)
        video_files.append(video_path)

# Create a text file containing a list of input video files
with open('input.txt', 'w') as input_file:
    for video_file in video_files:
        input_file.write(f"file '{video_file}'\n")

# Concatenate the video clips using FFmpeg with progress display and ignoring warnings
output_file = 'final.mp4'

ffmpeg_command = f'ffmpeg -f concat -safe 0 -i input.txt -c:v copy -c:a copy -v warning -progress pipe:1 {output_file}'

# Execute the FFmpeg command and display the progress in the terminal
ffmpeg_process = subprocess.Popen(
    ffmpeg_command,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True,
    universal_newlines=True
)

for line in ffmpeg_process.stdout:
    if "time=" in line:
        print(line.strip())

# Wait for FFmpeg to finish
ffmpeg_process.communicate()

# Remove the temporary input file
os.remove('input.txt')

print("Merged all videos into 'final.mp4'.")
