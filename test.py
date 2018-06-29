import subprocess
import time
import os
import random

#SKETCHBOOK_DIRECTORY = "your sketchbook location here"
SKETCHBOOK_DIRECTORY = "F:\processing-3.3.7\sketchbook"
SECONDS_BEFORE_CLOSING_PREVIOUS_SKETCH = 15
SECONDS_TO_DISPLAY_EACH_SKETCH = 30
SORT_RANDOM_ORDER, SORT_ALPHABETICAL_ORDER, SORT_DIRECTORY_ORDER = 0, 1, 2
DISPLAY_ORDER = SORT_RANDOM_ORDER

def get_sketches(sort_order):
    # Return a list of all folders that actually have sketches in them, in the selected display order
    dirs = [name for name in os.listdir(SKETCHBOOK_DIRECTORY) if os.path.exists("{}/{}/{}".format(SKETCHBOOK_DIRECTORY, name, "build/build.pde"))]
    if sort_order == SORT_ALPHABETICAL_ORDER:
        dirs.sort(key=str.lower)
    elif sort_order == SORT_RANDOM_ORDER:
        random.shuffle(dirs)

    return dirs[:]

idx = 0
sketch, prev = None, None

# Cycle through the sketches forever :-)
while True:
    # Keep a reference to the current sketch subprocess so we can shut it down after starting the next one
    if sketch:
        prev = sketch

    # Get the list of sketches each time we're starting a new cycle -- this serves both to include any new sketches
    # that have been added to the sketchbook, and to re-randomize if we're using DISPLAY_ORDER of SORT_RANDOM_ORDER
    if idx == 0:
        sketches = get_sketches(DISPLAY_ORDER)
    next_sketch = sketches[idx]

    # Open the next sketch with Processing
    sketch = subprocess.Popen('processing-java --sketch="{}/{}/build" --output="{}/{}/build/output" --force --run'.format(SKETCHBOOK_DIRECTORY, next_sketch, SKETCHBOOK_DIRECTORY, next_sketch))
    time.sleep(SECONDS_BEFORE_CLOSING_PREVIOUS_SKETCH)

    # Close the previous sketch behind the scenes -- it seems a little extreme, but I had no luck with things
    # like os.kill(), sketch.terminate(), etc. under Windows
    if prev:
        subprocess.call(['taskkill', '/F', '/T', '/PID', str(prev.pid)], stdout=open(os.devnull, 'wb'), stderr=open(os.devnull, 'wb'))
    time.sleep(SECONDS_TO_DISPLAY_EACH_SKETCH - SECONDS_BEFORE_CLOSING_PREVIOUS_SKETCH)

    # And on to the next sketch in the list
    idx = (idx + 1) % len(sketches)
