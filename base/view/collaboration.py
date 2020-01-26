from django.shortcuts import render, redirect


def collab_MoU_view(request):
    return render(request, 'collaboration/MoU.html', context={'active': 'collab_MoU'})

def collab_student_exchange_view(request):
    return render(request, 'collaboration/student_exchange.html', context={'active': 'collab_student_exchange'})
