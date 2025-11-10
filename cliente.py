import socket
import sys

HOST = '127.0.0.1'
PORTA = 65432

print("--- Iniciando Cliente ---")
print(f"Tentando conectar ao Servidor em {HOST}:{PORTA}...")

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        s.connect((HOST, PORTA))
        print("Conectado ao Servidor!")
        print("\nDigite seus comandos. Exemplos:")
        print("  LER_STATUS")
        print("  SET_ESTADO LIGADO")
        print("  LER_TEMPERATURA")
        print("  LER_ERRO")
        print("  SET_ERRO 404")
        print("  LER_COMPLETO")
        print("  Digite 'SAIR' para fechar a conexão.\n")

        with s.makefile('rw', encoding='utf-8', buffering=1) as f:
            
            while True:
                comando_para_enviar = input("Comando> ")

                if not comando_para_enviar or comando_para_enviar.upper() == 'SAIR':
                    print("Encerrando conexão...")
                    break
                
                f.write(f"{comando_para_enviar}\n")
                
                resposta_servidor = f.readline().strip()
                
                if not resposta_servidor:
                    print("Servidor fechou a conexão inesperadamente.")
                    break
                    
                print(f"Servidor: {resposta_servidor}")

except ConnectionRefusedError:
    print(f"ERRO: Não foi possível conectar ao servidor em {HOST}:{PORTA}.")
    print("Verifique se o script 'servidor.py' está em execução.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

print("--- Cliente finalizado. ---")