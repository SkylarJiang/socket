This is a simple client for interacting with a message board server. The client allows you to POST, GET, and DELETE messages, as well as QUIT the session.

How to Run the Client:

1. Prerequisites:
   - Python 3.x must be installed.
   - The server should be running and accessible at the specified IP and port.

2. Running the Client:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the client script and this README file.
   - Run the client using the following command (Replace <server_ip> with the IP address of the server and <server_port> with the port number):
      python ./MessageBoardClient.py <server_ip> <server_port>
   
3. Using the Client:
   - After running the client, you will be prompted to enter commands. Available commands are:
     - POST: To start posting messages to the server. Type messages followed by '#' to finish posting.
     - GET: To retrieve messages from the server. Messages will be displayed until a '#' is received.
     - DELETE: To delete messages from the server. Type message IDs followed by '#' to finish deleting.
     - QUIT: To quit the session and close the connection to the server.