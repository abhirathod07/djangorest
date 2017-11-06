from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
# Create your views here.


def base(request):
    URL = "https://apifootball.com/api"

    PARAMS = {'action': 'get_leagues', 'APIkey': 'ad66c7cd67d0324830c93f548554f57da97c893d1c9f9cbdacf779b108c46037' }
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    country_id1 = data[0]['country_id']
    country_id2 = data[1]['country_id']
    country_name1 = data[0]['country_name']
    country_name2 = data[1]['country_name']
    show_data = {'first_country': country_name1,'second_country': country_name2}
    # print("The two countries are {} and {}".format(country_name1,country_name2))
# print("The two countries are {} and {}".format(country_name1,country_name2))
    return render(request,'football/base.html',context=show_data)
