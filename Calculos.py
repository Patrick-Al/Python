import statistics as stats
import pandas as pd

Comprimento = [58, 64, 58, 56, 68, 55, 68, 62, 68, 50, 54, 70]
print("\n Comprimento:", Comprimento)
for i in range(len(Comprimento)):
    print(f"  Índice {i}: {Comprimento[i]}")

vendas = [58, 64, 58, 56, 68, 55, 68, 62, 68, 50, 54, 70]


frequencia = {}
for valor in Comprimento:
    if valor in frequencia:
        frequencia[valor] += 1
    else:
        frequencia[valor] = 1

print("\n Frequência de cada valor:")
for valor, count in frequencia.items():
    print(f"  {valor}: {count}")

freq = pd.Series(vendas).value_counts()
total = len(vendas)
freq_rel = freq / total
print("\n Frequência relativa:")
print(freq_rel.round(4))


Soma = sum(Comprimento)
print("\n A soma é:", Soma)
Média = sum(Comprimento) / len(Comprimento)
print("\n A média é:", Média)

import statistics
variancia = statistics.variance(Comprimento)
print("\n A variância é:", variancia ) 

desvio_padrao = statistics.stdev(Comprimento)
print("\n O desvio padrão é:", desvio_padrao)

import numpy as np
amplitude = np.ptp(Comprimento)
print("\n A amplitude é:", amplitude)

q1, q2, q3 = np.percentile(Comprimento, [25, 50, 75])
print("\n O primeiro quartil (Q1) é:", q1)
print("\n O segundo quartil (Q2) é:", q2)
print("\n O terceiro quartil (Q3) é:", q3)

