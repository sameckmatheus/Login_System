# Projeto de Sistema de Login em Python

Este projeto consiste em criar um sistema de login em Python utilizando a biblioteca Tkinter.

## Descrição do Projeto

O sistema de login deve conter os seguintes elementos:

* Um campo para o usuário digitar seu nome de usuário ou e-mail
* Um campo para o usuário digitar sua senha
* Um botão para o usuário fazer login
* Um link para o usuário recuperar sua senha em caso de esquecimento

![Interface do Sistema de Login](images/readme.png)

Ao clicar no botão de login, o programa deve verificar se o nome de usuário ou e-mail e a senha estão corretos. Se estiverem corretos, o programa deve permitir o acesso do usuário a uma área restrita do sistema. Caso contrário, o programa deve exibir uma mensagem de erro e pedir que o usuário tente novamente.

## Bibliotecas Utilizadas

### Tkinter

O Tkinter é uma biblioteca gráfica padrão do Python que permite criar interfaces gráficas de usuário (GUI - Graphical User Interface). Ele oferece diversos widgets, como botões, caixas de texto, rótulos e outros elementos, que podem ser usados para construir interfaces de forma intuitiva e interativa.

### Pillow

O Pillow é uma biblioteca Python para processamento de imagens. Neste projeto, o Pillow é utilizado para exibir a imagem de exemplo na interface gráfica do sistema de login. Além disso, ele pode ser utilizado para redimensionar, cortar, converter e manipular imagens de diversas formas.

### Banco de Dados SQLite3

O SQLite3 é um banco de dados leve e embutido em Python. Neste projeto, o SQLite3 é utilizado para armazenar e gerenciar os dados de login dos usuários. Ele é uma opção adequada para projetos menores e que não requerem um sistema de gerenciamento de banco de dados mais complexo. O SQLite3 é amplamente utilizado por sua simplicidade e facilidade de uso.

## Pré-requisitos

- Python 3 instalado no sistema.

## Como Executar o Projeto

1. Clone o repositório para o seu ambiente local:

   ```
   git clone https://github.com/sameckmatheus/Login_System.git
   ```

2. Acesse o diretório do projeto:

   ```
   cd Login_System
   ```

3. Execute o programa:

   ```
   python login.py
   ```

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir um "issue" ou enviar um "pull request".

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
