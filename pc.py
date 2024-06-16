import socket
import pyaudio


def receive_and_play_audio(listen_ip, listen_port):
    chunk = 1024
    format = pyaudio.paInt16
    channels = 1
    rate = 44100

    p = pyaudio.PyAudio()
    stream = p.open(format=format, channels=channels,
                    rate=rate,
                    output=True,
                    frames_per_buffer=chunk)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((listen_ip, listen_port))
    server_socket.listen(1)
    print("WAIT CONNECTION....")

    conn, addr = server_socket.accept()
    print(f"CONNECT BY {addr}")

    try:
        while True:
            data = conn.recv(chunk)
            if not data:
                break
            stream.write(data)
    except Exception as e:
        print(f"Error during reception/playback: {e}")
    finally:
        print("Terminating audio reception.")
        stream.stop_stream()
        stream.close()
        p.terminate()
        conn.close()
        server_socket.close()


if __name__ == '__main__':
    listen_ip = '0.0.0.0'
    listen_port = 5000
    receive_and_play_audio(listen_ip, listen_port)
