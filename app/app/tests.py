"""
Teste simples
"""
from django.test import SimpleTestCase

from app import calcular

class CalcularTestCase(SimpleTestCase):
    """Modulo de calculo e teste"""

    def teste_somando_numeros(self):
        res = calcular.somar(5, 6)

        self.assertEquals(res, 11)

    def teste_subtraindo_numeros(self):
        res = calcular.subtrair(5, 6)

        self.assertEquals(res, -1)
