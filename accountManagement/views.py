from django.shortcuts import render

# Create your views here.
def account_management_page_view(request):

    return render(request, "accountManagement/accountManagement.html", )
