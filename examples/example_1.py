import EleganPlot as elegan
import numpy as np


# Генерируем данные
x = np.random.rand(100)
y = np.random.rand(100)

# Использование функций из пакета
fig, ax = elegan.create_figure_and_axes()
elegan.plot([0, 1, 2], [0, 1, 4], ax=ax)
fig.show()
