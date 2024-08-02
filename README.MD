# Intro
```
Author:     Armin Hünniger
Erstellt:   20.07.2024
git:        DTSL-20240711-v02
```

# Intro

# Notwendige Grundbefehele aus dem vorherigen Tutorial v1

```Shell
python3 -m venv .env
source ./.env/bin/activate

python3 manage.py runserver
python3 manage.py shell
python3 manage.py createsuperuser

pip install -r requirements.txt

python manage.py shell
- und in der Shell das Passwort zurücksetzen wenn z. B. Vergessen
my_user = DjangoTemplate-SQLite.objects.filter(email="info@itleichtgemacht.de").first()
my_user.set_password("NewPassword")
my_user.save()


```

## git Respository

```Shell
…or create a new repository on the command line

echo "# DjangoHuenni-Blog" >> README.md
git init
git add .
git add README.md

git commit -m "first commit"
git branch -M main

git remote add origin https://github.com/itleichtgemacht/DjangoHuenni-Blog.git
git push -u origin main

…or push an existing repository from the command line

git remote add origin https://github.com/itleichtgemacht/DjangoHuenni-Blog.git
git branch -M main
git push -u origin main
```


## Wichtige Django Template-Tags
```
Tag	              Beschreibung
{% block %}	      Definiert einen Block, der in einem erweiterten Template überschrieben werden kann.
{% endblock %}	  Beendet einen Block.
{% extends %}	    Erweitert eine andere Template-Datei.
{% include %}	    Fügt den Inhalt einer anderen Template-Datei ein.
{% load %}	      Lädt eine benutzerdefinierte Template-Tag-Bibliothek.
{% static %}	    Gibt den URL-Pfad zu einer statischen Datei zurück.
{% url %}	        Erzeugt eine URL für die angegebene Ansichtsfunktion.
{% for %}	        Startet eine Schleife über eine Liste von Objekten.
{% endfor %}	    Beendet eine Schleife.
{% if %}	        Startet eine Bedingungsprüfung.
{% elif %}	      Fügt eine Bedingung innerhalb einer {% if %}-Prüfung hinzu.
{% else %}	      Fügt einen "ansonsten"-Block in eine {% if %}-Prüfung ein.
{% endif %}	      Beendet eine Bedingungsprüfung.
{% with %}	      Setzt eine oder mehrere Variablen in einem bestimmten Kontext.
{% endwith %}	    Beendet den {% with %}-Kontext.
{% comment %}	    Fügt einen Kommentar hinzu, der im gerenderten HTML nicht sichtbar ist.
{% endcomment %}	Beendet einen Kommentar.
```

## Wichtige Django Template-Filter
```
Filter	          Beschreibung
date	            Formatiert ein Datum oder eine Datums-/Zeitangabe.
escape	          Wandelt Zeichen so um, dass sie sicher in HTML verwendet werden können.
length	          Gibt die Länge einer Liste oder eines Strings zurück.
lower	            Wandelt eine Zeichenkette in Kleinbuchstaben um.
upper	            Wandelt eine Zeichenkette in Großbuchstaben um.
safe	            Markiert eine Zeichenkette als sicher, sodass sie nicht escapet wird.
truncatechars	    Kürzt eine Zeichenkette auf die angegebene Anzahl von Zeichen.
urlize	          Wandelt URLs in einem Text in anklickbare Links um.
default	          Gibt einen Standardwert zurück, wenn die Variable leer oder nicht definiert ist.
join	            Verbindet eine Liste von Zeichenketten mit einem angegebenen Trennzeichen.
```

Django Templates bieten eine leistungsstarke und flexible Möglichkeit, dynamische Inhalte zu rendern, indem sie eine Vielzahl 
von Tags und Filtern zur Verfügung stellen.

## Erläuterungen mit einfachen Beispiel

```Python
{% extends 'base.html' %}

{% load static %}

{% block title %}Startseite{% endblock %}

{% block content %}
    <h2>Willkommen auf der Startseite!</h2>
    <p>Dies ist der Inhalt der Startseite.</p>
    <p>Heute ist: {{ today|date:"D d M Y" }}</p>
    <p>In Kleinbuchstaben: {{ "Django TEMPLATES"|lower }}</p>

    {% if user.is_authenticated %}
        <p>Willkommen, {{ user.username }}!</p>
    {% else %}
        <p>Bitte <a href="{% url 'login' %}">melden Sie sich an</a>.</p>
    {% endif %}

    {% for item in item_list %}
        <p>{{ item.name }} - {{ item.description|truncatechars:30 }}</p>
    {% endfor %}
{% endblock %}

```

```
{% extends 'base.html' %}:                 Das Template erweitert base.html.
{% load static %}:                         Lädt die statische Dateien-Tag-Bibliothek.
{% block title %}Startseite{% endblock %}: Überschreibt den Titel-Block in der Basisvorlage.
{{ today|date:"D d M Y" }}:                Formatiert das today Datum.
{{ "Django TEMPLATES"|lower }}:            Wandelt den Text in Kleinbuchstaben um.
{% if user.is_authenticated %}...{% else %}...{% endif %}: Bedingte Anzeige basierend auf der Authentifizierung des Benutzers.
{% for item in item_list %}...{% endfor %}:                Schleife durch item_list.
```

Django Templates bieten eine leistungsstarke und flexible Möglichkeit, dynamische Inhalte zu rendern, indem sie eine Vielzahl 
von Tags und Filtern zur Verfügung stellen.



https://testdriven.io/blog/django-static-files/




--- IDEEN
- Know How Datenbank All mein Wissen
-- Tutorial's
--- Tabellen
    Name: tutorials
    Felder:
        id
        rubric          - Char(200)
            z. B. Ubuntu, Python, Django, BootStrap, ...
            z. B. Pyhton
        titel

        TypofBlogPage
            z. B. Totorial
            z. B. Post
        category1       - Char(200)
            z. B. Intro, Get Started, Sets, Tuples, Lists, ...
            z. B. ---
        category2       - Char(200)
            z. B. Zugriff auf Tuples, Methoden, Funktionen, Befehl systemctl, 
            z. B. ---
        category3       - Char(200)
            z. B. Methode count(), Methode index(), ...
            z. B. ---
        category4
            z. B. 
            z. B. 
        category5       - Char(200)

        content         - TinyMCE
            z. B.   Beschreibung
                    Verwendung
                    Syntax
                    Parameter
                    Beispiel

        contentshort    - TinyMCE
        bannerbild      - image
        attachments     - File

        createat
        publishedat





-- Syntax
