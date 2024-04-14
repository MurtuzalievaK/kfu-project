from django.shortcuts import render
from .models import New
from django.http import Http404
from django.shortcuts import render, get_object_or_404
def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

def news(request):
    newss = New.objects.order_by('-id')
    return render(request, 'main/news.html', {'title': 'Новости клининга', 'newss': newss})


def get_news_description(request, news_id):
    # Получаем объект новости по переданному ID
    news = get_object_or_404(New, pk=news_id)

    # Возвращаем описание новости в формате JSON
    return JsonResponse({'title': news.title, 'description': news.news})
def contacts(request):
    def news_detail(request, news_id):
        try:
            news = New.objects.get(id=news_id)
        except New.DoesNotExist:
            raise Http404("Новость не найдена")

        newss = New.objects.order_by('-id')  # Получаем все новости для боковой панели
        return render(request, 'main/news.html', {'title': 'Новости клининга', 'newss': newss, 'selected_news': news})
    return render(request, 'main/contacts.html')

from django.http import JsonResponse

def send_order(request):
    if request.method == 'POST':
        return JsonResponse({'success': True})

def orderForm(request):
    if request.method == 'POST':
        return JsonResponse({'success': True})

