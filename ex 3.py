#População a = 80k de pessoas e crescem 3%
#População b = 200k crescem 1.5%

total_a = 80000
total_b = 200000

aumento_a = 0.03
aumento_b = 0.015
ano = 0
while total_a <= total_b:
    ano = ano + 1
    total_a = total_a * (1 + aumento_a)
    total_b = total_b * (1 + aumento_b)
print (ano)
