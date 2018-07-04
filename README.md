# Processing Sketch Slideshow Python Script for Windows

## About the project

I'm a volunteer at the [Idea Fab Labs](https://santacruz.ideafablabs.com/) maker/hacker/artspace here in Santa Cruz, 
and when I came in for my shift today, I was surprised to see a giant (six feet tall? I should have measured) glossy 
black monolith, with most of the front being a giant display, and with a Windows computer somehow built into it. I 
don't know where it came from, or what it had been doing in a previous life, but I was asked to write a script for it 
that would continuously cycle through and display all the Processing graphics and animations sketches in a sketchbook 
network folder, joining the Raspberry Pi Instagram [Slideshow](https://github.com/tachyonlabs/raspberry_pi_instagram_slideshow) 
and [Slide and Video Show](https://github.com/tachyonlabs/raspberry_pi_slide_and_video_show) installations I had 
previously done in providing cool giant video displays for IFL open houses and other events, and making it easy for 
members to add their artworks to the slideshow by copying their sketches into the sketchbook.

BTW, I had never used/run Processing before this (though I had heard of it), and now I want to do at least one sketch 
of my own to copy into the IFL sketchbook next week, so I can have some art in the slideshow myself. :-)

## What you need to do to run the script

#### The script as-is requires Windows
I tested the script on systems running Windows 7 and Windows 10, but the operative word here is *Windows*. If 
you're running on another OS the general idea should be the same, but you'll need to look up and modify the commands 
it uses both to launch Processing with a sketch at the command line, and to terminate that process after moving on to 
the next sketch.

#### And it requires Python 
What can I say, it's a Python script ... it will work with either Python 2 or Python 3, so if you don't already have 
at least one of them installed on your computer, you should pay a visit to 
[https://www.python.org/downloads/](https://www.python.org/downloads/).

#### It also requires Processing
Because this script is starting and closing instances of Processing to display sketches, if you don't already have 
Processing installed on your computer, you will need to install it, by visiting 
[https://processing.org/download/](https://processing.org/download/). 

#### Copy the `processing_slideshow.py` script to your Processing directory
Copy the script [`processing_slideshow.py`](https://github.com/tachyonlabs/Processing-Sketch-Slideshow-Python-Script-for-Windows/blob/master/processing_slideshow.py) from this repo to your Processing directory -- the directory that has the files 
`processing.exe` and `processing-java.exe` (among others) in it.

#### Configure the script with the location of your sketchbook
Run Processing.exe and select `Preferences` in the `File` pull-down menu to copy the location of your sketchbook. Then 
replace "your sketchbook location here" in this line in the script -- `SKETCHBOOK_DIRECTORY = "your sketchbook location 
here"` -- with your sketchbook location. Use "/" "forward slashes" in the path as in this example -- 
"F:/processing-3.3.7/sketchbook" -- not "\" "backslashes".

#### Configure the sketch display order, if you like
By default the script displays sketches in random order (good both for variety in general, and also for if you have a 
bunch of sketches with similar names that are variations of each other), but if you like you can set the 
`DISPLAY_ORDER` variable to `SORT_ALPHABETICAL_ORDER` instead.

#### Try running the Processing sketch slideshow script at the command line
Open up a terminal window, navigate to your Processing directory, and enter
```
python processing_slideshow.py
```
at the command line. The slideshow will start once Processing starts and runs the first sketch in your sketchbook. Or if 
you like you can make a desktop shortcut or Windows menu entry to automatically run `python processing_slideshow.py` 
from your Processing directory when you click or select it.

#### You'll probably want to edit your sketches to make them full screen if they aren't already
IMHO randomly-sized sketches popping up doesn't make for the greatest-looking slideshow. What you would want to do 
about that depends on whether an individual sketch is using a 2D or 3D renderer:
* *For a 2D renderer*, the first line below the line `void setup() {` in your sketch should be `fullScreen();`, and you 
should comment out your `size` line.
* *For a 3D renderer* (your size statement will have `P3D` after the width and height values), you can't use 
`fullScreen()`, but you can set the size width and height values to match your screen resolution.

#### You might want to move your not-yet-working sketches temporarily out of your sketchbook
If you have any sketches you've started working on, but that just give error messages when you try to run them, yeah, 
you may want to temporarily move them out of your sketchbook, because that won't look very good in the slideshow. 
Ditto for any that haven't moved beyond the, say, white rectangle on a gray background level yet. :-) 
