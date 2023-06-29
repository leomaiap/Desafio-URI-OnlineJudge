entrada = input().split()
item, quantidade = int(entrada[0]), int(entrada[1])
lanche = [[''], [1, 4], [2, 4.5], [3, 5], [4, 2], [5, 1.5]]
total = lanche[item][1] * quantidade
print(f'Total: R$ {total:.2f}')