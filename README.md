# DATABASE_PROJECT

Projeto da disciplina de Banco de Dados

---

## 🧩 REQUISITOS PARA RODAR O PROJETO
- Python 3.12 ou superior  
- Banco de Dados MariaDB instalado e configurado  

---

## ⚙️ COMO RODAR O PROJETO

1. **Criar o ambiente virtual**
   ```
   python -m venv venv
   ```

2. **Ativar o ambiente virtual**
   - **Windows:**  
     ```
     ./venv/Scripts/activate
     ```
   - **Linux/Mac:**  
     ```
     source venv/bin/activate
     ```

3. **Instalar o Django (com a venv ativa)**
   ```
   pip install django
   ```

---

## 🗄️ INSTALAÇÃO DO MARIADB

1. Baixe e instale o MariaDB:  
   👉 [https://mariadb.com/downloads/](https://mariadb.com/downloads/)

2. Após a instalação e configuração, verifique se o serviço está rodando:
   ```
   mysql -u root -p
   ```

3. Caso o comando `mysql` não seja reconhecido, adicione o caminho do MariaDB nas variáveis de ambiente do sistema:

   **Windows:**
   ```
   win + r -> sysdm.cpl -> Avançado -> Variáveis de ambiente -> 
   Variáveis do sistema -> PATH -> Novo -> C:\Program Files\MariaDB 11.8\bin
   ```

---

## ⚙️ CONFIGURAÇÃO DO DJANGO

1. Crie um arquivo `.env` na **raiz do projeto** com base no arquivo `.env.example`.  
   Nesse arquivo, adicione as variáveis de ambiente com os dados do seu banco de dados.

2. Antes de rodar o projeto, **ative a venv** e instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Teste a conexão do Django com o banco de dados.

---

## 🚀 EXECUTANDO O PROJETO

Após seguir todos os passos anteriores, rode o servidor de desenvolvimento:
```
python manage.py runserver
```

Endpoint de teste:
```
/teste/
```

---

## 💡 OUTROS COMANDOS IMPORTANTES

- Aplicar migrações:
  ```
  python manage.py migrate
  ```

- Criar superusuário:
  ```
  python manage.py createsuperuser
  ```

---

📝 **Observação:**  
Não modifique as configurações do projeto sem necessidade.  
Certifique-se de seguir os passos na ordem para evitar erros de configuração.
