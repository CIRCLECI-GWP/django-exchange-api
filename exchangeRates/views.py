from django.shortcuts import render
from django.http import JsonResponse
from http import HTTPStatus
from . import exchangeRateHelper

def index(request):
    return JsonResponse(exchangeRateHelper.getExchangeRates(), safe=False)

def rates(request, currency):
    try:
        return JsonResponse(exchangeRateHelper.getExchangeRatesForCurrency(currency))
    except:
        return JsonResponse({'error':'Unsupported currency provided'}, status = HTTPStatus.BAD_REQUEST)