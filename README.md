# Face Recognition Game using OpenCV

This program utilizes OpenCV's DNN (Deep Neural Network) module in Python to track faces. 
The coordinates of the detected face are then sent to the game, allowing the player character to move accordingly.

## Description

The project combines face detection using the DNN support provided by the `cv2` module in Python and integrates it with a game. It tracks the face in real-time and translates its coordinates into game movements, creating an interactive experience.

## Project Components

- **Model Architecture**: The `deploy.prototxt.txt` file contains the architecture of the model used for face detection.
- **Model Weights**: The `weights.caffemodel` file holds the weights for the actual model layers.
- **Required Modules**:
  - OpenCV(cv2) for Python
  - NumPy
  - Pygame
  - Imutils

## Repository Structure

- `src/`: Contains the source code files (`main.py`, `face.py`, `game.py`).
- `model/`: Includes files that contain model architecture, weights etc.
- `assets/`: Contains PNG and related assets used by the game.
- `game.sh`: Shell Script to run code using Command Line.

## Usage

To run the code, execute the `game.sh` file, or use the following command to run the `main.py`:

```bash
python ".\src\main.py"
