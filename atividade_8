import threading
import random
import time

caixas_semaforo = threading.Semaphore(3)

tamanho_fila = 30

def atender_cliente(cliente_id):
    tempo_atendimento = random.randint(3, 10)
    print(f'Cliente {cliente_id} chegou e vai ser atendido em {tempo_atendimento} segundos.')

    time.sleep(tempo_atendimento)

    with caixas_semaforo:
        print(f'Cliente {cliente_id} está sendo atendido.')

def chegada_clientes():
    for cliente_id in range(1, tamanho_fila + 1):
        cliente_thread = threading.Thread(target=atender_cliente, args=(cliente_id,))
        cliente_thread.start()

        tempo_chegada = random.uniform(0.5, 2)
        time.sleep(tempo_chegada)

if __name__ == "__main__":
    print("Simulação da fila de atendimento de um banco com 3 caixas")

    chegada_thread = threading.Thread(target=chegada_clientes)
    chegada_thread.start()

    chegada_thread.join()

    print("Todos os clientes foram atendidos.")
