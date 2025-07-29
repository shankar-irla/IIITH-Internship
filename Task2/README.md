# Task-2: Image and Video Segmentation using YOLOv8

## 1. Prepare Image Dataset
- Collect all input images required for segmentation.
- Place them in a dedicated folder (e.g., `input_images/`) to maintain organization.

## 2. Apply YOLOv8 Segmentation to Images
- Load the YOLOv8 segmentation model:
  ```python
  from ultralytics import YOLO

  model = YOLO('yolov8n-seg.pt')  # YOLOv8 nano segmentation model
  results = model.predict(source='input_images/', save=True, project='segmentation_results', name='images')
  ```
- The segmented output images will be saved in:
  ```
  segmentation_results/images/
  ```

## 3. Convert Segmented Images to Video
- Use **FFmpeg** to compile the segmented images into a video:
  ```bash
  ffmpeg -framerate 30 -i segmentation_results/images/frame_%04d.jpg -c:v libx264 -pix_fmt yuv420p output_video.mp4
  ```
- Here, `-framerate 30` sets the frame rate, and `frame_%04d.jpg` refers to the image naming format.

## 4. Download and Extract Video Frames
- Download a short video clip (e.g., `input_video.mp4`).
- Extract frames from the video using FFmpeg:
  ```bash
  ffmpeg -i input_video.mp4 frames/frame_%04d.jpg
  ```
- The extracted frames will be stored in a folder like `frames/`.

## 5. Segment Extracted Video Frames
- Run YOLOv8 segmentation on each extracted frame:
  ```python
  model = YOLO('yolov8n-seg.pt')
  results = model.predict(source='frames/', save=True, project='segmentation_results', name='video_frames')
  ```
- The segmented frames will be saved in:
  ```
  segmentation_results/video_frames/
  ```

## 6. Reconstruct Final Segmented Video
- Combine all segmented frames into a final output video:
  ```bash
  ffmpeg -framerate 30 -i segmentation_results/video_frames/frame_%04d.jpg -c:v libx264 -pix_fmt yuv420p final_segmented_video.mp4
  ```
- This will create a smooth segmented video from the processed frames.

