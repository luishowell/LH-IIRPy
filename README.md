# LH-IIRPy

An IIR filter library written in Python.

This library features design and filtering using cascaded 2nd order IIR Butterworth filters.
 
The filter uses the Direct Form II structure.

## Prerequisites
 
This library requires Numpy and SciPy signal to be installed.

## Usage

`import lh_iirpy`

### Constructor

`new_filter = lh_iirpy.IIR2Filter()`

### Initialisation

1. Bandstop

   `new_filter.bandStop(order,Samplingfreq,Lower cutoff freq,Upper cutoff freq)`

2. Bandpass

   `new_filter.bandPass(order,Samplingfreq,Lower cutoff freq,Upper cutoff freq)`

3. Lowpass

   `new_filter.lowPass(order,Samplingfreq,Cutoff freq)`

4. Highpass

   `new_filter.highPass(order,Samplingfreq,Cutoff freq)`

### Filtering

Sample by sample allowing for real-time filtering:

`new_filter.filter(v)`

## Coding Example

See `Demo` folder for an example of using this library to remove 50Hz noise from an ECG. Run `demo.py` to show plots of ECG before and after filtering in the frequency and time domain. 

Running this demo requires Matplotlib pyplot to be installed.    
