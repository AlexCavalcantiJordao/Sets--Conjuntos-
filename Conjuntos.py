from pydoc import plain

planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(planeta_anao)

qtde_p = len(planeta_anao)
print(qtde_p)

'Ceres' in planeta_anao

for astro in planeta_anao:
    print(astro.upper())

astros = ['Lua', 'Vênus', 'Sirius', 'Marte', 'Lua']
print('Lista: ', astros)
astrosSet = set(astros)
print('Conjunto: ', astrosSet)

p1 = {'Terra', 'Vênus', 'Mercurio', 'Marte'}
p2 = {'Terra', 'Vênus', 'Mercurio', 'Marte', 'Saturno'}
print(p1 | p2)

p1 = {'Terra', 'Vênus', 'Mercurio', 'Marte'}
p2 = {'Terra', 'Vênus', 'Mercurio', 'Marte', 'Saturno'}
print(p1 & p2)