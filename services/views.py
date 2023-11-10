from django.shortcuts import render, redirect, reverse , HttpResponse


def services_list(request):
    if request.method == 'POST':
        services = str(request.POST.get('service'))
        return redirect(services)
    else:
        return render(request, 'services/services_lis.html')
