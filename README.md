# 📡 Trabalho gRPC
Bem-vindo! Esse repositório contém o projeto final da disciplina de Sistemas Distribuídos bem como as intruções para reprodução e execução do código.

## 📚 Conteúdo do Repositório 
- Cliente implementado em Node.JS
- Servidor implementado em Python
- Arquivos de definição da comunicação gRPC
- Arquivo teste.py que é uma versão inicial do que viria a ser o servidor, ele recebe como input o nome de uma imagem .jpg e transforma ela de acordo com as preferências do usuário

## 📄 Pré-Requisitos (para o vscode)
- Git
- Python
- Node.JS
- Extensão: vscode-proto3
- Bibliotecas para o servidor em Python:
    - Pillow (para maniplação de imagens)
    - grpcio e grpcio-tools (para o gRPC)
    - protobuf (para lidar com os arquivos .proto)
- Bibliotecas para o cliente em Node.JS:
    - grpc/grpc-js e grpc/proto-loader

- **IMPORTANTE:** Após clonar o repositório é necessário definir o IP do servidor de acordo com o IP da sua rede

## 🚶🏻‍♂️ Passo a Passo para Criação de Uma Comunicação gRPC
- Instalar Python e Node.JS, bem como as bibliotecas e extensões previamente mencionadas.
    - As bibliotecas podem ser instaladas com os comandos abaixo:
        - Python:
        ``` pip install pillow grpcio grpcio-tools protobuf ``` obs: a biblioteca pillow define as funções para manipulações de imagens, se seu projeto não envolver manipulação de imagens não precisa adiciona-la
        - Node.JS:
        ``` npm init -y ```
        ``` npm install @grpc/grpc-js @grpc/proto-loader ```

- Criar o arquivo .proto e nele definir como funcionará o serviço e qual tipo de dado será transmitido dentro de cada parte do serviço (Request e Response).
- Rodar o código abaixo para gerar os arquivos grpc:
    ``` python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. image_service.proto ``` -> Esse código gera 2 arquivos, um terminado em _pb2 e outro termina em _pb2_grpc. Esse módulos contêm classes e funções necessárias para a definição das mensagens e serviços gRPC que foram especificados no arquivo .proto
- Implementar o servidor gRPC em Python em um arquivo server.py
- Implementar o cliente gRPC em Node.JS
- Após implementar o servidor e o cliente e definir o endereço de IP (precisa ser o mesmo tanto no servidor quanto no cliente) e porta corretamente, basta rodar os seguintes códigos:
    ``` python server.py ``` em um terminal ou em uma máquina
    ``` node client.js ``` em um outro terminal ou em uma outra máquina
- Parabéns, você acaba de implementar uma comunicação gRPC

## 🔁 Feedbacks
Todo feedback é muito bem-vindo, sinta-se a vontade para complementar o conteúdo aqui desenvolvido!