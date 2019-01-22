# django-file-upload
Note: Configure file upload URL

Working Django framework - 100% complete
Front End  - Connection b/w DB and UI - incomplete

Establish MySQL Connection (After downloading MySQL)

>pip install mysqlclient
>pip install pymysql 
    Change__init__.py
        import pymysql
        pymysql.install_as_MySQLdb()
>pip install cryptography
>python manage.py makemigrations
>python manage.py migrate
>python manage.py runserver

Creating Database using sql command line
   > create DATABASE nameofproject CHARACTER SET UTF8;
    create USER username@localhost IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON nameofproject.* to username@localhost;
    FLUSH PRIVILEGES;


>python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
    adminname
    password

python manage.py runserver

To start mysql server
    >mysql -u username -p
