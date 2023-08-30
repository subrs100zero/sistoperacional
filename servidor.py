import socket
import threading
import datetime

def handle_client(client_socket):
    try:
        while True:
            comando = client_socket.recv(1024).decode()
            
            if comando == "/sair":
                print("Cliente desconectado.")
                break
            
            resposta = ""
            if comando == "d":
                resposta = datetime.date.today().strftime("%Y-%m-%d")
            elif comando == "h":
                resposta = datetime.datetime.now().strftime("%H:%M:%S")
            elif comando == "dh":
                resposta = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            else:
                resposta = "Comando inválido."
            
            client_socket.send(resposta.encode())
    
    finally:
        client_socket.close()

def main():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    
    print("Servidor pronto para receber conexões...")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print("Conexão recebida de:", addr)
            
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()
    
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
