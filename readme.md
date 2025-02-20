Sistema que consome os dados do Sistema1
https://github.com/95Caique/sistema_1

O intuido é cadastrar os usuários apenas uma vez e importa-los nos demais sistemas.

1 - Para executar, clone o repostório

2 - Navegue até a pasta do projeto com o comando cd sistema2

3 - Crie seu ambiente virtual (venv) para instalar os pacotes: 

Linux - python3 -m venv venv Ative com: source venv/bin/activate

Windows - python3 -m venv venv ative com: venv\Scripts\activate se estiver assim (venv) está ativada, pode instalar os 
requirements nesse ambiente criado

4 - Instale os requirements com a venv ativa (venv) com o comando pip install -r requirements.txt

5 - Execute o comando python manage.py makemigrations e python manage.py migrate para executar as migrações e popular 
o banco de dados, em seguida execute com python manage.py runserver 0.0.0.0:8011. Pois o Sistema1 é executado na porta 8000,
o Sistema2 é executado na 8011.

Com os dois sistemas rodando (Sistema 1 e Sistema 2), no sistema2 navegue até a pasta importador 
e execute o comando import.py e retornará os dados da pessoa selecionada.  Ou clique com o botão esquerdo do mouse
em impor.py e selecione Run import.py.