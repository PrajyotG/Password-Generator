from django.shortcuts import render
from string import ascii_lowercase, ascii_uppercase, punctuation, digits
from random import choice

def home(request):
    return render(request, "generator/home.html", {'to32':range(8,33)})


def password(request):
    pass_len = int(request.GET.get('length', 8))
    chars = list(ascii_lowercase)
    passw = ""

    if request.GET.get('uppercase'):
        chars.extend(list(ascii_uppercase))

    if request.GET.get('digits'):
        chars.extend(list(digits))

    if request.GET.get('special'):
        chars.extend(list(punctuation))

    for i in range(pass_len):
        passw += choice(chars)

    return render(request, "generator/password.html", {'passw':passw})


def about(request):
    return render(request, "generator/about.html")