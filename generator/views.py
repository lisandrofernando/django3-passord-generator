from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):



    characters = list('abcdefghijklmnopkrstuvwxz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPKRSTUVWXZ'))

    if request.GET.get('SpecialCharacter'):
        characters.extend(list(';._#$%^&*()+><?/|}{:'))

    if request.GET.get('Number'):
        characters.extend(list('0123456789'))


    length = int(request.GET.get('length', 14))

    passwordcreated = ''

    for x in range(length):
        passwordcreated += random.choice(characters)

    return render(request, 'generator/password.html', {'password': passwordcreated })