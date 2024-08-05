import datetime
import socket
import threading

import utils


def handle_client(conn, addr):
    print(f"Conexão estabelecida com {addr}")
    while True:
        data = conn.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"Recebido: {data}")

        enviar_mensagem(conn, data)

    conn.close()


def enviar_mensagem(conn, data):
    fim = "\n".encode('utf-8')
    try:
        partes = data.split(",")

        parte0 = partes[0]
        parte1 = partes[1].replace(" ", "")
        parte2 = partes[2].replace(" ", "")

        if parte0 == "romanos":
            romanos = utils.converter_int_para_romanos(int(parte1))
            inteiro = utils.converter_romanos_para_int(parte2)

            date = datetime.datetime.now()

            conn.sendall(
                f"Recebido: {data}, em: {date}, Romanos para int: {inteiro}, Inteiros para romano: {romanos}"
                .encode('utf-8') + fim)
        elif parte0 == "texto":
            texto = utils.gerar_texto_aleatorio(int(parte1), int(parte2))

            date = datetime.datetime.now()

            conn.sendall(
                f"Recebido: {data}, em: {date}, Texto aleatório: {texto}"
                .encode('utf-8') + fim)

    except:
        conn.sendall("Erro ao converter".encode('utf-8') + fim)


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('192.168.1.49', 12345))
    server.listen(5)
    print("Servidor iniciado e aguardando conexões...")

    while True:
        conn, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()


if __name__ == "__main__":
    start_server()
