# database_project
PROJETO DA DISCIPLINAS DE BANCO DE DADOS 
# REQUISITOS PARA RODAR O PROJETO
python 3.12 ou superior
# COMO RODAR O PROJETO
criar a venv com: python -m venv venv 
ativar a venv: ./venv/Scripts/activate ou para linux source venv/bin/activate
instalar o django com a venv ativa: pip install django
# INSTALEM O BANCO DE DADOS MARIADB
https://mariadb.com/downloads/ 
após instalação e configuração verifiquem se o serviço está rodando 
mysql -u root -p
se não reconhecer  o comando mysql vocês precisam adicionar mysql nas variaveis de ambiente PATH do sistema
win + r -> sysdm.cpl -> avançado -> variaveis de ambiente -> variaveis do sistema -> PATH -> novo -> C:\Program Files\MariaDB 11.8\bin
# SETTINGS CONFIG
criem um arquivo .env na raiz do projeto no formato do .env.example e nele coloquem as variáveis de ambiente do banco de dados de vocês para rodar o projeto. Depois teste para ver se o django está conseguindo se conectar ao banco de dados.
LEMBRE DE ANTES DE RODAR O PROJETO DE ATIVAR A VENV E INSTALAR AS DEPENDENCIAS DO PROJETO COM O COMANDO: pip install -r requirements.txt
