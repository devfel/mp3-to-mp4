<p align="center">
  <a href="https://devfel.com/" rel="noopener">
 <img  src="https://devfel.com/imgs/devfel-logo-01.JPG" alt="DevFel"></a>
</p>

# 🎵 MP3 to MP4 Converter 🎬

Convert your favorite MP3 files into MP4 videos with static images, perfect for uploading to platforms like YouTube.

## 🌟 Features

- Convert any MP3 file into an MP4 video.
- Add a static image to your audio, ideal for music uploads on video platforms.
- (Optional) Specify a start and end time to convert only a segment of your audio.

## ⚙️ Installation and Setup

1. **Clone the Repository**:
   Begin by cloning the repository to your local machine:

   ```bash
   git clone https://github.com/devfel/mp3-to-mp4.git
   ```

2. **Navigate to the Directory**:

   ```bash
   cd mp3-to-mp4
   ```

3. **Install the Required Libraries**:
   Ensure you have the required libraries installed:
   ```bash
   pip install moviepy pillow
   ```

## 🚀 Getting Started

1. Place your MP3 files and the desired image inside the `input` directory.
2. Run `main.py` to initiate the conversion.
3. Collect the converted MP4 files from the `output` directory.

## 📖 Usage Examples

- **Basic Conversion**:
  Convert an entire MP3 file with a static image:

  ```python
  mp3_to_mp4("sample.mp3", "background-image.jpg")
  ```

- **Segmented Conversion**:
  Convert a specific segment of the MP3 file:

  ```python
  mp3_to_mp4("sample.mp3", "background-image.jpg", "1:30:00", "1:35:00")
  mp3_to_mp4("sample.mp3", "background-image.jpg", "H:MM:SS", "H:MM:SS")
  ```

- **Entire Folder Conversion**:
  To convert all MP3 files present in the `input` directory at once using a single background image, you can use the `mp3_to_mp4_folder` function:

  Simply call the `mp3_to_mp4_folder` function with the desired background image:

  ```python
  mp3_to_mp4_folder("background-image.jpg")
  ```

  This will convert all MP3 files in the `input` directory using the specified image as the background, and save the resulting MP4 files in the `output` directory.

## 🔥 Execution

To run the program, navigate to the project's main directory and execute:

```bash
python main.py
```

## 🔧 Requirements

- Python 3.x
- `moviepy` library
- Pillow (PIL)
- (Optional) ImageMagick for advanced image processing.

## 📂 Directory Structure

- `input/`: Place your MP3 and image files here.
- `output/`: Find your converted MP4 files here.
- `main.py`: Main script to run the conversion.

## 🙌 Contribution

Feel free to fork the project, open issues, and provide pull requests.

## 📜 License

This project is licensed under the MIT License.
