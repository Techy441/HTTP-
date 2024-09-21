import socket  # noqa: F401
# Parse the request data to extract the HTTP method, path and
def parse_request (request_data):
    lines = request_data.split('\r\n')
    start_line = lines [0] # The start line is the first line o
    method, path, version = start_line.split(''
)
    return method, path, version
1
# Returns the HTTP response for a given path
def get_response (path):
    # Mapping paths to their responses
    responses = {"/": "HTTP/1.1 200 OK\r\n\r\n",}
    # Default response if path not found
    default_response = "HTTP/1.1 404 Not Found\r\n\r\n"
    return responses. get (path, default_response)

def handle_request(client_socket):
    # Read data from the client
    client_socket.recv(1024) # type: ignore # Reading a bit of data
    # Send a 200 OK response
    response = "HTTP/1.1 200 OK\r\n\r\n"
    client_socket.send(response.encode ()) 
def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    server_socket.accept()[0].sendall(b"HTTP/1.1 200 OK\r\n\r\n")
    
    try:
        while True:
            # Wait for a connection
            print("Waiting for a connection...")
            client_socket, addr = server_socket.accept() 
            print(f"Connection from {addr} has been established")
            # Handle the client's request
            handle_request (client_socket)

            # Close the connection to the client
            client_socket.close()
    except KeyboardInterrupt:
                  print("InServer is shutting down.")
    finally:
                  # Clean up the server socket
                  server_socket.close()
                  print("Server has been shut down.")
    

if __name__ == "__main__":
    main()



