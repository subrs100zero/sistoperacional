import socket

def main():
    host = "127.0.0.1"
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        while True:
            comando = input("Digite o comando (d/h/dh) ou /sair para sair: ")
            
            if comando == "/sair":
                client_socket.send(comando.encode())
                print("Conexão encerrada.")
                break
            
            if comando not in ["d", "h", "dh"]:
                print("Comando inválido. Digite d, h, dh ou /sair.")
                continue
            
            client_socket.send(comando.encode())
            resposta = client_socket.recv(1024).decode()
            print("Resposta do servidor:", resposta)
    
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
