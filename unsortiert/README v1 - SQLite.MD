# Intro
Author:     Armin Hünniger
Erstellt:   10.07.2024
Geändert:   12.07.2024 19:15 Uhr
     Was:   Web-Links ergänzt und Feinheiten noch bereinigt
git:        DTSL-20240711-v02

# Installation
## Grundinstallation Python - Django
- Wechseln sie in das Entwicklungsverzeichnis indem Sie Ihren sourcecode erstellen
- Erstellen Sie ein neues Verzeichnis z. B. DjangoTemplate-SQLLite

```Shell
mkdir DjangoTemplate-SQLLite
cd DjangoTemplate-SQLLite
```

- Starten Sie den Code Editor, in meinem Fall Microsoft Visual Code
```Shell
code .
```


- Starten sie im Visual Code über <Terminal - Neues Terminal> ein Termininalfenster

- Erstellen Sie eine neue virtuelle Umgebung. Somit haben Sie jedes Django Projekt unter kontrolle, wenn sich einmal die Python Version ändern sollte.

```Shell
python3 -m venv .env
source ./.env/bin/activate
```

- Die Verwaltung von Python-Paketen kann über eine einfache Textdatei geschehen, die requirements.txt. Erstellen
  Sie die im Projektverzeichnis und schreiben Sie als erstes das Framework Django hinein und drücken Sie Return. Danach installieren wir die Pakete mit pip
  <requirements.txt>
  Django

  ```Shell
  pip install -r requirements.text
  ```

  ## Erstellung eines Django Projektes
  Ein Django Projekt ist die Projektstruktur, die wiederum mehrere Django Anwendungen haben kann.

  Hierfür nehmen wir uns die mitgelieferte Django-Shell Befehle zur Hand, in diesem Fall django-admin 

```Shell
  django-admin startproject djangotemplateproject .
```

  Mit diesem Kommando wird ein neues Verzeichnis djangotemplateproject erstellt und die notwendigen Dateien:

```Shell
  manage.py         - hat die gleichen Funktionen wie das Befehlszeilenhilfsprogramm django-admin
    helloproject/   - Projektverzeichnis
    __init__.py     - hiermit erkennt Python, dass es ein Paket ist
    asgi.py         - Einstiegspunkt für den Webserver (wird hier nicht verwendet)
    wsgi.py         - Einstiegspunkt für den Webserver (wird hier näher erklärt mit einem Plesk Apache2)
    settings.py     - Enthält alle Einstellungen Projektübergreifend
    urls.py         - Enthält die Web-URLs die von einem Webbrowser aufgerufen werden können
```
  
  Nun kann die Webseite, sprich das erste Djangoprojekt auch schon gestartet werden. Zum jetzigen Zeitpunkt werden noch Fehler ausgegeben, hierzu später mehr.

  ```Shell
  python3 manage.py runserver
  ```

  Erreichbar ist unser erstes Blanko Django Projekt unter: http://localhost:8000/ oder http://127.0.0.1:8000

  Fehlermeldung nach dem Start mit runserver:
  --> You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
  Run 'python manage.py migrate' to apply them.

  Was nun noch fehlt ist die SQLLite Datenbank. Auch hier unterstützt uns das Framework. Standardmäßig bringt Django eine Datenbank Administrationsseite mit. Die dazugehörige Datenbank wird mit folgenden Befehlen erstellt:

  ```Shell
  python3 manage.py makemigrations
  python3 manage.py migrate
```

  Im Terminal wird nun angezeigt, dass Änderungen an der Datenbank durchgeführt werden müssen. Dies ist logisch, da wir ein neues Projekt aufgesetzt haben und noch keine Datenbank haben:

  Ausgabe im Termin sollte etwa so sein:

```Shell
  Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions

  Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```
  
  Da standardmäßig seitens Django eine SQLLite Datenbank bereits schon konfiguriert ist, wird diese im Projektordner auch erstellt:

```Shell
    manage.py         - hat die gleichen Funktionen wie das Befehlszeilenhilfsprogramm django-admin
    db.sqlite3        - SQLite 3 Datenbank (hier werden alle Tabellen gespeichert)
    helloproject/     - Projektverzeichnis
      __init__.py     - hiermit erkennt Python, dass es ein Paket ist
      asgi.py         - Einstiegspunkt für den Webserver (wird hier nicht verwendet)
      wsgi.py         - Einstiegspunkt für den Webserver (wird hier näher erklärt mit einem Plesk Apache2)
      settings.py     - Enthält alle Einstellungen Projektübergreifend
      urls.py         - Enthält die Web-URLs die von einem Webbrowser aufgerufen werden können
```

  Starten wir nun unseren Entwicklungs-Web-Server, so sollten keine Fehlermeldungen mehr erscheinen:

  ```Shell
  python3 manage.py runserver
  ```

  Ausgabe sollte in etwa so im Terminal aussehen:

```Shell
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
    July 11, 2024 - 09:09:13
    Django version 5.0.7, using settings 'djangotemplateproject.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
```


## Erstellung einer Django App im Django Projekt
  wie erwähnt kann ein Django Projekt mehrere Apps beinhalten, z. B. für eine Loginseite für einen Mitgliederbereich, eine App die sich um einen Blog kümmert, eine App für einen Shop und vieles mehr.

  Mit diesem Befehl erstellen wir uns eine hello_world-App:

```Shell
  python3 manage.py startapp hello_world

  hello_world/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py           # hier wird der Inhalt der Datenbank definiert
    tests.py
    views.py            # hier die Funktionen erstellt, wenn eine Webbrowser URL aufgerufen.
```

  Diese neuerstellte App muss nun noch im Projekt eingebunden werden. Hierzu muss die Liste INSTALLED_APPS in der Datei settings.py um die Klasse aus der apps.py ergänzt werden:

```Python

  INSTALLED_APPS = [
    'django.contrib.admin',        # Admin-Webseite /admin
    'django.contrib.auth',         # Authentifizeirungssystem
    'django.contrib.contenttypes', # Framework für Inhaltstypen
    'django.contrib.sessions',     # Sessionverwaltung
    'django.contrib.messages',     # Framework für Messaging
    'django.contrib.staticfiles',  # Framework zum Verwalten statischer Dateien (siehe auch weiter unten)
    # ### AH
    # Selbstentwickelten Apps ...
    # ###
    'hello_world.apps.HelloWorldConfig',   
  ]
```

  Soweit so gut, aber wie kann ich nun die App über den Webbrowser aufrufen, bzw. erreichen. Hierzu mehr im folgenden Abschnitt

## Kurzer Überblick wie Django arbeitet
### Models - models.py
In der models.py werden die Datenbankinhalte definiert. Diese Datei ist grundlegend damit mit "python3 manage.py makemigrations bzw. migrate," eine Datenbank erstellt, als auch geändert werden kann.
Django bringt von sich aus eine umfassende Definitions- und Funktionssammlung mit. 
Weiteres folgt daher in einen separaten Abschnitt

### Routen - urls.py
In der urls.py werden die Web-URLs definiert und welche View / Ansicht angezeigt werden soll. Im Projektverzeichnis, als auch im App-Verzeichnis können urls.py Dateien enthalten sein.
Details folgen in einen separaten Abschnitt
Unser Beispiel enthält eine Minimalversion

### Views / Ansichten - views.py
In der views.py Datei werden die aus der urls.py Datei entsprechenden Ansichten und der dazugehörige Source-Code verwaltet.
Details folgen in einen separaten Abschnitt
Unser Beispiel enthält eine Minimalversion

## Routen - urls.py 
Erstellen wir nun eine Route um die hello_world App aufzurufen. Hierzu erstelle folgende Datei mit Inhalt im App Verzeichnis:

```Python
hello_world/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('helloworld', views.hello, name='hello'),    #  https://localhost:8000/helloworld wird mit der View views.hello verbunden
]
```

Die urlpattens ist eine Pyhton-Tupel, in dem die Ansichten und URLs verbunden werden.
Details folgen in einem separaten Abschnitt

Diese urls.py muss nun noch dem Projekt bekanntgegeben werden, dass es diese App gibt. Hierzu muss Sie in der sogenannten Urlconf im Projektverzeichnis konfiguriert werden.

```Python
urls.py (aus dem Projektverzeichnis)
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),      
    path('helloworld', include('hello_world.urls')),
    path('admin/', admin.site.urls),
]
```




## Ansichten - views.py
Appverzeichnis (hello_world): Wir rufen in der urls.py die view.hello auf. Diese wird in der views.py im App Verzeichnis definiert.

```Python
hello_world/views.py
from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, world! Die App hello_world wurde aufgefrufen.")
```


Projektverzeichnis: Wir rufen in der urls.py die view.hello auf. Diese wird in der views.py im App Verzeichnis definiert.

```Python
views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Projekt index wurde aufgerufen!")

```

Nun muss noch der Webserver einmal neugestartet werden. Fertig die erste minimalisierte Webseite wurde nun erstellt.

Folgende Web-URLs haben wir nun erstellt:
localhost:8000/
localhost:8000/hello_world

Probiere es aus. Es sollten unterschiedliche Texte, wie in der View definiert erscheinen.

# Erstellung eine Login und Registrierungs App
Die App soll den Namen "login_reg" lauten.

```Shell
python3 manage.py startapp login_reg
```


Für die Darstellung der Webseite erweitern wir noch die Funktion um Templates (BootStrap-html-Dateien) und legen auch einen statischen Ordner für Bilder, css, js Dateien usw. an

mkdir templates
mkdir static

DjangoTemplate-SQLLite/
  temlates
  static

Nicht im App- oder Projektverzeichnis anlegen!


## models.py


## urls.py 
### Appverzeichnis
```Python
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginSeite, name ="login"),
    path('logout/', views.logoutBenutzer, name ="logout"),
    path('reg/', views.regBenutzer, name ="reg"),
]
```

### Projektverzeichnis
urls.py (aus dem Projektverzeichnis)

```Python
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),      
    path('', views.impressum, name='impressum'),      
    path('test', views.test, name='test'),      
    path('helloworld', include('hello_world.urls')),    
    path('login', include('login_reg.urls')),

    path('admin/', admin.site.urls),
]
```



## views.py (App-Verzeichnis)

```Python
from django.http import HttpRequest                 # beinhaltet die Http Request Typen, wie z. B. Post, Get, ...
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render                 # gibt die gerenderten Daten z. B. zur Ansicht in einer HTML Seite
from django.contrib import messages                 # Stellt Informationen schöner dar und enthält vordefinierte Templates, wie z. B. für Wichtig, Info, usw. zur Verfügung
from .models import *

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import EigeneUserCreationForm



def loginSeite(request):
    seite = 'login'
    if request.method == 'POST':
        benutzername = request.POST['benutzername']
        passwort = request.POST['passwort']

        benutzer = authenticate(request, username=benutzername, password=passwort)  # Stimmen die Logindaten, so wird der Benutzer zurückgegeben.

        if benutzer is not None:            # ist ein Benutzer ermittelt worden, so wird
            login(request, benutzer)        # dieser eingeloggt und
            return redirect('test')    # die Beiträge (Post) angezeigt
        else:
            messages.error(request, "Benutzername oder Passwort nicht korrekt.")

    return render(request, 'login_reg/login.html', {'seite': seite})

def logoutBenutzer(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('home')

def regBenutzer(request):
    seite = 'reg'
    form = EigeneUserCreationForm

    if request.method == 'POST':
        form = EigeneUserCreationForm(request.POST)
        if form.is_valid():
           benutzer = form.save(commit=False)
           benutzer.save()

           username = form.cleaned_data.get('benutzer')
           messages.success(request=f"Neuer Benutzer erstellt: {username}")
           login(request, benutzer)
           return redirect('home')
        else:
            messages.error(request, "Fehlerhafte Eingabe! Bitte prüfe deinen Benutzernamen oder das Passwort!")

    ctx = {'form': form, 'seite': seite}
    return render(request, 'login.html', ctx)
```

## views.py (Projekt-Verzeichnis)

```Python
from django.shortcuts import render

def index(request):
    # home.html aus dem Template Verzeichnis laden.
    return render(request, 'home.html')


def impressum(request):
    return render(request, 'impressum.html')
```


## Templates





## settings.py

```Python
  INSTALLED_APPS = [
    'django.contrib.admin',        # Admin-Webseite /admin
    'django.contrib.auth',         # Authentifizeirungssystem
    'django.contrib.contenttypes', # Framework für Inhaltstypen
    'django.contrib.sessions',     # Sessionverwaltung
    'django.contrib.messages',     # Framework für Messaging
    'django.contrib.staticfiles',  # Framework zum Verwalten statischer Dateien (siehe auch weiter unten)
    # ### AH
    # Selbstentwickelten Apps ...
    # ###
    'hello_world.apps.HelloWorldConfig',   
    'login_reg.apps.LoginRegConfig',   
     # BootStrap5 bekanntgeben für die HtML Templates
    "crispy_bootstrap5",           # Framework um HTML Dateien zu designen (Desktop, Mobile, ... )
    "crispy_forms",                # Framework zur Verwaltung von Formularen zur Eingabe der Daten 

]


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [BASE_DIR / 'templates'], 
        
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```


## requirements.txt
Django
crispy_bootstrap5
django-crispy_forms

## forms.py (App-Verzeichnis)

```Python
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EigeneUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control'})
        self.fields['username'].label = 'Benutzername'
        self.fields['password1'].widget.attrs.update({'class':'form-control'})
        self.fields['password1'].label = 'Passwort'
        self.fields['password2'].widget.attrs.update({'class':'form-control'})
        self.fields['password2'].label = 'Passwort wiederholen'
        self.fields['email'].widget.attrs.update({'class':'form-control'})
        self.fields['email'].label = 'Email'
 ```
       
## Benutzer anlegen und im Admin-Center anmelden

Nun haben wir den Quellcode soweit fertig und wir müssen nur noch einen Benutzer anlegen. 

```Shell
python3 manage.py createsuperuser --username=master --email=info@it-leicht-gemacht.de 
```


Ruft man nun die http://localhost:8000/admin auf, so erhält man eine Übersicht der angelegten Tabellen.
Wie man neu angelegte Tabellen im Admin-Center sichtbar macht, folgt in einen weiteren Kapitel.



############# neues Kapitel #############
# Django Hintergrundwissen zu dem ersten Kapitel
## Dateistruktur und Djangoshell Befehle



## Aufbau eines Django-Projektes
### Was ist der Unterschied zwischen einem Projekt und einer App im Django
### Ergänzende Erläuterungen zu den am häufigsten verwendeten Dateien
#### Allgemeines
hier sollte eine grafische Darstellung als JPG sein....


#### settings.py
In der settings.py werden alle Einstellungen für das Projekt und den enthaltenen App's konfiguriert.
Eine vollständige Dokumentation findet ihr unter: https://docs.djangoproject.com/en/5.0/ref/settings/

#### urls.py
Eine vollständige Dokumentation findet ihr unter: https://docs.djangoproject.com/en/5.0/ref/urls/

#### view.py
Eine vollständige Dokumentation findet ihr unter: https://docs.djangoproject.com/en/5.0/ref/class-based-views/base/

#### models.py
Eine vollständige Dokumentation findet ihr unter: https://docs.djangoproject.com/en/5.0/ref/models/

#### froms.py
Eine vollständige Dokumentation findet ihr unter: https://docs.djangoproject.com/en/5.0/ref/forms/

#### Staticdateien
Eine vollständige Dokumentation findet ihr unter: https://docs.djangoproject.com/en/5.0/howto/static-files/

#### Templates
Eine vollständige Dokumentation findet ihr unter: https://docs.djangoproject.com/en/5.0/ref/templates/

#### Bonus: wsgi.py
Eine vollständige Dokumentation findet ihr unter:
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/modwsgi/



# Hintergrundinformationen
## Django Upgrade How To
Links: https://docs.djangoproject.com/en/5.0/howto/upgrade-version/

# git Respository

```Shell
echo "# DjangoTemplate-SQLite" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M DTSL-20240711-v01
git branch -M DTSL-20240711-v02

git remote add origin https://github.com/itleichtgemacht/DjangoTemplate-SQLite.git
git push -u origin DTSL-20240711-v02
```




