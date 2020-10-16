# Gerador de Dataset para Processamento de Linguagem Natural

![](https://img.shields.io/badge/Python-3.8.5-green)
![](https://img.shields.io/badge/Tweepy-3.9.0-orange)
![](https://img.shields.io/badge/NLTK-3.5-red)
![](https://img.shields.io/badge/Unidecode-1.1.1-yellow)

## Descrição
Este repositório tem o intuito de gerar um dataset simples, com um conjunto de frases extraídas do Twitter, por meio da API disponibilizada pelo próprio Twitter.

## Módulos

- **main.py**\
  É responsável por comandar todos os outros módulos.

- **call_stream.py**\
  Unicamente invocado para fazer as chamadas de ativação da stream.

- **stream.py**\
  O módulo é ativado e tem uma função call back que retorna todo tweet que chega na pesquisa.

- **auth.py**\
  Unicamente para autenticar as chaves da API.

- **aux_mod.py**\
  São funções que auxiliam módulos maiores, retornam listas de pontuação, stopwords e strings tokenizadas.

- **twitter_data_cleaner.py**\
  Esse módulo remove todas as informações que não são utilizados para a analise:
    * remove_stopwords
    * remove_user
    * remove_URL
    * remove_emoji
    * remove_hashtag
    * remove_punct
    
- **config.env**\
  As chaves de acesso da API do twitter e a palavra chave a ser pesquisada, podem ser acessadas por meio desse arquivo.
  
  **O fluxo de software se dá por essa primeira imagem:**
![image](https://drive.google.com/uc?export=view&id=1LgeNobP9HVsbWzo8nU0OYU376jcq3WGl)
![image](https://drive.google.com/uc?export=view&id=15bgr66RpwSD2ZFTgzWEY4XWDVIbodgcu)

## Twitter API
Para poder utilizar a API vocÊ precisa das chaves que são disponibilizadas a partir do momento que você cria o projeto.

![image](https://drive.google.com/uc?export=view&id=1VoVev9ovz37wuja_ST0UdN7Z9bmYu3yT)
![image](https://drive.google.com/uc?export=view&id=1FySb1D-5IEjZ-S0HjAOlCnVwYbn--GZM)
![image](https://drive.google.com/uc?export=view&id=1wB4zoOH9YXEfBaZr3YvjqS1fDtDvMRuA)

## I/O
- **Input**
  No arquivo config.env é possível editar a palavra que quer basear seu dataset em WORDKEY.
  As outras variáveis são chaves que são disponibilizadas pela API do Twitter, e são necessárias no processo de autenticação.
  
  `WORDKEY=`
  `CONSUMER_KEY=`
  `CONSUMER_SECRET_KEY=`
  `ACESS_TOKEN= ACESS_SECRET_TOKEN=` 

- **Output**
  O arquivo cria um arquivo CSV e popula o arquivo com os tweets que vão chegando, até que sofra uma interrupção do teclado (Ctrl+C).
  
  1 | tweet exemplo 1 
  --------------------
  2 | tweet exemplo 2
  --------------------
  
## Contribua com o repositório :)

Qualquer tipo de contribuição é bem vinda, desde dicas até pull requests. 

`git clone https://github.com/otaviodantas/NLP-generator-dataset.git`
