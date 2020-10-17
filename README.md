## Alx-accessor

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/53823e9fcc0940c18bed6f5898788147)](https://app.codacy.com/gh/Paulwamaria/alxlaunchepadaccessback?utm_source=github.com&utm_medium=referral&utm_content=Paulwamaria/alxlaunchepadaccessback&utm_campaign=Badge_Grade_Settings)

Alx-accessor is the backend API for an information management system.

### Tecnologies

- Python
- Django
- Djoser
- Postgresql
- Bootstrap
- Html

### Requirements

To run the application locally, you need to meet the following requirements:

- Python==3.8
- Pip
- Postgresql

### Set-up

1. Clone the application or download the zip package from this link:
   [Github Repository](https://github.com/Paulwamaria/alxlaunchepadaccessback.git)

1. Navigate to the root folder

```
$ cd alxlaunchepadaccessback
```

3. Create a virtual environment. (You need to have virtualenv installed)
4. Activate the virtual environment.

```
$ python -m venv virtual

$ source virtual/bin/activate

```

5. Install the necessary requirements as per the requirements.txt file

```
$ pip install -r requirements.txt
```

6. Create a database

```
# CREATE DATABASE "database-name";
```

6. Create a .env file and add the following variables

```
SECRET_KEY='your secret key'
DEBUG=True
DB_NAME="your database name"
DB_USER="your database user name"
DB_PASSWORD="your database password"
DB_HOST="localhost"
PORT="5432"
ALLOWED_HOSTS=[*]
MODE="dev"
EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST="smtp.gmail.com"
EMAIL_PORT="587"
EMAIL_HOST_USER="your email"
EMAIL_HOST_PASSWORD="your email app password"
EMAIL_USE_TLS=True
DISABLE_COLLECTSTATIC=1
```

8. Make migrations on the database you have just created

```python
$ python manage.py migrate
```

9. Run the server

```python
$ python manage.py runserver
```

10. Open your browser and navigate to the localhost on port 8000 and you are good to go.

### Developer

[Paul Wamaria](https://paulwamaria.netlify.app)

### Acknowledgement

This application was an asignment by [alx](https://www.alx.app/)
