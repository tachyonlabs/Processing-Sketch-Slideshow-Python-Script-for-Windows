import subprocess
import time
import os
import random

# replace "your sketchbook location here" below with the location of your Processing sketchbook, for example
# it might be something like "F:/processing-3.3.7/sketchbook". Use "/" "forward slashes" in the path as shown
# in that example, not "\" "backslashes".
SKETCHBOOK_DIRECTORY = "your sketchbook location here"
SECONDS_BEFORE_CLOSING_PREVIOUS_SKETCH = 15
SECONDS_TO_DISPLAY_EACH_SKETCH = 30
SORT_RANDOM_ORDER, SORT_ALPHABETICAL_ORDER = 0, 1
DISPLAY_ORDER = SORT_RANDOM_ORDER

def get_sketches(sort_order):
    # Recursively find and return a list of all folders in the sketchbook that actually have sketches in them,
    # in the selected display order
    def find_all_sketches(dir):
        dir_contents = [name.lower() for name in os.listdir(dir)]
        for name in dir_contents:
            with_path = dir + "/" + name
            last_dir = dir[dir.rindex("/") + 1:]
            if name.endswith(last_dir + ".pde"):
                sketch_dirs.append(dir)
            elif os.path.isdir(with_path):
                find_all_sketches(with_path)

    sketch_dirs = []
    find_all_sketches(SKETCHBOOK_DIRECTORY.lower())

    if sort_order == SORT_ALPHABETICAL_ORDER:
        sketch_dirs.sort(key=lambda path: path[path.rindex("/") + 1:])
    elif sort_order == SORT_RANDOM_ORDER:
        random.shuffle(sketch_dirs)

    return sketch_dirs[:]

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
    sketch = subprocess.Popen('processing-java --sketch="{}" --force --run'.format(next_sketch))
    time.sleep(SECONDS_BEFORE_CLOSING_PREVIOUS_SKETCH)

    # Close the previous sketch behind the scenes -- it seems a little extreme, but I had no luck with things
    # like os.kill(), sketch.terminate(), etc. under Windows
    if prev:
        subprocess.call(['taskkill', '/F', '/T', '/PID', str(prev.pid)], stdout=open(os.devnull, 'wb'), stderr=open(os.devnull, 'wb'))
    time.sleep(SECONDS_TO_DISPLAY_EACH_SKETCH - SECONDS_BEFORE_CLOSING_PREVIOUS_SKETCH)

    # And on to the next sketch in the list
    idx = (idx + 1) % len(sketches)
