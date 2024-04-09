import socket
import threading

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

# Main function to handle client setup and user input
def main():
    # Client configuration
    host = '127.0.0.1'
    port = 12340

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    try:
        client_socket.connect((host, port))
        print("connected")
    except Exception as e:
        print(f"Error connecting to server: {e}")
        return

    # Start a thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Send messages to the server
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

    # Close the client socket
    client_socket.close()

if __name__ == "__main__":
    main()
