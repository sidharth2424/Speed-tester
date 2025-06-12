import socket

# Config
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 5001       # Port number
BUFFER_SIZE = 4096
DATA = b'x' * BUFFER_SIZE  # Dummy data to send

def start_server():
    # Step 1: Create TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))    # Step 2: Bind to port
        s.listen()              # Step 3: Start listening for client
        print(f"Server listening on port {PORT}")
        
        conn, addr = s.accept() # Step 4: Accept incoming connection
        with conn:
            print(f"Connected by {addr}")
            
            # Step 5: Receive upload data from client
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break
            print("Finished receiving upload data.")
            
            # Step 6: Send dummy data to client (simulate download)
            for _ in range(5000):
                conn.sendall(DATA)
            print("Finished sending download data.")

if __name__ == "__main__":
    start_server()
