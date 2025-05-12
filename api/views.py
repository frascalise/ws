from django.http import HttpResponse
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home/home.html')

# Custom 404 view
def not_found_view(request, exception):
    message = "Oops! The page you're looking for doesn't exist or has been moved."
    return render(request, 'error/error.html', {'status_code': 404, 'message': message}, status=404)

def net_worth(request):
    return redirect('https://docs.google.com/spreadsheets/d/1lnO_5bNFqW7wP4a7W94wnnTM7oEBH4pQaOc1vKpTOes/edit?usp=sharing', permanent=True)

def oracle(request):
    return render(request, 'other/oracle/oracle.html')