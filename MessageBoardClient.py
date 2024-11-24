import socket
import sys

class SocketWrapper:
    # Task 1: Socket initialization
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(10)

    # Task 2: Initiate the connection request
    def connect(self, host, port):
        self.socket.connect((host, port))

    # Task 3: Send command to the server
    def send(self, msg):
        self.socket.send(msg.encode('utf-8'))

    # Task 4: Receive the message from the server
    def receive(self):
        response = self.socket.recv(1024)
        if response:
            response_str = response.decode('utf-8').strip()
            print(f"server: {response_str}")
            return response_str
        else:
            print("No data received, connection might be closed.")
            return ""

    def close(self):
        self.socket.close()

# Main function to run the client
def main():
    if len(sys.argv) != 3:
        print("Usage: MessageBoardClient <server_ip> <server_port>")
        sys.exit(1)
    else:
        server_ip = sys.argv[1]
        server_port = int(sys.argv[2])

    client_socket = SocketWrapper()

    try:
        client_socket.connect(server_ip, server_port)

        while True:
            command = input("client: ").upper()
            client_socket.send(command)
            if command == 'POST' or command == 'DELETE':
                # Handle the data input by users in POST and DELETE
                while True:
                    user_input = input("client: ")
                    client_socket.send(user_input)
                    if (user_input == '#'): 
                        client_socket.receive()
                        break
            elif command == 'GET':
                # Print the data received from server
                while True:
                    response = client_socket.receive()
                    if response == "#":
                        break
            elif command == 'QUIT':
                response = client_socket.receive()
                if response == "OK":
                    # Task 5: Close socket
                    client_socket.close()
                    break
            else:
                client_socket.receive()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except socket.timeout:
        print("Receive timed out, no data received within the timeout period.")
    except Exception as e:
        print(f"An error occurred: {e}")
        client_socket.close()

if __name__ == "__main__":
    main()