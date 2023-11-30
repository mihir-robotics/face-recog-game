# Simple code to find absolute paths of file w.r.t working dir.
# Can be expanded to obtain game configuration as well

# Import OS for req. functions
import os

#
def find_absolute_paths():
    '''
    Find absolute paths for specific files located within sub-folders.

    This function retrieves the absolute paths for three files: 
    'deploy.prototxt.txt',
    'res10_300x300_ssd_iter_140000.caffemodel', 
    'player.png'. 
    Files are expected to be located within respective sub-folders ('models' and 'assets/images')
    relative to the current working directory.

    Returns:
        tuple: A tuple containing the absolute paths for the three specified files.
               (MODEL_absolute, WEIGHTS_absolute, PNG_absolute)

    Note:
        Ensure the files exist within their corresponding sub-folders to retrieve
        their absolute paths successfully; or make the required changes in the MODEL, WEIGHTS, PNG
        variables
    '''
    # Define the files w/ relative path:
    model = 'model\\deploy.prototxt.txt'
    weights = 'model\\res10_300x300_ssd_iter_140000.caffemodel'
    png = 'assets\\player.png'

    # Try to find paths; throw error if paths cannot be resolved
    try:
        # Find absolute paths for the three files
        MODEL_path = os.path.abspath(model)
        WEIGHTS_path = os.path.abspath(weights)
        PNG_path = os.path.abspath(png)

        # Store the absolute paths as raw string variables
        MODEL_absolute = rf'{MODEL_path}'
        WEIGHTS_absolute = rf'{WEIGHTS_path}'
        PNG_absolute = rf'{PNG_path}'

        return MODEL_absolute, WEIGHTS_absolute, PNG_absolute

    except Exception as e:
        print(f"Error occurred: {e}")
        return None

