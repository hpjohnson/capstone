from django.shortcuts import render

# Create your views here.

def about_page_view(request):
    """ 
    render about page
    """

    return render(request, "about/about.html", )
