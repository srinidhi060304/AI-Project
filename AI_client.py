import socket

def get_customer_order():
    print("Enter the menu items you want (comma-separated):")
    order = input().split(',')
    return order

def connect_to_canteen_owner(order):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 9999)  # Change this to the canteen owner's server address

    try:
        client_socket.connect(server_address)
        message = ','.join(order).encode('utf-8')
        client_socket.sendall(message)

        token = client_socket.recv(1024).decode('utf-8')
        print(f"Token number received: {token}")

    finally:
        client_socket.close()

if __name__ == "__main__":
    customer_order = get_customer_order()
    connect_to_canteen_owner(customer_order)
