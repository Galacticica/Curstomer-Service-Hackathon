from django.shortcuts import render

def home_page(request):
    return render(request, 'service/customer_service.html')

def cursed_home_page(request):
    return render(request, 'service/customer_service_cursed.html')

def no_escape(request):
    return render(request, 'service/second_review.html')

def gov(request):
    return render(request, 'service/42.html')

def possess(request):
    return render(request, 'service/possess.html')

def xfile(request):
    return render(request, 'service/us.html')

def names(request):
    return render(request, 'service/names.html')