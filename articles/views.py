from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request):
	articles = Article.objects.all()
	return render(request, 'articles/index.html', {'articles': articles})

def create(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		content = request.POST.get('content')
		Article.objects.create(title=title, content=content)
		return redirect('articles:index')
	return render(request, 'articles/create.html', {'articles': create})

