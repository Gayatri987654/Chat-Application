import socket
import threading

# Function to handle incoming client connections
def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")

    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            print(f"Connection from {address} closed.")
            break

        print(f"Received message from {address}: {data}")

        # Broadcast the received message to all connected clients
        broadcast(data, client_socket)

    # Close the client connection
    client_socket.close()

# Function to broadcast message to all connected clients except the sender
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Error broadcasting message: {e}")
                client.close()
                clients.remove(client)

# Main function to handle server setup and connections
def main():
    # Server configuration
    host = '127.0.0.1'
    port = 12340

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Start listening for incoming connections
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        # Accept a client connection
        client_socket, address = server_socket.accept()
        clients.append(client_socket)

        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

# List to store client sockets
clients = []

if __name__ == "__main__":
    main()
