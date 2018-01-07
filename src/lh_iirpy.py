import numpy as np
import scipy.signal as signal


class IIR2Filter:

    # design methods using second order sections Butterworth IIR filters
    def bandStop(self, order, fs, lower_cutoff, upper_cutoff):
        self.coeffs = signal.butter(order, [lower_cutoff/fs*2, upper_cutoff/fs*2], btype='bandstop', output='sos')
        self.shape = np.shape(self.coeffs)
        self.order = self.shape[0]
        self.delay2 = np.zeros(self.order)
        self.delay1 = np.zeros(self.order)

    def bandPass(self, order, fs, lower_cutoff, upper_cutoff):
        self.coeffs = signal.butter(order, [lower_cutoff/fs*2, upper_cutoff/fs*2], btype='bandpass', output='sos')
        self.shape = np.shape(self.coeffs)
        self.order = self.shape[0]
        self.delay2 = np.zeros(self.order)
        self.delay1 = np.zeros(self.order)

    def lowPass(self, order, fs, cutoff):
        self.coeffs = signal.butter(order, cutoff/fs*2, btype='lowpass', output='sos')
        self.shape = np.shape(self.coeffs)
        self.order = self.shape[0]
        self.delay2 = np.zeros(self.order)
        self.delay1 = np.zeros(self.order)

    def highPass(self, order, fs, cutoff):
        self.coeffs = signal.butter(order, cutoff/fs*2, btype='highpass', output='sos')
        self.shape = np.shape(self.coeffs)
        self.order = self.shape[0]
        self.delay2 = np.zeros(self.order)
        self.delay1 = np.zeros(self.order)

    # direct form II filter
    def filter(self, input_value):

        for n in range(self.order):

            input_acc = input_value + (-(self.coeffs[n][4])*self.delay1[n]) + (-(self.coeffs[n][5])*self.delay2[n])

            output_acc = (input_acc*self.coeffs[n][0]) + (self.coeffs[n][1]*self.delay1[n]) + (self.coeffs[n][2]*self.delay2[n])

            self.delay2[n] = self.delay1[n]
            self.delay1[n] = input_acc
            input_value = output_acc

        return output_acc
