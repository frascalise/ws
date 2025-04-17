from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

# Custom 404 view
def not_found_view(request):
    message = "Oops! The page you're looking for doesn't exist or has been moved."
    return render(request, 'error/error.html', {'status_code': 404, 'message': message}, status=404)