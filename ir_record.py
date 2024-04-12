import numpy as np
import cv2
import time

# Import the necessary modules from pykinect2
from pykinect2 import PyKinectRuntime

# Initialize the Kinect runtime
kinect = PyKinectRuntime.PyKinectRuntime(PyKinectRuntime.FrameSourceTypes_Infrared)

# Define the dimensions of the IR frame
ir_width, ir_height = kinect.infrared_frame_desc.Width, kinect.infrared_frame_desc.Height

# Define the output file path
output_file = "ir_data.bin"

# Set the desired frame rate (frames per second)
desired_fps = 30  # Adjust as needed

# Calculate the delay between each frame capture
frame_delay = 1.0 / desired_fps

try:
    # Open the output file in binary mode for writing
    with open(output_file, "wb") as f:
        # Main loop to capture and save IR data
        while True:
            start_time = time.time()

            # Get the latest IR frame from the Kinect
            if kinect.has_new_infrared_frame():
                # Get the IR data as a numpy array
                ir_frame = kinect.get_last_infrared_frame()

                # Convert the IR frame to a bytes object
                ir_bytes = ir_frame.tobytes()

                # Write the IR data to the output file
                f.write(ir_bytes)

                print("IR frame saved.")

            # Calculate elapsed time since frame capture
            elapsed_time = time.time() - start_time

            # Introduce delay to achieve desired frame rate
            if elapsed_time < frame_delay:
                time.sleep(frame_delay - elapsed_time)

except KeyboardInterrupt:
    print("Recording stopped by user.")
finally:
    # Close the Kinect runtime
    kinect.close()