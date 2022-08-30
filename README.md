# Crud Django

### Este repositório visa criar um Crud usando Docker, Django, Postgres, Redis, Swagger e JWT.

<br>

# Pré-requisitos
### Certifique-se de possuir o docker compose instalado em sua máquina

<br>

# Clone este repositório
$ git clone <https://github.com/jonathanprange/crud_django.git>

<br>

# Acesse a pasta do projeto via terminal e execute o comando 
$ docker-compose up --build

<br>

# Aguarde alguns minutos e terá os seguintes serviços em execução:
- Postgres no endereço localhost:5432
- Redis no endereço localhost:6379
- App Django no endereço localhost:8000

<br>

# Acesse a API de Regions através do seguinte endereço:
- http://localhost:8000/api/schema/swagger-ui/#/

<br>

# Você terá uma interface do Swagger para o crud de Regions, para utilização será necessário estar autenticado. Entre no shell da aplicação com o comando via terminal:
$ docker exec -it <nome_do_container> bash

<br>

# Crie um super usuário com o comando:
$ python manage.py createsuperuser

# Com este usuário que você acabou de criar, retorne a API e execute um POST no seguinte endpoint com os dados de usuário:
- acesse: /api/token 
- selecione try it out 
- preencha as credenciais

<br>

# Você receberá um token de acesso como resposta da requisição.
# Após isso acesse a caixa AUTHORIZE no canto superior direito da API
# e faça login com o token de acesso que você agora possui.
# Após todas estas etapas você está autorizado a realizar todas as requisições disponíveis
# e avaliar todos os serviços utilizados nesta construção.