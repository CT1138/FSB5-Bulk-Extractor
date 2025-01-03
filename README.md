# Hello :3
I wrote this to extract sound banks from SOMA. Should work with most FSB5 sound banks. <br>
This script uses the FSB5 library for its conversions and is essentially just a wrapper. As such, you must install FSB5 with pip and make sure the bundled .dll's are in the working directory of the script.
FSB5 repository: https://github.com/HearthSim/python-fsb5

# Usage:
1. Install FSB5 if not installed <br>
    **pip install FSB5**
3. Move script and dll's to the directory of your sound banks (.fsb files) <br>
4. Run the script with python <br>
    **python ./decompressFSB.py**
   
### The script will search the working directory recursivelly and will unpack any found .fsb banks to .ogg files.
Extracted samples will be put in their own folders per source bank <br>
**Example:** <br>
### Input:
    ./sounds/special/player_fx.fsb
### Output:
    ./output/sounds/special/player_fx/{samplename}.ogg
