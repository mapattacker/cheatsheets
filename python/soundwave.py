from scipy.io import wavfile
rate, audio = wavfile.read('data/nightingale.wav')

# https://www.xeno-canto.org

import librosa
data, sampling_rate = librosa.load('your_file.mp3')


# https://www.analyticsvidhya.com/blog/2017/08/audio-voice-processing-deep-learning/
# https://www.nch.com.au/wavepad/index.html
# https://towardsdatascience.com/audio-classification-using-fastai-and-on-the-fly-frequency-transforms-4dbe1b540f89