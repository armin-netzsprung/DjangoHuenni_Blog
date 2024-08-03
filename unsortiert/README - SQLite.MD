# Intro
```
Author:     Armin Hünniger
Erstellt:   10.07.2024
git:        DTSL-20240711-v02
```

# Intro
In dieser Version widmen wir uns den Templates im Django. Nur in sehr wenigen Ausnahmefällen kann auf die responsive Entwicklung verzichtet werden.
Daher schauten wir uns die Zusammenarbeit zwischen Templates und BootStrap 5.x genauer an.

# Notwendige Grundbefehele aus dem vorherigen Tutorial v1

```Shell
python3 -m venv .env
source ./.env/bin/activate

python3 manage.py runserver
python3 manage.py shell
python3 manage.py createsuperuser

pip install -r requirements.text

python manage.py shell
- und in der Shell das Passwort zurücksetzen wenn z. B. Vergessen
my_user = DjangoTemplate-SQLite.objects.filter(email="info@itleichtgemacht.de").first()
my_user.set_password("NewPassword")
my_user.save()


```

## git Respository

```Shell
echo "# DjangoTemplate-SQLite" >> README.md
git init
git branch -M DTSL-20240711-v02
git remote add origin https://github.com/itleichtgemacht/DjangoTemplate-SQLite.git
git push -u origin DTSL-20240711-v02
```

# Installation
## Python
Hier ist keine Installation notwendig. Da BootStrap ein JavaScript Framework ist.

## index.html
Hier wird der Weg über CDN gezeigt. Im Projekt werden wir das BootStrap vom lokalen Static Verzeichnis laden.
Da ich diese Themenreihe noch fortführe und aus diesem Django Projekt ein PWA Anwendung machen möchte, ist dies notwendig.

```HTML
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD"
      crossorigin="anonymous" />

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    ...

    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN"
      crossorigin="anonymous"
    ></script>
```
# Grundlegendes zu Django Templates
## Zwecke und Vorteile von Django Templates
```
Zweck	                                    Beschreibung
Trennung von Logik und Präsentation	      Django Templates ermöglichen eine klare Trennung zwischen der Geschäftlogik (im Python-Code) und der Präsentationslogik (im HTML-Code).        Dies fördert eine saubere, wartbare und übersichtliche Codebasis.
Wiederverwendbarkeit	                    Templates können für verschiedene Teile der Webseite wiederverwendet werden. Zum Beispiel können Header,
                                          Footer und Navigationselemente als separate Templates erstellt und in anderen Templates eingebunden werden.
Erleichterung der Entwicklung	            Entwickler und Designer können gleichzeitig an einem Projekt arbeiten. Designer können sich auf das HTML und 
                                          CSS konzentrieren, während Entwickler die Logik in Python schreiben.
Dynamische Inhalte	                      Mit Django Templates können dynamische Inhalte einfach dargestellt werden. Daten, die vom Backend kommen, 
                                          können direkt in den HTML-Code eingebettet werden.
Template-Vererbung	                      Templates in Django unterstützen Vererbung, was bedeutet, dass man eine Basisvorlage erstellen kann, die 
                                          von anderen Templates erweitert wird. Dies fördert Konsistenz und reduziert Redundanz.
Sicherheitsfunktionen	                    Django Templates bieten Schutz gegen viele Sicherheitsprobleme, wie z.B. Cross-Site Scripting (XSS), indem 
                                          sie automatisch HTML-Entitäten escapen.
```

Django Templates sind unerlässlich für die effiziente und strukturierte Entwicklung von Webanwendungen. Sie ermöglichen die Trennung von HTML und
Python-Code, fördern die Wiederverwendbarkeit von HTML-Strukturen und unterstützen die Einbindung dynamischer Inhalte, wodurch die Erstellung und 
Wartung von Webseiten deutlich vereinfacht wird.

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

# DjangoTemplate-SQLite for free Armin Hünniger
Die Version 1 war für den Einstieg ein nicht so perfekter HTML Code, da es hier überwiegend um ein lauffähiges Django Projekt ging.
In der Version 2 wurden daher die Templates nocheinmal überarbeitet und einige Bugs, die mir im Testlauf aufgefallen sind, bereinigt. 
Weiter wurde der HTML Code und auch die BootStrap's Tag's in der HTML Datei näher erläutert. In der README.md gehe ich daher nicht 
näher ein.






