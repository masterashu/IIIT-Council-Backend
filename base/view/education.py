from django.shortcuts import render, redirect


def education_btech(request):
    return render(request, 'education/b_tech.html', context={'name': 'education_btech'})
