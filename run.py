import os
import subprocess

# Define the paths to the tools directory and the dials directory
TOOLS_DIR = "tools"
DIALS_DIR = "test"

# Define the name of the Java jar file to run
JAR_NAME = "watchface.jar"

# Find all .bin files in the dials directory and its subdirectories
bin_files = []
for root, dirs, files in os.walk(os.path.join(os.getcwd(), DIALS_DIR)):
    for file in files:
        if file.endswith(".bin"):
            f, e = os.path.splitext(file)
            if (os.path.exists(os.path.join(root, f + ".png"))):
                print("image for " + file + " exists")
            else:
                bin_files.append(os.path.join(root, file))

# Process each .bin file and save the name of processed files in a text file
for bin_file in bin_files:
    subprocess.call(["java", "-jar", os.path.join(TOOLS_DIR, JAR_NAME), bin_file, "240", "240"])

    # Get the directory of the processed file and create the path for the processed_files.txt file
    processed_files_path = os.path.join(os.path.dirname(bin_file), "README.md")

    # Save the name of the processed file in the processed_files.txt file
    with open(processed_files_path, "a+") as f:
        # Check if the file is empty
        f.seek(0)
        first_char = f.read(1)
        if not first_char:
            # If the file is empty, write some header text
            f.write("# Dials \n\n")
            f.write(" | Watchface | Binary |  \n")
            f.write(" | -- | -- |  \n")

        #![1](resources/dt78_app1.png?raw=true "3")
        f.write(" | ![watchface]("+ os.path.basename(bin_file).replace(".bin", ".png") + "?raw=true \"watchface\") | [`" + os.path.basename(bin_file) + "`](raw/main" + os.path.basename(bin_file) + ") |  \n")

# Save a text file showing all the paths of the generated text files
text_files = []
current_folder = os.getcwd()
for root, dirs, files in os.walk(current_folder):
    for file in files:
        if file.endswith(".md") and root != current_folder:
            relative_path = os.path.relpath(os.path.join(root, file), current_folder)
            text_files.append(relative_path)

header = '''# watch-face-wearfit
 
 A collection of watch face binary files.

 ## Collection

'''

footer = '''
## Installation
 
 They can be installed using Chronos app
 
 <a href='https://play.google.com/store/apps/details?id=com.fbiego.chronos&pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1'><img alt='Get it on Google Play' height="100px" src='https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png'/></a>


> **Warning**
> Install faces at your own risk as they may not be compatible with your watch

## Tools

The [`watchface.jar`](tools/watchface.jar) file can be used to rebuild the watchface background for the purpose of viewing only. Modifying the background is not yet possible for use as a watch face.

Extract > `java -jar watchface.jar 107_2_dial.bin 240 240`

On Windows, you can drag and drop the bin file on [`drag-drop.bat`](tools/drag-drop)

'''
with open("README.md", "w") as f:
    f.write(header)
    for text_file in text_files:
        f.write(" - [`" + os.path.dirname(text_file).replace("\\", "/") + "`](" + text_file.replace("\\", "/") + ")\n")
    f.write(footer)