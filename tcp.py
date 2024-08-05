import socket

MEU_IP = '192.168.196.238'
MINHA_PORTA = 12345

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

MEU_SERVIDOR = (MEU_IP, MINHA_PORTA)

tcp.bind(MEU_SERVIDOR)

print(f"Servidor iniciado e aguardando conexões em {MEU_IP}:{MINHA_PORTA}")

tcp.listen(1)

conexao, cliente = tcp.accept()

print(f"Conexão estabelecida com {cliente}")

def verificar_numero_primo(numero):
    if numero > 1:
        for i in range(2, numero):
            if (numero % i) == 0:
                return False
        else:
            return True
    else:
        return False

while True:
    data = conexao.recv(1024)
    texto = data.decode('utf-8')
    print(f"Recebido: {texto}")

    teste = f"{texto.lower()}".encode('utf-8')
    conexao.sendall(teste)

conexao.close()

