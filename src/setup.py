# File creates the FILEPATHS for PNGS ASSETS, MODEL FILES ETC

import os

def find_absolute_paths():
    try:
        # Find absolute paths for the three files
        MODEL_path = os.path.abspath('model\\deploy.prototxt.txt')
        WEIGHTS_path = os.path.abspath('model\\res10_300x300_ssd_iter_140000.caffemodel')
        PNG_path = os.path.abspath('assets\\player.png')

        # Store the absolute paths as raw string variables
        MODEL_absolute = rf'{MODEL_path}'
        WEIGHTS_absolute = rf'{WEIGHTS_path}'
        PNG_absolute = rf'{PNG_path}'

        return MODEL_absolute, WEIGHTS_absolute, PNG_absolute

    except Exception as e:
        print(f"Error occurred: {e}")
        return None

