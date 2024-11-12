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
        print(66)
        response = client_socket.recv(1024)
        print(55555555)
        if response:
            response_str = response.decode('utf-8').strip()
            print(f"Server response: {response_str}")  # 打印接收到的响应
            return response_str
        else:
            print("No data received, connection might be closed.")
            return ""
    except socket.timeout:
        print("Receive timed out, no data received within the timeout period.")
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
            user_input = input("")
            send_command(client_socket, "", user_input)
    except KeyboardInterrupt:
        print("\nExiting...")


# Main function to run the client
def main():
    if len(sys.argv) != 3:
        print("Usage: MessageBoardClient <server_ip> <server_port>")
        sys.exit(1)

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])

    client_socket = create_socket()
    connect_to_server(client_socket, server_ip, server_port)

    while True:
        try:
            command = input("").upper()
            if command == 'POST':
                handle_post(client_socket)
            elif command == 'GET':
                send_command(client_socket, "GET", "")
                response = handle_response(client_socket)
                while True:
                    response = handle_response(client_socket)
                    if response == "END":
                        break
            elif command == 'QUIT':
                send_command(client_socket, "QUIT", "")
                response = handle_response(client_socket)
                print(response)
                if response == "OK":
                    close_socket(client_socket)
                    break
            else:
                print("ERROR - Command not understood2")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()