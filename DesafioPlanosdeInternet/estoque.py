itens = []

for i in range(3):
    item = input(f'Equipamento {i}: ')
    itens.append(item)

print("Lista de Equipamentos:")  
for item in itens:
    print(f"- {item}")