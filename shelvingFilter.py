"""
    Name: Shameen Shetty
    ID: 1001429743
"""


import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

def applyShelvingFilter(inName, outName, g, fc) :
    soundData, sampleRate = sf.read(inName)

    mu = np.power(10, (g/20))
    fs = sampleRate
    theta_c = (2 * np.pi * fc) / fs
    
    gamma_numerator = 1 - ( ( 4 / (1 + mu) ) * np.tan(theta_c/2) )
    gamma_denominator = 1 + ( ( 4 / (1 + mu) ) * np.tan(theta_c/2) )

    gamma = gamma_numerator / gamma_denominator

    alpha = (1 - gamma) / 2

    mu_n = []
    y_n = []
    mu_n.append(0)
    for n in range(len(soundData)):
        if n == 0:
            result = alpha * (soundData[n])
            mu_n.append(result)
        else: 
            result = alpha * (soundData[n] + soundData[n-1]) + gamma * mu_n[n - 1]
            mu_n.append(result)
        
        filteredResult = soundData[n] + (mu - 1) * mu_n[n]
        y_n.append(filteredResult)

    filteredSignal = y_n
    
    
    
    ''' 
        Here we get the FFTs of both the original signal
        and the filtered signal
    '''
    originalSignal_FFT = np.fft.fft(soundData)
    filteredSignal_FFT = np.fft.fft(filteredSignal)

    # Here we are getting the magnitude of both the signals, so we can plot them properly.
    originalSignal_magnitude = []
    filteredSignal_magnitude = []

    # We are taking the magnitudes of the two arrays, because originally they are in complex form a+ib
    # which will not plot properly.
    for i in range(len(originalSignal_FFT)):
        # np.linalg.norm(originalSignal_FFT[i])
        originalMagnitude = abs(originalSignal_FFT[i])
        originalSignal_magnitude.append(originalMagnitude)

        # np.linalg.norm(filteredSignal[i])
        filteredMagnitude = abs(filteredSignal_FFT[i])
        filteredSignal_magnitude.append(filteredMagnitude)
    
    # Getting the length of the original signals magnitude and then dividing by 4
    #  so that we can plot only the first N/4. We convert it to an int 
    # to make sure that we aren't accidentally entering a float value.
    data_len = len(originalSignal_magnitude)
    first_oneFourth = int(data_len/4)

    fig1, axs1 = plt.subplots(nrows=1, ncols=2)
    # Here we are getting the maximum value in the orginalSignal array and the 
    # filteredSignal array, and then choosing the max between those two, which
    # will be stored in the ylim - because, if the second array has a max magnitude of
    # 12000, and the first has a max of 8000, we want the y-axis of both plots to go from
    # 0 to 12000, instead of one being 8000 and the other being 12000
    # Then we add 100, so we are plotting the max value for both plots, plus 100
    originalMax = np.amax(originalSignal_magnitude) # amax gets max val in array
    filteredMax = np.amax(filteredSignal_magnitude)
    yLimit = max(originalMax, filteredMax) # find which maximum is bigger
    yLimit = yLimit + 100

    axs1[0].set_ylim(0, yLimit)
    axs1[1].set_ylim(0, yLimit)

    # We set the individual titles for each of the subplots (original signal, filtered signal),
    # then we set the global title for the entire plot itself, hence figure.suptitle()
    axs1[0].set_title('Original Signal', color='blue', fontname='Cambria')
    axs1[1].set_title('Filtered Signal', color='blue', fontname='Cambria')
    fig1.suptitle('Comparision of signal after applying shelving filter', color='grey', fontsize=16, fontname='Cambria')

    axs1[0].set_xlabel('Hz')
    axs1[1].set_xlabel('Hz')

    axs1[0].plot(originalSignal_magnitude[:first_oneFourth])
    axs1[1].plot(filteredSignal_magnitude[:first_oneFourth])
    plt.tight_layout
    plt.show()

    # writing the filtered signal to a file whose name is determined by 
    # whatever value is inputted in outName
    filteredSignal = np.array(filteredSignal)
    realFilteredSignal = filteredSignal.real
    sf.write(outName, realFilteredSignal,  sampleRate)

##########################  main  ##########################
if __name__ == "__main__" :
    inName = "P_9_1.wav"
    gain = -10  # can be positive or negative
                # WARNING: small positive values can greatly amplify the sounds
    cutoff = 300
    outName = "shelvingOutput.wav"

    applyShelvingFilter(inName, outName, gain, cutoff)
