🕸️ Workshop de Web Scraping com Selenium & Python

Bem-vinda ao workshop! Este projeto foi configurado para que você não precise se preocupar com a instalação de Drivers, Chrome ou variáveis de ambiente. Usaremos o Docker para garantir que tudo funcione perfeitamente no seu computador.

📋 Pré-requisitos

Você só precisa de uma coisa instalada:

    Docker Desktop (baixe e instale a versão para o seu sistema operacional).

    Atenção: Certifique-se de que o Docker esteja aberto e rodando antes de começar.

🚀 Como começar
1. Baixe o projeto

Faça o download do código e abra a pasta no seu terminal favorito ou no VS Code.
2. Prepare o ambiente

No terminal, dentro da pasta do projeto, digite o seguinte comando:

```
docker compose up -d
```

Este comando vai baixar as imagens necessárias e preparar os "computadores virtuais" (containers) para o nosso código.

3.Abra o browser do container

📺 Como o Selenium está rodando dentro de um container, você não verá uma janela do Chrome pulando na sua tela. Mas você pode assistir ao processo por "dentro" do Docker:

    Abra o seu navegador (Chrome, Edge, Firefox...) e digite: http://localhost:7900

    Clique em Connect.

    Se pedir uma senha, digite: secret

    Pronto! Você verá a tela do Linux do container onde o Chrome está rodando.

4. Rode o código

Agora, para executar o nosso script de raspagem de dados, rode:

```
docker compose run app poetry run python main.py
```

Vá ao browser do container e veja o navegador sendo comandado ao vivo pelo Selenium :)

🛠️ Comandos Úteis

    Para parar tudo: docker-compose down

    Para reinstalar uma biblioteca nova (Poetry): Se você adicionar algo no pyproject.toml, rode: docker-compose build app

📝 O que vamos aprender?

    Como navegar em páginas dinâmicas.

    Como encontrar elementos (botões, inputs, textos).

    Como lidar com esperas implícitas e explícitas.

    Boas práticas para não ser bloqueada.