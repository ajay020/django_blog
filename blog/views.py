from django.shortcuts import render

posts = [
    {
        'author':'CoreuMS',
        'title':'Blog post 1',
        'content':'First post content',
        'date_posted':'Feb 13 ,2020'
    },
      {
        'author':'Ola Hola',
        'title':'Blog post 2',
        'content':'Second post content',
        'date_posted':'Feb 14 ,2020'
    }
]

def home(request):
    return render(request,'blog/home.html')

def about(request):
   return render(request,'blog/about.html')