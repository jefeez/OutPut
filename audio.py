import pyaudio

# Inicializa o PyAudio
p = pyaudio.PyAudio()

# Lista os dispositivos de áudio disponíveis
print("Lista de dispositivos de áudio:")
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(f"Dispositivo {i}: {info['name']} - Entradas: {info['maxInputChannels']}, Saídas: {info['maxOutputChannels']}")

# Fecha o PyAudio
p.terminate()