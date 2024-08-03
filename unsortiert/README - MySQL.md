# Django MySQL Tutorial

## Features
** Auf dieser Beispielseite werde ich folgende Themen behandeln: **

### Installation / Konfiguration
- Python
- Visual Code
- Virtuelle Umgebungen
- Microsoft WSL2 (Resourcenschonender Ubuntu Entwicklungsserver unter Windows 10)
### Python / Django: 
- Erstellung einer Python WebApp mit dem Framework Django
- Django Login mit angepasster Registrierungsseite
- Einbindung von MySQL als Datenbank (CreateReadUpdateDelete)
### Python / Django / HTML: 
- Wysiwyg mit dem HTML Framework BOOTSTRAP
-Einbindung vom Wysiwyg Editor Tiny
- Erstellung minimalisierter DOCX Dateien aus HTML heraus
### GitHub: 
- Publizieren über GitHub



## Einrichtung der Projektstruktur

### Shell Befehle

```Shell
[shell] pip install pipenv --user
[shell] pipenv shell
[shell] pipenv install django
[shell] pipenv install mysqlclient
[shell] pipenv install crispy-bootstrap5
[shell] pipenv install django-crispy-forms
[sehll] pipenv install django-tinymce
[shell] django-admin startproject MySQLDjangoProjekt .
[shell] py manage.py startapp MySQLDajangoApp01

[shell] py manage.py makemigrations
[shell] py manage.py migrate
[shell] py manage.py createsuperuser
[shell] git init
[shell] py manage.py runserver

Bei Problemen mit dem Zugriff unter Windows:
[shell] py -m pip install --upgrade --force-reinstall pip


In der Test-DB wurde folgender Superuser erstellt:
User: master
Passwort: Tester12345#

### Verzeichnisse Dateien die angelegt werden müssen

./MySQL-Django/static
./MySQL-Django/MySQLDajangoApp01/ansichten
./MySQL-Django/MySQLDajangoApp01/templates



### Django Projekt starten

[shell] py manage.py runserver
Url: http://127.0.0.1:8000/

### DB anlegen mit dem MySQL Workbench

> [!NOTE]
> Shema-Name: MySQLDjangoProjekt wird mit den folgenden Tabellen erstellt:

'auth_group'
'auth_group_permissions'
'auth_permission'
'auth_user'
'auth_user_groups'
'auth_user_user_permissions'
'django_admin_log'
'django_content_type'
'django_migrations'
'django_session'

### Standard Django Tabellen erstellen lassen

```Shell
[shell] py manage.py migrate
```

### DB Änderungen

Die DB Tabellen werden in der jeweiligen Django App in der models.py definiert.
Feld Typen: https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.Field
Änderungen an der Datenbankstruktur mit folgenden Befehlen migrieren:

```Shell
[shell] py manage.py makemigrations
[shell] py manage.py migrate
```

# github

create a new repository on the command line
echo "# MySQL-Django" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/itleichtgemacht/MySQL-Django.git
git push -u origin main

…or push an existing repository from the command line
git remote add origin https://github.com/itleichtgemacht/MySQL-Django.git
git branch -M master
git push -u origin master

# TinyMCE

URL:
https://www.tiny.cloud/docs/tinymce/latest/django-zip/
https://www.tiny.cloud/my-account/integrate/#html

https://django-tinymce.readthedocs.io
https://www.geeksforgeeks.org/integrating-tinymce-with-django

# VS Code auf Deutsch umstellen
Erweiterung German Language instieren
https://www.anleitung24.com/visual-studio-code-sprache-auf-deutsch-aendern-anleitung.html

# WSL Linux Ubuntu Subsystem einrichten
[shell] sudo apt update && sudo apt upgrade
[shell] sudo apt upgrade python3
[shell] sudo apt install python3-pip
[shell] pip install pipenv

[shell] pipenv shell
	✔ Successfully created virtual environment!
	Virtualenv location: /home/master/.local/share/virtualenvs/MySQL-Django-co0NHAlr
	Creating a Pipfile for this project...
	Launching subshell in virtual environment...
	master@LAP-Armin2022:~/devProjekte/Python-Projekte/django/MySQL-Django$  . /home/master/.local/share/virtualenvs/MySQL-Django-co0NHAlr/bin/activate
	(MySQL-Django) master@LAP-Armin2022:~/devProjekte/Python-Projekte/django/MySQL-Django$

[shell] sudo shutdown -r now


## Wird für das mysql Package benötigt
[shell] sudo apt-get install python3-dev libmysqlclient-dev libssl-dev default-libmysqlclient-dev build-essential pkg-config


## git einrichten
[shell] sudo add-apt-repository ppa:git-core/ppa
[shell] sudo apt-get install git
[shell] sudo apt update && sudo apt upgrade
[shell] git init
[shell] git config --global user.email "info@it-leicht-gemacht.de"
[shell] git config --global user.name "itleichtgemacht"
[shell] git add . 
[shell] git commit   

## MySQL Server
[shell] sudo apt update && sudo apt upgrade
[shell] sudo apt install mysql-server

[shell] sudo update-rc.d mysql defaults

Jedes Mal, wenn WSL heruntergefahren wird, stoppt MySQL auch. Wenn WSL gestartet wird, startet MySQL nicht automatisch, 
obwohl es so konfiguriert werden könnte! Um über das MySQL Workbench aus Windows heraus zuzugreifen zu können müssen noch 
folgende Änderungen gemacht werden:

[shell] sudo vim /etc/mysql/my.cnf

[mysqld]
port = 33061
bind-address=0.0.0.0

[shell] sudo mysql
SELECT user,authentication_string,plugin,host FROM mysql.user;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Tester12345#';

### Allgemeine Befehle
[shell] sudo service mysql start
[shell] sudo service mysql restart


## MySQL deinstallieren
sudo apt-get remove --purge mysql-server mysql-client mysql-common
sudo apt-get autoremove
sudo apt-get autoclean
sudo apt install mysql-server



## WebMin Apache2 für Django installieren/konfigurieren
Url: 	https://webmin.com/download/#standard-modules
		https://wiki.ubuntuusers.de/Apache/mod_wsgi/
		https://www.tutorialspoint.com/django/django_apache_setup.htm
		https://medium.com/@nutanbhogendrasharma/host-django-website-in-apache-webserver-part-2-77a9ce6844f1
		https://www.tecmint.com/forbidden-you-dont-have-permission-to-access-on-this-server-error/
		https://modwsgi.readthedocs.io/en/develop/user-guides/quick-configuration-guide.html#wsgi-application-script-file
		https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-14-04

[shell] sudo apt-get install libapache2-mod-wsgi-py3 
Nach der Installation muss das Modul gegebenenfalls noch aktiviert werden [2]:
[shell] sudo a2enmod wsgi 

### Exkurs Webmin und WordPress
https://www.seekahost.com/how-to-install-wordpress-through-webmin/
https://ubuntu.com/tutorials/install-and-configure-wordpress#1-overview
https://www.webhosterwissen.de/know-how/eigener-webserver/tutorial-linux-apache-mysql-php-lamp-auf-ubuntu-18-04-installieren/

		https://localhost:10000/sysinfo.cgi?xnavigation=1

### php, FireWall
[shell] sudo apt-get install php ufw 
[shell] sudo ufw allow ssh
[shell] sudo ufw allow http
[shell] sudo ufw allow https
[shell] sudo ufw enable
[shell] sudo ufw status

### WordPress
[shell] sudo apt install ghostscript php-bcmath php-curl  php-imagick php-intl php-json php-mbstring php-mysql php-xml php-zip
[shell] sudo mkdir -p /var/www/html/netzsprung

Wordpress muss in das Dateisystem schreiben können, daher den Besitzer auf den Apache Prozess ändern
[shell] sudo chown www-data: /var/www/html/netzsprung

[shell] curl https://wordpress.org/latest.tar.gz | sudo tar zx -C /var/www/html/netzsprung
[shell] sudo service apache2 reload

### Postfix
Url:	https://www.ionos.de/digitalguide/e-mail/e-mail-technik/postfix-mail-server-mit-dovecot-und-squirrelmail-auf-ubuntu/


[shell] sudo systemctl reload postfix
[shell] sudo vim /etc/postfix/main.cf
[shell] sudo apt install mailutils
[shell] echo „TestEmail“ | mail -s yoursubject info@it-leicht-gemacht.de

[shell] sudo dpkg-reconfigure postfix
[shell] sudo postconf -e '[new setting]'

[shell] sudo openssl req -x509 -nodes -newkey rsa:2048 -keyout mailserver.key -out mailserver.crt -nodes -days 365
[shell] sudo openssl req -new -x509 -extensions v3_ca -keyout cakey.pem -out cacert.pem -days 3650

sudo postconf -e 'smtpd_sasl_local_domain ='
sudo postconf -e 'smtpd_sasl_auth_enable = yes'
sudo postconf -e 'smtpd_sasl_security_options = noanonymous'
sudo postconf -e 'broken_sasl_auth_clients = yes'
sudo postconf -e 'smtpd_recipient_restrictions =  permit_sasl_authenticated,permit_mynetworks,reject_unauth_destination'
sudo postconf -e 'inet_interfaces = all'
sudo postconf -e 'smtp_tls_security_level = may'
sudo postconf -e 'smtpd_tls_security_level = may'
sudo postconf -e 'smtpd_tls_auth_only = no'
sudo postconf -e 'smtp_tls_note_starttls_offer = yes'
sudo postconf -e 'smtpd_tls_key_file = /etc/postfix/ssl/mailserver.key'
sudo postconf -e 'smtpd_tls_cert_file = /etc/postfix/ssl/mailserver.crt'
sudo postconf -e 'smtpd_tls_CAfile = /etc/postfix/ssl/cacert.pem'
sudo postconf -e 'smtpd_tls_loglevel = 1'
sudo postconf -e 'smtpd_tls_received_header = yes'
sudo postconf -e 'smtpd_tls_session_cache_timeout = 3600s'
sudo postconf -e 'tls_random_source = dev:/dev/urandom'

[shell] sudo postconf -e 'myhostname = netzsprung.local' 



### günstige V-Server
Url:	https://www.1blu.de/server/vserver/?gad_source=1&gclid=CjwKCAiA29auBhBxEiwAnKcSqheEFBlvkvuFWP0ZxM5YMLfjk6Ip99K8I51bxQyUSoXmMVf4eFBJuBoCwKMQAvD_BwE
		

[shell] sudo systemctl restart apache2
[shell] sudo chown -R master:www-data .
[shell] cd /var/www/html
[shell] sudo find . -type d -exec chmod 755 {} \;
[shell] sudo find . -type f -exec chmod 644 {} \;


### Auszug aus der Apache VirtualHost.conf
Pfad:	/etc/apache2/sites-available/mysql-django.local.conf
Inatalliertes pipenv Verzeichnis liegt: in /var/www/html/mysqldjango/MySQL-Django-env


WSGIPythonPath /var/www/html/mysqldjango/
WSGIScriptAlias / /var/www/html/mysqldjango/MySQLDjangoProjekt/wsgi.py
    
<VirtualHost mysql-django.local:80>
    DocumentRoot /var/www/html/mysqldjango
    ServerName mysql-django.local
    <Directory "/var/www/html/mysqldjango">
        Options None
        Require all granted
    </Directory>
    WSGIDaemonProcess mysql-django.local python-path=/var/www/html/mysqldjango  python-home=/var/www/html/mysqldjango/MySQL-Django-env
    WSGIProcessGroup mysql-django.local
    HostNameLookups off
    Alias /static/ /var/www/html/mysqldjango/static/
</VirtualHost>





Pfad wo Python installiert wird: 	/usr/bin/python3.10
Pfad wo Django Apps sein sollten:	/opt/django-apps
							Bsp:	MySQLDjango


# Microsoft Word und HTML
[shell] pipenv install python-docx
[shell] pipenv install bs4
[shell] pipenv install html2docx

[shell] sudo apt update
[shell] sudo apt install pandoc
[shell] sudo apt install texlive
[shell] sudo apt-get install texlive-latex-base

[shell] sudo dpkg --configure -a
[shell] sudo apt install texlive-lang-german
[shell] pdflatex --version

[shell] pandoc -s test_neu.html -o beispiel.pdf
[shell] pandoc -s test_neu.html -o beispiel.docx




<!--
Allgemeines zu git
==================
https://boolie.org/git-github-anfaenger-tutorial/
https://docs.github.com/de/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks

Allgemeines zu Python MySQL
===========================
https://www.mysqltutorial.org/python-mysql/getting-started-mysql-python-connector/

Allgemeines zu MySQL - Dokumentation
====================================
https://dev.mysql.com/doc/refman/8.3/en/sql-statements.html


HTML nach PDF OpenSource
	https://plainenglish.io/blog/best-python-libraries-to-write-reports-to-pdf-87771be815c9
https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#quickstart

Google Auth
https://www.hacksoft.io/blog/adding-google-login-to-your-existing-django-and-django-rest-framework-applications#conclusion


# LibreOffice und HTML
??? [shell] pipenv install pyoo

sudo apt update
sudo apt install libreoffice
sudo apt install libreoffice-script-provider-python
sudo apt install libreoffice-script-provider-python
sudo apt remove libreoffice libreoffice-script-provider-python
---< NICHT DAS RICHTIGE: pipenv install uno

pipenv install ooo-dev-tools
pipenv install unotools


dpkg -l | grep libreoffice-script-provider-python

-->

---

zum sortieren
