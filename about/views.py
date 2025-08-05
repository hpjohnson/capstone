from django.shortcuts import render
from .models import About


# Create your views here.
def about_page_view(request):
    """
    render about page
    """
    # get the most recent about from the database
    about = About.objects.all().order_by("-updated_on").first()

    return render(request, "about/about.html", {"about": about}, )
