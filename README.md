# EQUIPE-WOLF---INFRA-DE-COMUN.

# INTEGRANTES: 

* João Eduardo Monteiro Cavalcanti

* Jonas de Lima Neto

* Leonardo Felipe Demétrio Lins Nascimento


# Projeto: Emulador de Dispositivo I/O Simples (Simulação Profinet)

## 1. Tema do Projeto

Desenvolvimento de um sistema Cliente/Servidor para simular a comunicação entre um controlador industrial (Profinet) e um dispositivo de campo (Dispositivo I/O), utilizando protocolos de comunicação simples baseados em TCP/IP.

## 2. Escopo da Solução

O objetivo é criar duas aplicações em Python que se comunicam pela rede:

* **O Servidor (Dispositivo I/O Simples):**
    * Esta aplicação simula um dispositivo de campo (como um sensor ou atuador).
    * Ela ficará "escutando" em uma porta de rede específica (usando `socket` TCP).
    * Manterá um estado interno simulado (ex: "LIGADO" ou "DESLIGADO").
    * Responderá a comandos simples enviados pelo Cliente para ler ou alterar esse estado.

* **O Cliente (Controlador Simulado):**
    * Esta aplicação simula o controlador (CLP/Controlador Profinet).
    * Ela irá iniciar a conexão com o Servidor.
    * Enviará comandos definidos, como "LER_STATUS" (para ler o estado) e "SET_ESTADO [novo_estado]" (para mudar o estado simulado do dispositivo I/O).
    * Receberá e exibirá as respostas do Servidor.

## 3. Tecnologias e Bibliotecas

* **Linguagem de Programação:** Python 3
* **Biblioteca Principal:** `socket` (biblioteca nativa do Python para comunicação em rede via TCP/IP). Não serão necessárias bibliotecas externas para a funcionalidade principal.

## 4. Divisão de Tarefas (Cronograma)

Este planejamento segue o cronograma de 4 semanas:

* **Semana 1: Planejamento e Configuração**
    * **Entrega:** Documento de Planejamento Inicial (este documento).
    * **Marco:** Ambiente Python configurado e código inicial (esqueleto) do **Servidor TCP** (Possibilidade 1) pronto, capaz de aceitar uma conexão.

* **Semana 2: Desenvolvimento Básico**
    * **Entrega:** Protótipo funcional do Servidor (Possibilidade 1).
    * **Marco:** Servidor com a funcionalidade de Rede *Core* implementada: capaz de manter o estado ("LIGADO"/"DESLIGADO") e responder a um comando básico de leitura (ex: "LER_STATUS").

* **Semana 3: Refinamento e Interface (Cliente)**
    * **Entrega:** Aplicação completa com interface básica.
    * **Marco:** Desenvolvimento do **Cliente (Possibilidade 2)**, capaz de se conectar ao servidor e enviar comandos de leitura e escrita. Tratamento de erros básicos implementado.

* **Semana 4: Documentação e Preparação**
    * **Entrega:** Versão final do código (Cliente e Servidor), Documentação (README finalizado) e Roteiro da Apresentação.
    * **Marco:** Projeto 100% finalizado, documentado e pronto para a apresentação.
