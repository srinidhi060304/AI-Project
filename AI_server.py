import socket

def process_order(order):
    # Simulate processing the order and generating a token number
    token_number =(hash(','.join(order)) % 100)+1
    return str(token_number)

def start_canteen_owner_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 9999)  # Choose a port for the server

    server_socket.bind(server_address)
    server_socket.listen(1)

    print("Canteen Owner Server is listening for incoming connections...")

    while True:
        connection, client_address = server_socket.accept()
        try:
            data = connection.recv(1024).decode('utf-8')
            if data:
                order = data.split(',')
                print(f"Received order from customer: {order}")

                token = process_order(order)
                connection.sendall(token.encode('utf-8'))
                response="no"
                # Ask if the customer is satisfied with the token
                response = input("Is the returned token okay? (yes/no): ").lower()
                if response == 'yes':
                   break

        finally:
            connection.close()

if __name__ == "__main__":
    start_canteen_owner_server()
