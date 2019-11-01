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

## Using MailGun service for sending mails
For sending mail you can import send_mail, send_mass_mail from either `django.core.mail` or `mailgun` module. Below are the example for both

> For API Based Mailing import from `mailgun`  
> Note: It only supports *fail_silently* kwargs  
 
```python
    from mailgun import send_mail, send_mass_mail
```

> For SMTP Based Mailing import from `django.core.mail`  
 
```python
    from django.core.mail import send_mail, send_mass_mail
```
```python
    # Sample con
    # send mail to single person
    send_mail(
        'Subject',
        'Body', 
        'from@mail.com', 
        ['to_person1@mail.com'])

    # To send mail to multiple people as CC
    send_mail(
        'Subject',
        'Mail Body',
        'from@example.com',
        ['to_person1@mail.com', 'to_person2@mail.com', ])

    # For sending multiple mails or mails with BCC
    send_mass_mail(
        (
            'Subject',
            'Mail Body',
            'from@example.com',
            ['to_person1@mail.com']
        ),
        (
            'Subject',
            'Mail Body',
            'from@example.com',
            ['to_person3@mail.com', 'to_person2@mail.com', ]
        ),
    )
```
