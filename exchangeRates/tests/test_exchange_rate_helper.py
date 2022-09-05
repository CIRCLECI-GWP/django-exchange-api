from django.test import TestCase
from .. import exchangeRateHelper

class ExchangeRateHelperTest(TestCase):
    """ Test module for ExchangeRate Helper """

    def test_get_all_rates(self):
        rates = exchangeRateHelper.getExchangeRates()
        expectedNumberOfRates = len(exchangeRateHelper.getSupportedCurrencies())
        actualNumberOfRates = len(rates)
        self.assertEqual(expectedNumberOfRates, actualNumberOfRates)

    def test_get_unsupported_currency_throws_exception(self):
        with self.assertRaises(ValueError):
            rates = exchangeRateHelper.getExchangeRatesForCurrency("YUAN")

    def test_rates_for_currency_returns_expected_number_of_items(self):
        rates = exchangeRateHelper.getExchangeRatesForCurrency("NGN")
        expectedNumberOfRates = len(exchangeRateHelper.getSupportedCurrencies()) - 1
        actualNumberOfRates = len(rates)
        self.assertEqual(expectedNumberOfRates, actualNumberOfRates)