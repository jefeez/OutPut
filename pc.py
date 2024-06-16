import pyaudio
import socket

# Configurações do servidor de escuta
HOST = '0.0.0.0'  # Todos os interfaces
PORT = 12345

# Configuração do PyAudio
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Inicializar PyAudio
audio = pyaudio.PyAudio()

# Criar um socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Listening on {HOST}:{PORT}...")

# Aguardar conexão do cliente (seu dispositivo móvel)
client_socket, addr = server_socket.accept()
print(f"Connected by {addr}")

# Abrir stream de entrada do PyAudio
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True, frames_per_buffer=CHUNK)

print("Capturing audio...")

try:
    while True:
        # Ler dados do stream de entrada
        data = stream.read(CHUNK)
        # Enviar dados capturados para o cliente (se necessário)
        client_socket.sendall(data)
except KeyboardInterrupt:
    print("Interrupted")
finally:
    # Fechar conexões e stream de áudio
    stream.stop_stream()
    stream.close()
    audio.terminate()
    client_socket.close()
    server_socket.close()
