# EleganPlot

EleganPlot - это библиотека на Python, являющаяся оберткой над matplotlib, предназначенная для создания красивых и элегантных визуализаций данных. Она предоставляет удобные функции и стили для упрощения процесса построения графиков, делая их более привлекательными и понятными.


## Использование

### Пример 1: Построение простого графика

```python
from your_framework.plotting import plot_line
import matplotlib.pyplot as plt

# Данные для графика
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

# Построение графика
plot_line(x, y, title="Простой график", xlabel="X", ylabel="Y")

# Показать график
plt.show()
```



### Пример 2: Использование пользовательской цветовой схемы

```python
from your_framework.plotting import plot_bar
from your_framework.styles.color_schemes import cool_colors
import matplotlib.pyplot as plt

# Данные для графика
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 10]

# Построение графика с пользовательской цветовой схемой
plot_bar(categories, values, color_scheme=cool_colors, title="График с цветовой схемой")

# Показать график
plt.show()
```

![Пример 2](https://via.placeholder.com/400x300.png?text=Пример+2)

## Тестирование

Для запуска тестов используйте:

```bash
pytest tests/
```

## Лицензия

Этот проект лицензирован под лицензией MIT. Подробности смотрите в файле LICENSE.

## Вклад

Мы приветствуем вклад в развитие EleganPlot. Пожалуйста, создавайте pull request'ы и открывайте issues для улучшения проекта.