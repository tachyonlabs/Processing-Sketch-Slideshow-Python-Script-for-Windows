import subprocess
import time
import os

SKETCHBOOK_DIRECTORY = "your sketchbook location here"
SECONDS_BEFORE_CLOSING_PREVIOUS_SKETCH = 15
SECONDS_TO_DISPLAY_EACH_SKETCH = 30

# get a list of all folders that actually have sketches in them
sketches = [name for name in os.listdir(SKETCHBOOK_DIRECTORY) if os.path.exists("{}/{}/{}".format(SKETCHBOOK_DIRECTORY, name, "build/build.pde"))]
idx = 0
sketch, prev = None, None

# cycle through the sketches forever :-)
while True:
    # keep a reference to the current sketch subprocess so we can shut it down after starting the next one
    if sketch:
        prev = sketch
    next_sketch = sketches[idx % len(sketches)]

    # open the next sketch with Processing
    sketch = subprocess.Popen('processing-java --sketch="{}/{}/build" --output="{}/{}/build/output" --force --run'.format(SKETCHBOOK_DIRECTORY, next_sketch, SKETCHBOOK_DIRECTORY, next_sketch))
    time.sleep(SECONDS_BEFORE_CLOSING_PREVIOUS_SKETCH)

    # close the previous sketch behind the scenes
    # it seems a little extreme, but I had no luck with things like os.kill(), sketch.terminate(), etc. under Windows
    if prev:
        subprocess.call(['taskkill', '/F', '/T', '/PID', str(prev.pid)])

    time.sleep(SECONDS_TO_DISPLAY_EACH_SKETCH - SECONDS_BEFORE_CLOSING_PREVIOUS_SKETCH)
    # and on to the next sketch in the list
    idx += 1
