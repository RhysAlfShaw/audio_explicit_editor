# Explicit Audio Editor.

Author: Rhys A Shaw.
Date: 03-05-2023

This short program will reverse sections of an audio file and reverse it.
It is a great way to quickly make a song appropriate for the radio (removing swear words).

## Dependencies

* python 3.9 (might work with other versions, but not tested)
* moviepy
* numpy

## Installation

Clone this repository and install the dependencies.

```bash
git clone ...
cd audio_explicit_editor
pip install moviepy numpy
```

## Example

contents of test.ipynb

I would recommend adding a buffer of 0.25 seconds to the start and end time to ensure the audio is cut off.

```python
from AEE.audio_explicit_editor import reverse_audio_section

start_time = [3]                
end_time = [10]                 
input_file = "Cardi-B_WAP.mp3"  
output_file = "output.mp3"     

reverse_audio_section(input_file,output_file,start_time,end_time)
```

## Maintanence
If you want to report a bug, create an issue on github (I cannot promise I will be prompt in fixing it). If you want to fix a bug, create a pull request. 