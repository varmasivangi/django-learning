from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

def about_page(request):
    return HttpResponse("hello world")


def shopping_page(request):
    data = {"product_name":"Shirt"}
    return JsonResponse(data)
     
def show_html_page(request):
    return render(request,"home.html")
