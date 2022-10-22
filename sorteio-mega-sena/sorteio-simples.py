from random import sample

# Altere para a quantidade de sorteios que deseja concorrer
num_sorteios = 8
# Altere para a quantidade de números que terá em cada sorteio
quantidade_nums = 7

for num_sorteio in range(num_sorteios):
    print(f'Sorteio {num_sorteio + 1}: {sample(range(1,61), quantidade_nums)}')
