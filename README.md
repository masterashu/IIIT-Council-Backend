# IIITS Council Website Backend

## Cloning the project  
* Run command `git clone https://github.com/Gradient-IIITS/IIIT-Council-Backend.git` and movie in the repository
* Create a virtual environment `env` in the repository (use virtualenv, etc)
* Activate virtual environment  
    >    Windows:  ```.\env\Scripts\activate```  
    >    Ubuntu/Linux: ```source env/bin/activate```   
    
    Install the requirements  
    ```bash
    pip install -r requirements.txt
    ```
    
* [Setup postgreSQL database](#setup-postgresql)
* Run `python manage.py check` to check any errors
* Run `python manage.py makemigrations` to make the migrations
* un `python manage.py migrate` to update the database schema


## Setup postgreSQL
1. Install [postgreSQL](https://www.postgresql.org/download/) and configure it. (Set postgres password, **Note down the PORT**, etc).  

2. Start postgreSQL shell and create a new user `user1` .   
    ```sql
    CREATE USER user1 WITH PASSWORD 'password';
    ```

1. Edit properties to optimize queries (optional)
    ```sql
    ALTER ROLE user1 SET client_encoding TO 'utf8';
    ALTER ROLE user1 SET default_transaction_isolation TO 'read committed';
    ALTER ROLE user1 SET timezone TO 'UTC';
    ```

1. Create a new database named `iiits_council` and give `user1` the access using the following command  
   ```sql
    CREATE DATABASE iiits_council
        WITH 
        OWNER = user1
        ENCODING = 'UTF8'
        CONNECTION LIMIT = -1;
    
    GRANT ALL ON DATABASE iiits_council TO user1;
   ```


