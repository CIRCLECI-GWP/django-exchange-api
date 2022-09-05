import random

supportedCurrencies = ["EUR", "GBP", "NGN", "USD", "YEN"]

def getExchangeRates():
	rates = {}
	for rate in supportedCurrencies:
		rates[rate] = getExchangeRatesForCurrency(rate)
	return rates

def getExchangeRatesForCurrency(currency):
	availableCurrencies = supportedCurrencies.copy()
	availableCurrencies.remove(currency)
	rates = {}
	for rate in availableCurrencies:
		rates[rate] = str(round(random.random(), 2))
	return rates

def getSupportedCurrencies():
	return supportedCurrencies