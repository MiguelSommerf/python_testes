import librosa as lib
import matplotlib.pyplot as plt
from IPython.display import Audio

def playerDeAudio(endereco):
    audio_data, sample_rate = lib.load(endereco, sr=None)
    print(f"Taxa de amostragem: {sample_rate} Hz")
    print(f"Dados do áudio: {audio_data}")

    #Mostra se o tipo do áudio é mono ou estéreo
    print(f"Formato do array de áudio: {audio_data.shape}")
    return Audio(audio_data, rate = sample_rate)

def ondasSonoras(endereco):
    audio_data, sample_rate = lib.load(endereco, sr=None)
    print(f"Taxa de amostragem: {sample_rate} Hz")
    print(f"Dados do áudio: {audio_data}")
    
    print(f"Formato do array do áudio: {audio_data.shape}")
    return plt.figure(), plt.plot(endereco)