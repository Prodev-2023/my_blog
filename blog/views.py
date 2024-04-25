from django.shortcuts import render
from .models import Post



# Create your views here.

# posts = [
#     {
#         'author':'Mr philip',
#         'title':'The way',
#         'content':'first content',
#         'date_posted':'April 11 2024'
#     },
#      {
#         'author':'Mr Timothy',
#         'title':'The minister',
#         'content':'second content',
#         'date_posted':'April 12 2024'
#     }
# ]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title':'about'})
