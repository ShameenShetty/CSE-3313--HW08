# CSE-3313--HW08
This is the coding assignment for Homework 8 for CSE3313 (Introduction to Signal Processing).


## Purpose
Learn to amplify or attenuate a particular range of frequencies.


### Process
* Use skeleton file that teacher provided (*shelvingFilter.py*) which calls a function called `applyShelvingFilter(inName, outName, gain, cutoff)`. Where,
  - inName  = A string representing the name of an audio file in the WAVE format to read and process
  - outName = A string representing the name of an audio file that you will write in the WAVE format after applying the filter
  - gain    = An integer that represents the gain g of the filter. This is how much to increase or decrease the relevant frequencies and therefore could be negative.
  - cutoff  = An integer that represents the cut-off frequency f c of the filter. The modified magnitudes will be for frequencies in the range of 0 Hz to the cut-off frequency.
* We use the file *DSP_Filters_Electronics_Cookbook_Series_ch11.pdf* where it details the process that our shelving filter will use.
* Our program will: 
  - Plot the magnitudes of the fft of the original signal and the fft of the filtered signal with the x-axis of both plots in Hertz.
* If the fft of the original signal has *N* values, we will plot only the first *N/4* values.
