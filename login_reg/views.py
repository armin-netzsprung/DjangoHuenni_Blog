
from django.http import HttpRequest                 # beinhaltet die Http Request Typen, wie z. B. Post, Get, ...
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render                 # gibt die gerenderten Daten z. B. zur Ansicht in einer HTML Seite
from django.contrib import messages                 # Stellt Informationen schöner dar und enthält vordefinierte Templates, wie z. B. für Wichtig, Info, usw. zur Verfügung
from .models import *
# ### AH
# Authentication
# ###
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
    return redirect('index')

def regBenutzer(request):
    seite = 'reg'
    form = EigeneUserCreationForm

    if request.method == 'POST':
        form = EigeneUserCreationForm(request.POST)
        if form.is_valid():
           benutzer = form.save(commit=False)
           benutzer.save()

           #kunde = Staff(name=request.POST['username'],email=request.POST['email'], benutzer=benutzer)
           #kunde.save()
           #bestellung = Bestellung(kunde=kunde)
           #bestellung.save()
           username = form.cleaned_data.get('benutzer')
           messages.success(request=f"Neuer Benutzer erstellt: {username}")
           login(request, benutzer)
           return redirect('index')
        else:
            messages.error(request, "Fehlerhafte Eingabe! Bitte prüfe deinen Benutzernamen oder das Passwort!")

    ctx = {'form': form, 'seite': seite}
    return render(request, 'login_reg/login.html', ctx)

