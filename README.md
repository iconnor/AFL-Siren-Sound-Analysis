# AFL-Siren-Sound-Analysis

This repository contains Python scripts for analyzing the frequency composition of the Australian Football League (AFL) game siren sound. It includes Fast Fourier Transform (FFT) analysis of .wav files, identification of the most prominent frequency peaks, and .wav sound generation based on the identified frequencies. The ultimate aim is to reproduce the siren sound using an Arduino microcontroller.

It also runs on the basis that the siren is a twin tone horn, the higher pitch note is a 5th (seven semitones apart). The frequency of the higher note is 3/2 times the frequency of the lower note.

## Samples

## Listen to the Sound

Here's the original sound file:

<audio src="./AFL Siren Sound Effect.wav" controls preload></audio>

|   | Sound File |
|---|------------|
| Original Sound | <audio src="https://media.githubusercontent.com/media/iconnor/AFL-Siren-Sound-Analysis/master/wav-files/AFL Siren Sound Effect.wav" controls preload></audio> |
| Echoed Sound | <audio src="https://media.githubusercontent.com/media/iconnor/AFL-Siren-Sound-Analysis/master/wav-files/echoed_sine_waves.wav" controls preload></audio> |
| Combined Sine Waves | <audio src="https://media.githubusercontent.com/media/iconnor/AFL-Siren-Sound-Analysis/master/wav-files/combined_sine_waves.wav" controls preload></audio> |
| Twin Tones | <audio src="https://media.githubusercontent.com/media/iconnor/AFL-Siren-Sound-Analysis/master/wav-files/twin_tones.wav" controls preload></audio> |



## Installation

To run these scripts, you need Python 3 installed. You also need the following Python libraries in your Juptyer environment:

- numpy
- scipy
- matplotlib

You can install these using pip:

```
pip install numpy scipy matplotlib
```

## Usage

Run the `afl-siren` notebook with a .wav file of the AFL siren sound as input. This notebook will perform an FFT analysis and identify the most prominent frequencies in the sound and then in the second block will generate a .wav file that is the sum of sine waves at each of the identified frequencies.

Please refer to the notebook for more.

## Credits

The siren file was generated from the following YouTube video: https://www.youtube.com/watch?v=h1GAsXHS_7s

## License

Copyright 2023 Ian Connor

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

See the [LICENSE](LICENSE.md) file for more details.