# /// script
# requires-python = ">=3.7"
# dependencies = ["numpy", "scipy"]
# ///

import os
import numpy as np
import scipy.io.wavfile as wavfile

_dir = os.path.dirname(os.path.abspath(__file__))

# Parameters
# **********

# Input audio file must be readable by scipy.io.wavfile.read() function
input_file = os.path.join(_dir, 'Marimba.wav')
output_file = os.path.join(_dir, 'output.wav')


# Read input file
# ***************

fs, input_data = wavfile.read(input_file, mmap=True)
# convert to float
max_value = float(-np.iinfo(input_data.dtype).min)
input_data = input_data.astype('float32') / max_value
# convert to mono if not already
if len(input_data.shape) > 1:
    input_data = np.mean(input_data, axis=1)
input_data = input_data.flatten()


# Audio data process
# ******************

output_data = np.zeros(len(input_data))

# *************************
# * PROCESSING COMES HERE *
# *************************

# *** Echo ****************
#
#delay = 0.5         # Delay (s)
#d = int(delay*fs)
#feedback = .5
#output_data = input_data
#for i in range(d,len(input_data)):
#    output_data[i] += feedback*output_data[i-d]
# *************************

# *** Vibrato *************
# Low frequency oscillator
f_low = 5       # frequency (Hz)
a_low = 10      # freq shift amplitude 

for n in range(len(input_data)):
    output_data[n] = input_data[n - a_low*(1+np.sin(f_low*2*np.pi*n))/2] # /!\



# *************************


# Save output
# ***********
output_data = 0.99 * output_data / max(abs(output_data))
wavfile.write(output_file, int(fs), (output_data*np.iinfo(np.int16).max).astype(np.int16))
