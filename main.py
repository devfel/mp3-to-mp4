from moviepy.editor import *
import os

INPUT_DIR = "./input"
OUTPUT_DIR = "./output"


def mp3_to_mp4(mp3_filename, image_filename, start_time=None, end_time=None):
    mp3_filepath = os.path.join(INPUT_DIR, mp3_filename)
    image_filepath = os.path.join(INPUT_DIR, image_filename)
    output_filepath = os.path.join(OUTPUT_DIR, mp3_filename.replace(".mp3", ".mp4"))

    # Load the audio file
    audioclip = AudioFileClip(mp3_filepath)

    # If start and end times are specified, subclip the audio
    if start_time and end_time:
        audioclip = audioclip.subclip(start_time, end_time)

    # Load the image file
    imgclip = ImageClip(image_filepath)

    # Set the duration of the image to the duration of the audio
    imgclip = imgclip.set_duration(audioclip.duration)

    # Set the audio of the image clip to our audio
    videoclip = imgclip.set_audio(audioclip)

    # Set fps and resize video
    videoclip.fps = 30
    videoclip = videoclip.resize((1280, 720))

    # Export the video clip as an MP4 file
    videoclip.write_videofile(output_filepath, codec="libx264", fps=30)


# Convert all MP3 files in the INPUT_DIR to MP4 videos using a specified image.
# Parameters:
# - image_filename: The name of the image file to use as background for the videos.
def mp3_to_mp4_folder(image_filename):
    # List all files in the INPUT_DIR
    all_files = os.listdir(INPUT_DIR)

    # Filter out only the MP3 files
    mp3_files = [f for f in all_files if f.lower().endswith(".mp3")]

    # Convert each MP3 file to MP4
    for mp3_file in mp3_files:
        mp3_to_mp4(mp3_file, image_filename)


# Example usage:
# mp3_to_mp4("sample.mp3", "image-placeholder.jpg")

# mp3_to_mp4('sample.mp3', 'image.jpg', 'H:MM:SS', 'H:MM:SS')
# mp3_to_mp4('sample.mp3', 'image.jpg', '1:30:00', '1:35:00')

# to run, go to the main folder and execute: python main.py

mp3_to_mp4_folder("rper-placeholder.jpg")
