
import numpy as np
from scipy.io.wavfile import write

# Settings
sample_rate = 44100  # Sample rate in Hz
duration = 5.0  # seconds
A4_frequency = 440
A4_note_number = 69
note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def note_to_frequency(note_name):

    # Separate the note name and the octave
    note, octave = note_name[:-1], int(note_name[-1])

    # Calculate the note number
    note_number = note_names.index(note) + (octave + 1) * 12

    # Calculate the frequency
    frequency = A4_frequency * 2 ** ((note_number - A4_note_number) / 12)

    return frequency

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Guess the notes used and generate wav file',
                                     usage='python %(prog)s E5 B5', epilog='Good luck!')
    parser.add_argument('notes', metavar='N', type=str, nargs='+', help='Notes to guess separated by spaces')
    
    args = parser.parse_args()
    signal = None        
    # Generate the time values for each sample
    t = np.arange(int(sample_rate * duration)) / sample_rate
    for note in args.notes:
        print(note, note_to_frequency(note))
        if signal is None:
            signal = 0.05 * np.sin(2 * np.pi * note_to_frequency(note) * t)
        else:
            signal += 0.05 * np.sin(2 * np.pi * note_to_frequency(note) * t)
    

    # Write to .wav file within range for a 16-bit .wav file
    scaled_signal = np.int16(signal/np.max(np.abs(signal)) * 32767)
    write(f'./wav-files/{"_".join(args.notes)}_notes.wav', sample_rate, scaled_signal)

if __name__ == '__main__':
    main()