from matplotlib.widgets import Cursor
import matplotlib.pyplot as plt

'''
Documentation: 
https://matplotlib.org/stable/gallery/widgets/cursor.html#sphx-glr-gallery-widgets-cursor-py
https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot
'''

'''
Configurações iniciais
'''
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 1000)
ax.set_ylim(0, 1000)

'''
Insere a quantidade de motes contando com a base central - considerar primeira coordenada.
'''
motes = int(input('Quantidade de motes: '))

# motes
for vi in range(0, motes + 1):
    coordenada = input()
    result = coordenada.split(", ")
    cx = float(result[0])
    cy = float(result[1])

    # base central
    if vi == 0:
        ax.plot(cx, cy, 'm*')

    else:
        ax.plot(cx, cy, 'gD')

'''
Legenda
'''
plt.style.use('classic')
plt.title('Representation of the motes spread across the cartesian plane')
plt.xlabel('X Axis(1000 meters)')
plt.ylabel('Y Axis(1000 meters)')
#plt.legend()

# Set useblit=True on most backends for enhanced performance.
cursor = Cursor(ax, useblit=True, color='yellow', linewidth=1)

plt.savefig('plano_cartesiano.png')
print('Cartesian plane saved!')