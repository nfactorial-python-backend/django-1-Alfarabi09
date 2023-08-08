from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
import random, math
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

def generate_random_number(request, min, max):
    if min > max:
        return HttpResponse({'error': 'min должен быть меньше max'})

    number = random.randint(min, max)
    return HttpResponse(str(number))

def reverse_text(request, text):
    reversed_text = text[::-1]
    return HttpResponse(reversed_text)

def calculate_factorial(request, number):
    if number < 0:
        return HttpResponse({'error': 'number должен быть больше или равен 0'})

    factorial = math.factorial(number)
    return HttpResponse(str(factorial))