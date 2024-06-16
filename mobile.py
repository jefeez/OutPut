import socket
import pyaudio


def capture_and_send_audio(client_ip, client_port):
    chunk = 1024  # Número de frames por buffer
    format = pyaudio.paInt16  # Formato de áudio
    channels = 1  # Canal único
    rate = 44100  # Taxa de amostragem

    p = pyaudio.PyAudio()
    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((client_ip, client_port))

    print("SEEDING AUDIO...")

    try:
        while True:
            data = stream.read(chunk)
            client_socket.sendall(data)
    except Exception as e:
        print(f"Error during capture/send: {e}")
    finally:
        print("Ending audio sending.")
        stream.stop_stream()
        stream.close()
        p.terminate()
        client_socket.close()


if __name__ == "__main__":
    client_ip = '192.168.66.174'
    client_port = 5000
    capture_and_send_audio(client_ip, client_port)
