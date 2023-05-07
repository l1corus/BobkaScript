from django.shortcuts import render


def main_page(request):
    return render(request, 'main/main_page.html')


def docs(request):
    return render(request, 'main/docs.html')


def about(request):
    return render(request, 'main/about.html')

