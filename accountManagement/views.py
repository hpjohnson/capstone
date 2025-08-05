from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def account_management_page_view(request):

    return render(request, "accountManagement/accountManagement.html", )
