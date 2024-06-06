from django.shortcuts import render
import requests
from django.http import JsonResponse
import os


def home_view(request):
    return render(request, 'home.html')


def domain_search_view(request):
    context = {}
    if 'domain' in request.GET:
        domain = request.GET.get('domain')
        
        if domain:
            # Here, make a request to the external API that provides domain information.
            url = "https://domain-checker7.p.rapidapi.com/whois"
            headers = {
       "X-RapidAPI-Key": os.getenv('RAPIDAPI_KEY'),
       "X-RapidAPI-Host": "domain-checker7.p.rapidapi.com"
  } 
            params = {"domain": domain}
            response = requests.get(url, headers=headers, params=params)
            
            if response.status_code == 200:
                data = response.json()
                # Extract the required information
                context['domain_info'] = {
                    'available': data.get('available'),
                    'Domain': data.get('domain'),
                    'status': data.get('valid'),
                    'Registrant_at': data.get('registrar'),
                    'Created_at': data.get('created_at'),
                    'expires_at': data.get('expires_at'),
                    
                }
            else:
                context['error'] = f"Error fetching domain information: {response.status_code} - {response.text}"
        else:
            context['error'] = 'No domain provided'
    
    return render(request, 'domain_search.html', context)

# Create your views here.
