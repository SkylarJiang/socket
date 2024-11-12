import socket
import sys

# Task 1: Socket initialization
def create_socket():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(10)
    return client_socket

# Task 2: Initiate the connection request
def connect_to_server(client_socket, server_ip, server_port):
    server_address = (server_ip, server_port)
    client_socket.connect(server_address)

# Task 3: Send command to the server
def send_command(client_socket, msg):
    client_socket.sendall(msg.encode('utf-8'))

# Task 4: Receive the message from the server
def handle_response(client_socket):
    try:
        response = client_socket.recv(1024)
        if response:
            response_str = response.decode('utf-8').strip()
            print(f"server: {response_str}")
            return response_str
        else:
            print("No data received, connection might be closed.")
            return ""
    except socket.timeout:
        print("Receive timed out, no data received within the timeout period.")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

# Handle the data input by users in POST and DELETE
def handle_input(client_socket):
    while True:
        user_input = input("client: ")
        send_command(client_socket, user_input)
        if (user_input == '#'): 
            handle_response(client_socket)
            break

# Main function to run the client
def main():
    if len(sys.argv) != 3:
        print("Usage: MessageBoardClient <server_ip> <server_port>")
        sys.exit(1)
    else:
        server_ip = sys.argv[1]
        server_port = int(sys.argv[2])

    client_socket = create_socket()

    try:
        connect_to_server(client_socket, server_ip, server_port)

        while True:
            command = input("client: ").upper()
            send_command(client_socket, command)
            if command == 'POST' or command == 'DELETE':
                handle_input(client_socket)
            elif command == 'GET':
                while True:
                    response = handle_response(client_socket)
                    if response == "#":
                        break
            elif command == 'QUIT':
                response = handle_response(client_socket)
                if response == "OK":
                    # Task 5: Close socket
                    client_socket.close()
                    break
            else:
                handle_response(client_socket)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
        client_socket.close()

if __name__ == "__main__":
    main()