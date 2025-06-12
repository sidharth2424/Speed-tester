import socket
import time

# Config
HOST = '127.0.0.1'  # Use 'localhost' or the server IP
PORT = 5001
BUFFER_SIZE = 4096
UPLOAD_SIZE_MB = 10
UPLOAD_BYTES = UPLOAD_SIZE_MB * 1024 * 1024

def test_speed():
    # Step 1: Connect to server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # Step 2: Upload test
        upload_data = b'x' * BUFFER_SIZE
        start_upload = time.time()
        sent = 0
        while sent < UPLOAD_BYTES:
            s.sendall(upload_data)
            sent += len(upload_data)
        s.shutdown(socket.SHUT_WR)  # Tell server upload is done
        end_upload = time.time()
        upload_duration = end_upload - start_upload
        upload_speed = (UPLOAD_BYTES * 8) / (upload_duration * 1_000_000)  # Mbps
        print(f"Upload Speed: {upload_speed:.2f} Mbps")

        # Step 3: Download test
        start_download = time.time()
        received = 0
        while True:
            data = s.recv(BUFFER_SIZE)
            if not data:
                break
            received += len(data)
        end_download = time.time()
        download_duration = end_download - start_download
        download_speed = (received * 8) / (download_duration * 1_000_000)  # Mbps
        print(f"Download Speed: {download_speed:.2f} Mbps")

if __name__ == "__main__":
    test_speed()
