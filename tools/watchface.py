import sys
import subprocess

for filename in sys.argv[1:]:
    print("Current file:", filename)
    subprocess.call(["java", "-jar", "watchface.jar", filename, "240", "280"])
