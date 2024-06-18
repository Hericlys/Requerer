from django.shortcuts import render


def citizen(request) -> render:
    return render(request, 'citizen/citizen.html')
