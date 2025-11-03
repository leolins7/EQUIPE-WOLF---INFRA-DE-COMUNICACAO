import socket

HOST = '127.0.0.1'
PORTA = 65432

estado_atual_dispositivo = "DESLIGADO"

print(f"--- Iniciando Servidor em {HOST}:{PORTA} ---")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORTA))
    s.listen(1)
    print("Servidor pronto. Aguardando uma conexão...")
    
    conn, addr = s.accept()
    
    with conn:
        print(f"Cliente conectado pelo endereço: {addr}")
        
        with conn.makefile('rw', encoding='utf-8', buffering=1) as f:
            
            while True:
                comando_recebido = f.readline().strip()
                
                if not comando_recebido:
                    break
                    
                print(f"Cliente enviou: {comando_recebido}")

                if comando_recebido == "LER_STATUS":
                    print(f"Enviando estado: {estado_atual_dispositivo}")
                    f.write(f"{estado_atual_dispositivo}\n")
                
                else:
                    print("Comando nao reconhecido.")
                    f.write("ERRO: Comando nao reconhecido\n")

        print(f"Cliente {addr} desconectou.")

print("--- Servidor finalizado. ---")