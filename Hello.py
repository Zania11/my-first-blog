print('Hello, djangogirls')
if 3 > 2 :
	print('To działa!')
if 5 > 2 :
	print('5 jest jednak wieksze od 2')
else :
	print('5 nie jest wieksze od 2')
name = ''
if name == 'Ola' :
	print('Hey, Ola!')
elif name == 'Sonja' :
	print('Hey, Sonja!')
else :
	print('Hey, nieznajoma!')
glosnosc = 57
if  glosnosc < 20 :
	print('Prawie nic nie slychac.')
elif 20 <= glosnosc < 40 :
	print('O muzyka leci w tle.')
elif 40 <= glosnosc < 60 :
	print('Idealnie, moge uslyszec wszystkie detale.')
elif 60 <= glosnosc < 80 :
	print('Dobra impreza.')
elif 80 <= glosnosc < 100 :
	print('Troszecze za glosno.')
else :
	print('Oj oj moje uszy...')

def hej(imie) :
	if imie == 'Ola' :
		print('Hey, Ola!')
	elif imie == 'Sonja' :
		print('Hey, Sonja!')
	else :
		print('Hey, nieznajoma!')

hej('Zaneta')

def hejka(imie) :
	print('Hej' + imie + '!')

hejka('Rachel')

dziewczyny = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Zaneta']
for imie in dziewczyny :
	hejka(imie)
	print('Kolejna dziewczyna')


for i in range(1, 6):
	print(i)
