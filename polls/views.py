from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
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

def calculator(request, first, operation, second):
        if operation == 'add':
            result = first + second
        elif operation == 'sub':
            result = first - second
        elif operation == 'mult':
            result = first * second
        elif operation == 'div':
            if second != 0:
                result = first / second
            else:
                return HttpResponseBadRequest("Cannot divide by zero")
        else:
            return HttpResponseBadRequest("Invalid operation")

        return HttpResponse(str(result))