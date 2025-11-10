


---

# 🐺 EQUIPE WOLF — INFRA DE COMUNICAÇÃO

## 👥 Integrantes

* **João Eduardo Monteiro Cavalcanti**
* **Jonas de Lima Neto**
* **Leonardo Felipe Demétrio Lins Nascimento**

---

## 💡 Projeto: Emulador de Dispositivo I/O Simples (Simulação Profinet)

### 🎯 1. Tema do Projeto

Desenvolvimento de um sistema **Cliente/Servidor** para simular a comunicação entre um **controlador industrial (Profinet)** e um **dispositivo de campo (Dispositivo I/O)**, utilizando protocolos de comunicação simples baseados em **TCP/IP**.

---

### 🧩 2. Escopo da Solução

O objetivo é criar **duas aplicações em Python** que se comunicam pela rede local:

#### 🖥️ Servidor (`servidor.py`) — *Dispositivo I/O Simples*

* Simula um dispositivo de campo (como um **sensor** ou **atuador**).
* Fica “escutando” em uma porta específica da rede (via **socket TCP**).
* Utiliza **threading** para aceitar múltiplos clientes simultaneamente.
* Mantém um **estado interno simulado**, incluindo:

  * Status (ligado/desligado)
  * Temperatura
  * Código de erro
* Responde a **comandos enviados pelo cliente** para leitura e alteração de estado.

#### 💻 Cliente (`cliente.py`) — *Controlador Simulado*

* Simula o **controlador industrial (CLP/Profinet)**.
* Inicia a conexão com o servidor.
* Envia comandos definidos para ler e escrever dados no dispositivo.
* Recebe e exibe as respostas do servidor em tempo real.

---

### ⚙️ 3. Tecnologias Utilizadas

| Categoria                  | Tecnologia            |
| -------------------------- | --------------------- |
| **Linguagem**              | Python 3              |
| **Bibliotecas Principais** | `socket`, `threading` |

---

### 🚀 4. Como Executar o Projeto

Para testar a simulação, abra **dois ou mais terminais** na pasta do projeto.

#### 🧠 Passo 1: Iniciar o Servidor

No **primeiro terminal**, execute o servidor:

```bash
python servidor.py
```

Saída esperada:

```
--- Iniciando Servidor em 127.0.0.1:65432 ---
Servidor pronto. Aguardando conexões...
```

#### ⚡ Passo 2: Iniciar o Cliente

No **segundo terminal**, execute o cliente:

```bash
python cliente.py
```

Saída esperada:

```
--- Iniciando Cliente ---
Tentando conectar ao Servidor em 127.0.0.1:65432...
Conectado ao Servidor!
```

---

### 🧾 5. Comandos Disponíveis

Após a conexão, o cliente exibirá o menu de comandos:

```
--- Comandos Disponíveis ---
  LER_STATUS
  SET_ESTADO LIGADO / SET_ESTADO DESLIGADO
  LER_TEMPERATURA
  LER_ERRO
  SET_ERRO [numero]  (ex: SET_ERRO 404)
  LER_COMPLETO
  SAIR
```

#### 🛠️ Descrição dos Comandos

| Comando                         | Função                                                                |
| ------------------------------- | --------------------------------------------------------------------- |
| `LER_STATUS`                    | Consulta o status atual do dispositivo (LIGADO/DESLIGADO).            |
| `SET_ESTADO [LIGADO/DESLIGADO]` | Altera o status principal do dispositivo.                             |
| `LER_TEMPERATURA`               | Consulta a temperatura simulada.                                      |
| `LER_ERRO`                      | Mostra o código de erro atual.                                        |
| `SET_ERRO [numero]`             | Define um novo código de erro (ex: `SET_ERRO 101`).                   |
| `LER_COMPLETO`                  | Solicita o estado completo do dispositivo (em formato de dicionário). |
| `SAIR`                          | Encerra a conexão do cliente.                                         |

---

### 🧪 6. Exemplo de Uso (Protótipo Funcional)

#### 🖼️ Exemplo 1 — Comunicação entre Cliente e Servidor

O servidor (terminal superior) recebe comandos do cliente (terminal inferior) e responde conforme o protocolo definido:

<img width="851" height="418" alt="image" src="https://github.com/user-attachments/assets/6996d27c-af26-417a-8785-9e86e70146ad" />

<img width="905" height="576" alt="image" src="https://github.com/user-attachments/assets/87a45903-eccc-4a08-b6b9-44c9f8323412" />



#### 🖼️ Exemplo 2 — Comando Inválido

Quando o cliente envia um comando não reconhecido, o servidor retorna uma mensagem de erro:

<img width="441" height="80" alt="image" src="https://github.com/user-attachments/assets/018990c3-922c-4284-8692-df1339ba8d32" />


---

### 📘 7. Conclusão

O projeto **EQUIPE WOLF — Infra de Comunicação** simula, de forma didática, o comportamento básico de um **sistema industrial com comunicação Profinet**, permitindo compreender o funcionamento entre um **controlador (CLP)** e um **dispositivo I/O**, com ênfase na **comunicação via TCP/IP** e no **uso de threads para conexões simultâneas**.

---
