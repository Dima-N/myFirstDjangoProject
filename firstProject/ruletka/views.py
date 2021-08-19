from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def show_student(request):
    lst = [['Olga', 10], ['Dima', 20], ['Alexy', 30]]
    return render(request, 'hello.txt', {'lst': lst})
