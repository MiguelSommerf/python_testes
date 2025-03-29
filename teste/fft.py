#Fast Fourier Transform em Python

#Para utilizar a FFT, antes precisamos de um áudio, e os respectivos valores desse áudio: Frequência de amostragem, período de amostragem, e o número de pontos do áudio.

import numpy as np
import librosa as lib
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, ifft
import soundfile as sf

#Atribuição de valores importantes para a FFT
audio_sinal, sample_rate = lib.load(r'C:\Users\HueHu\OneDrive\Área de Trabalho\teste\sounds\C Major Scale.mp3', sr=None)

#Descobrindo os valores do sinal
num_points = len(audio_sinal) #num_points recebe a quantidade de amostras
audio_duration = num_points/sample_rate #audio_duration recebe a duração do áudio
sample_period = 1/sample_rate #sample_period recebe o período de amostragem (tempo entre uma amostragem e outra)

print(f"sample rate: {sample_rate}")
print(f"taxa de amostras: {num_points}")
print(f"período de amostragem: {sample_period}")
print(f"duração: {audio_duration}")

#Executando a FFT
yf = fft(audio_sinal)
xf = fftfreq(num_points,sample_period)

#Removendo frequências indesejadas
freq_min, freq_max = 345, 355
index = np.where((np.abs(xf) >= freq_min) & (np.abs(xf) <= freq_max))[0]
yf_filtered = yf.copy()
yf_filtered[index] = 0

#Salvando as alterações
audio_changed = ifft(yf_filtered).real
audio_changed = audio_changed / np.max(np.abs(audio_changed))
sf.write('C_Major_Scale_349hz.wav', audio_changed, sample_rate)

#Plotando o gráfico
plt.figure()
plt.plot(xf[:num_points//2], 2.0/num_points * np.abs(yf[:num_points//2]))
plt.grid() #Coloca grades ao gráfico para facilitar a visualização
plt.xlabel("Frequência (Hz)") #Nomeia X
plt.ylabel("Amplitude") #Nomeia Y
plt.title("Espectograma de Frequência (FFT)") #Adiciona um título ao gráfico
plt.show() #Executa o código