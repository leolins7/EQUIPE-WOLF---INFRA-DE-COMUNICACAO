import socket
import threading

HOST = '127.0.0.1'
PORTA = 65432

estado_dispositivo = {
    'status': 'DESLIGADO',
    'temperatura': 25.5,
    'codigo_erro': 0
}
estado_lock = threading.Lock()

def tratar_cliente(conn, addr):
    global estado_dispositivo
    
    print(f"Cliente {addr} conectou. (Thread iniciada)")
    
    with conn:
        with conn.makefile('rw', encoding='utf-8', buffering=1) as f:
            
            while True:
                try:
                    comando_recebido = f.readline().strip()
                    
                    if not comando_recebido:
                        break
                        
                    print(f"Cliente {addr} enviou: {comando_recebido}")

                    if comando_recebido == "LER_STATUS":
                        with estado_lock:
                            estado_para_enviar = estado_dispositivo['status']
                        f.write(f"{estado_para_enviar}\n")
                    
                    elif comando_recebido.startswith("SET_ESTADO"):
                        partes = comando_recebido.split(maxsplit=1)
                        if len(partes) == 2:
                            novo_estado = partes[1].upper()
                            if novo_estado == "LIGADO" or novo_estado == "DESLIGADO":
                                with estado_lock:
                                    estado_dispositivo['status'] = novo_estado
                                f.write(f"OK: Status alterado para {novo_estado}\n")
                            else:
                                f.write(f"ERRO: Estado '{novo_estado}' inválido. Use LIGADO ou DESLIGADO.\n")
                        else:
                            f.write("ERRO: Comando SET_ESTADO mal formatado.\n")
                    
                    elif comando_recebido == "LER_TEMPERATURA":
                        with estado_lock:
                            temp = estado_dispositivo['temperatura']
                        f.write(f"{temp}\n")

                    elif comando_recebido == "LER_ERRO":
                        with estado_lock:
                            erro = estado_dispositivo['codigo_erro']
                        f.write(f"{erro}\n")
                    
                    elif comando_recebido.startswith("SET_ERRO"):
                        partes = comando_recebido.split(maxsplit=1)
                        if len(partes) == 2:
                            try:
                                novo_erro = int(partes[1])
                                with estado_lock:
                                    estado_dispositivo['codigo_erro'] = novo_erro
                                f.write(f"OK: Codigo de erro alterado para {novo_erro}\n")
                            except ValueError:
                                f.write("ERRO: Codigo de erro deve ser um número inteiro.\n")
                        else:
                            f.write("ERRO: Comando SET_ERRO mal formatado. Use: SET_ERRO [numero]\n")
                    
                    elif comando_recebido == "LER_COMPLETO":
                        with estado_lock:
                            estado_str = str(estado_dispositivo)
                        f.write(f"{estado_str}\n")

                    else:
                        f.write("ERRO: Comando nao reconhecido\n")
                
                except ConnectionResetError:
                    break
                except Exception as e:
                    print(f"Erro na thread {addr}: {e}")
                    break

    print(f"Cliente {addr} desconectou. (Thread finalizada)")

print(f"--- Iniciando Servidor em {HOST}:{PORTA} ---")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORTA))
    s.listen(5)
    print("Servidor pronto. Aguardando conexões...")
    
    while True:
        try:
            conn, addr = s.accept()
            
            thread_cliente = threading.Thread(target=tratar_cliente, args=(conn, addr))
            thread_cliente.start()
        
        except KeyboardInterrupt:
            print("\n--- Servidor sendo finalizado... ---")
            break
        except Exception as e:
            print(f"Erro no loop principal do servidor: {e}")

print("--- Servidor finalizado. ---")