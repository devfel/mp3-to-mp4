from moviepy.editor import *
import os

INPUT_DIR = "C:\\Users\\LFVAR\\Desktop\\Coding-UF\\mp3-to-mp4\\input"
OUTPUT_DIR = "C:\\Users\\LFVAR\\Desktop\\Coding-UF\\mp3-to-mp4\\output"


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


# Example usage:
# mp3_to_mp4("sample.mp3", "image-placeholder.jpg")
# mp3_to_mp4('sample.mp3', 'image.jpg', '1:30:00', '1:35:00')
# mp3_to_mp4('sample.mp3', 'image.jpg', 'H:MM:SS', 'H:MM:SS')

mp3_to_mp4("2020-02-07-13-33-01-part2.mp3", "rper-placeholder.jpg")
