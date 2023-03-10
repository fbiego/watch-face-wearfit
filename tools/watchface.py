import sys
import subprocess
import os

if len(sys.argv) < 2:
    print("Usage")
    print("\tOn MacOS, drag and drop files onto the python script to process them")
    print("\tOn Windows,  drag and drop files onto the batch script to process them")
    print("You can also run the command 'java -jar watchface.jar [dial.bin] 240 240'")
else:
    for filename in sys.argv[1:]:
        print("Current file:", os.path.basename(filename))
        subprocess.call(["java", "-jar", "watchface.jar", filename, "240", "280"])
