import datetime
import random
import socket
import string
import threading


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
            romanos = converter_int_para_romanos(int(parte1))
            inteiro = converter_romanos_para_int(parte2)

            date = datetime.datetime.now()

            conn.sendall(
                f"Recebido: {data}, em: {date}, Romanos para int: {inteiro}, Inteiros para romano: {romanos}"
                .encode('utf-8') + fim)
        elif parte0 == "texto":
            texto = gerar_texto_aleatorio(int(parte1), int(parte2))

            date = datetime.datetime.now()

            conn.sendall(
                f"Recebido: {data}, em: {date}, Texto aleatório: {texto}"
                .encode('utf-8') + fim)

    except:
        conn.sendall("Erro ao converter".encode('utf-8') + fim)


def converter_romanos_para_int(romano):
    romano = romano.upper()

    romanos = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    numero = 0
    anterior = 0

    for letra in romano:
        atual = romanos[letra]

        if anterior < atual:
            numero -= 2 * anterior

        numero += atual
        anterior = atual

    return numero


def gerar_texto_aleatorio(numero_caracteres, numero_palavras):
    texto = ""
    for i in range(numero_palavras):
        for j in range(numero_caracteres):
            texto += random.choice(string.ascii_letters)
        texto += " "
    return texto


def converter_int_para_romanos(numero):
    if numero < 1 or numero > 3999:
        return "Número inválido"
    else:
        romanos = ""
        while numero >= 1000:
            romanos += "M"
            numero -= 1000
        if numero >= 900:
            romanos += "CM"
            numero -= 900
        if numero >= 500:
            romanos += "D"
            numero -= 500
        if numero >= 400:
            romanos += "CD"
            numero -= 400
        while numero >= 100:
            romanos += "C"
            numero -= 100
        if numero >= 90:
            romanos += "XC"
            numero -= 90
        if numero >= 50:
            romanos += "L"
            numero -= 50
        if numero >= 40:
            romanos += "XL"
            numero -= 40
        while numero >= 10:
            romanos += "X"
            numero -= 10
        if numero >= 9:
            romanos += "IX"
            numero -= 9
        if numero >= 5:
            romanos += "V"
            numero -= 5
        if numero >= 4:
            romanos += "IV"
            numero -= 4
        while numero >= 1:
            romanos += "I"
            numero -= 1
        return romanos


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
