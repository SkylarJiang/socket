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
def send_command(client_socket, command, data):
    full_command = f"{command} {data}\n"
    client_socket.sendall(full_command.encode('utf-8'))

# Task 4: Handle server response
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
        # print("Receive timed out, no data received within the timeout period.")
        return ""
    except UnicodeDecodeError:
        print("Received data is not valid UTF-8 encoded.")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

# Task 5: Close socket
def close_socket(client_socket):
    client_socket.close()

def handle_post(client_socket):
    try:
        send_command(client_socket, "POST", "")
        while True:
            user_input = input("client: ")

            if (user_input == '#'): 
                send_command(client_socket, "", user_input + '\n')
                handle_response(client_socket)
                break
            else:
                send_command(client_socket, "", user_input)
    except KeyboardInterrupt:
        print("\nExiting...")

def handle_delete(client_socket):
    try:
        send_command(client_socket, "DELETE", "")
        while True:
            user_input = input("client: ")

            if (user_input == '#'): 
                send_command(client_socket, "", user_input + '\n')
                handle_response(client_socket)
                break
            else:
                send_command(client_socket, "", user_input)
    except KeyboardInterrupt:
        print("\nExiting...")

# Main function to run the client
def main():
    if len(sys.argv) != 3:
        # print("Usage: MessageBoardClient <server_ip> <server_port>")
        # sys.exit(1)
        server_ip = '127.0.0.1'
        server_port = 16111
    else:
        server_ip = sys.argv[1]
        server_port = int(sys.argv[2])

    client_socket = create_socket()
    connect_to_server(client_socket, server_ip, server_port)

    while True:
        try:
            command = input("client: ").upper()
            if command == 'POST':
                handle_post(client_socket)
            elif command == 'GET':
                send_command(client_socket, "GET", "")
                while True:
                    response = handle_response(client_socket)
                    if response == "#":
                        break
            elif command == 'DELETE':
                handle_delete(client_socket)
            elif command == 'QUIT':
                send_command(client_socket, "QUIT", "")
                response = handle_response(client_socket)
                if response == "OK":
                    close_socket(client_socket)
                    break
            else:
                print("ERROR - Command not understood")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()