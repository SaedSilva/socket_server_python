import string
import random

def converter_romanos_para_int(romano):
    romano = romano.upper()

    romanos = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    numero = 0
    anterior = 0

    for letra in romano:
        atual = romanos[letra]

        if anterior < atual:
            numero -= 2 * anterior

        numero += atual
        anterior = atual

    return numero


def gerar_texto_aleatorio(numero_caracteres, numero_palavras):
    texto = ""
    for i in range(numero_palavras):
        for j in range(numero_caracteres):
            texto += random.choice(string.ascii_letters)
        texto += " "
    return texto


def converter_int_para_romanos(numero):
    if numero < 1 or numero > 3999:
        return "Número inválido"
    else:
        romanos = ""
        while numero >= 1000:
            romanos += "M"
            numero -= 1000
        if numero >= 900:
            romanos += "CM"
            numero -= 900
        if numero >= 500:
            romanos += "D"
            numero -= 500
        if numero >= 400:
            romanos += "CD"
            numero -= 400
        while numero >= 100:
            romanos += "C"
            numero -= 100
        if numero >= 90:
            romanos += "XC"
            numero -= 90
        if numero >= 50:
            romanos += "L"
            numero -= 50
        if numero >= 40:
            romanos += "XL"
            numero -= 40
        while numero >= 10:
            romanos += "X"
            numero -= 10
        if numero >= 9:
            romanos += "IX"
            numero -= 9
        if numero >= 5:
            romanos += "V"
            numero -= 5
        if numero >= 4:
            romanos += "IV"
            numero -= 4
        while numero >= 1:
            romanos += "I"
            numero -= 1
        return romanos