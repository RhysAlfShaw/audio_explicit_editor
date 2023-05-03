'''
audio_explicit_editor.py
Author: Rhys Alfred Shaw
Date: 2021-09-01

Description: This script contains functions for reversing audio sections of an audio file.
'''
# Import the necessary packages

from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.audio.AudioClip import concatenate_audioclips, AudioArrayClip
import numpy as np


def is_list(var):
    '''
    decsription: This function checks if the input variable is a list.
    ''' 
    if isinstance(var, list):
        return True
    else:
        return False


def reverse_audio_section(input_file,output_file,start_time,end_time):
    '''
    Decription: This function takes an audio file and reverses the audio between the start and end time.

    Input:
        input_file (string): The path to the input audio file.
        output_file (string): The path to the output audio file.
        start_time (list): The start times of the audio sections to be reversed.
        end_time (list): The end times of the audio scetions to be reversed.

    Output:
        None
        (will create a new audio file at the output_file path)

    Example:
        reverse_audio_section('input_file.mp3','output_file.mp3',[0,10],[5,15])
    '''

    original_audio = AudioFileClip(input_file)

    if is_list(start_time) == True:
        for ts in range(0,len(start_time)):
        
            reversed_audio = original_audio.subclip(start_time[ts],end_time[ts])
            # Reverse the audio data
            reversed_audio_array = reversed_audio.to_soundarray()

            reversed_audio_array_flipped = np.flip(reversed_audio_array)

            reversed_audio_flipped = AudioArrayClip(reversed_audio_array_flipped, fps=reversed_audio.fps)

            # Concatenate the original and reversed audio
            if ts == 0:

                before_audio = original_audio.subclip(0, start_time[ts])
        
            else: 

                before_audio = final_audio.subclip(0, start_time[ts])
        
            after_audio = original_audio.subclip(end_time[ts])
            final_audio = concatenate_audioclips([before_audio, reversed_audio_flipped, after_audio])

    else:
        reversed_audio = original_audio.subclip(start_time,end_time)
        # Reverse the audio data
        reversed_audio_array = reversed_audio.to_soundarray()
        reversed_audio_array_flipped = np.flip(reversed_audio_array)
        reversed_audio_flipped = AudioArrayClip(reversed_audio_array_flipped, fps=reversed_audio.fps)
        # Concatenate the original and reversed audio
        before_audio = original_audio.subclip(0, start_time)
        after_audio = original_audio.subclip(end_time)
        final_audio = concatenate_audioclips([before_audio, reversed_audio_flipped, after_audio])

    # Save the edited audio to output file
    final_audio.write_audiofile(output_file)
