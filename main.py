import socket
import threading

def handle_client(conn, addr):
    print(f"Conexão estabelecida com {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        texto = data.decode('utf-8')
        print(f"Recebido: {texto}")
        conn.sendall(data)
    conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(5)
    print("Servidor iniciado e aguardando conexões...")

    while True:
        conn, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

if __name__ == "__main__":
    start_server()