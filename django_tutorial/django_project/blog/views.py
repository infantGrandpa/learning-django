from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Brett Abraham',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 11, 2021'
    },
    {
        'author': 'Brett Abraham',
        'title': 'Blog Post 2',
        'content': '2nd Post Content',
        'date_posted': 'August 12, 2021'
    },
    {
        'author': 'Brett Abraham',
        'title': 'Blog Post 3',
        'content': '3rd Post Content',
        'date_posted': 'August 13, 2021'
    },
    {
        'author': 'Brett Abraham',
        'title': 'Blog Post 4',
        'content': '4th Post Content',
        'date_posted': 'August 14, 2021'
    },
    {
        'author': 'Brett Abraham',
        'title': 'Blog Post 5',
        'content': '5th Post Content',
        'date_posted': 'August 15, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
