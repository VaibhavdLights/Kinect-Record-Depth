import ctypes
import _ctypes
import numpy as np
import cv2

# Import the necessary modules from pykinect2
from pykinect2 import PyKinectRuntime

# Initialize the Kinect runtime
kinect = PyKinectRuntime.PyKinectRuntime(PyKinectRuntime.FrameSourceTypes_Depth)

# Define the dimensions of the depth frame
depth_width, depth_height = kinect.depth_frame_desc.Width, kinect.depth_frame_desc.Height

# Define the output file path
output_file = "depth_data.bin"

try:
    # Open the output file in binary mode for writing
    with open(output_file, "wb") as f:
        # Main loop to capture and save depth data
        while True:
            # Get the latest depth frame from the Kinect
            if kinect.has_new_depth_frame():
                # Get the depth data as a numpy array
                depth_frame = kinect.get_last_depth_frame()

                # Convert the depth frame to a bytes object
                depth_bytes = depth_frame.tobytes()

                # Write the depth data to the output file
                f.write(depth_bytes)

                print("Depth frame saved.")

except KeyboardInterrupt:
    print("Recording stopped by user.")
finally:
    # Close the Kinect runtime
    kinect.close()