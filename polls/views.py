from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, nfactorial")

def add(request, first, second):
        result = first + second
        return HttpResponse(str(result))

def upp(request, text):
        return HttpResponse(str(text).upper())

def is_palindrome(request, word):
        if word == word[::-1]:
            return HttpResponse("True")
        return HttpResponse("False")