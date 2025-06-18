import unittest
import sys
import os

# boa pratica caso fosse modularizar e pastas
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

# importa as funções do conversor
from conversor import celsius_para_fahrenheit, celsius_para_kelvin, celsius_para_rankine

class TestConversorTemperaturas(unittest.TestCase):

    # Testes para Celsius para Fahrenheit
    def test_celsius_para_fahrenheit_ponto_congelamento(self):
        # Teste com o ponto de congelamento da água (0°C = 32°F)
        self.assertAlmostEqual(celsius_para_fahrenheit(0), 32.0, places=2)

    def test_celsius_para_fahrenheit_ponto_ebulicao(self):
        # Teste com o ponto de ebulição da água (100°C = 212°F)
        self.assertAlmostEqual(celsius_para_fahrenheit(100), 212.0, places=2)

    def test_celsius_para_fahrenheit_negativo(self):
        # Teste com uma temperatura negativa (-10°C = 14°F)
        self.assertAlmostEqual(celsius_para_fahrenheit(-10), 14.0, places=2)

    # Testes para Celsius para Kelvin
    def test_celsius_para_kelvin_zero_absoluto(self):
        # Teste com o zero absoluto (-273.15°C = 0K)
        self.assertAlmostEqual(celsius_para_kelvin(-273.15), 0.0, places=2)

    def test_celsius_para_kelvin_cem_graus(self):
        # Teste com 100°C (100°C = 373.15K)
        self.assertAlmostEqual(celsius_para_kelvin(100), 373.15, places=2)

    # Teste para Celsius para Rankine
    def test_celsius_para_rankine_zero_celsius(self):
        # Teste com 0°C = 491.67°R (aproximadamente)
        self.assertAlmostEqual(celsius_para_rankine(0), 491.67, places=2)

    def test_celsius_para_rankine_cem_graus(self):
        # Teste com 100°C = 671.67°R (aproximadamente)
        self.assertAlmostEqual(celsius_para_rankine(100), 671.67, places=2)


if __name__ == '__main__':
    unittest.main()