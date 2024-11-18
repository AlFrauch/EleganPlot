# EleganPlot

EleganPlot - это библиотека на Python, являющаяся оберткой над matplotlib, предназначенная для создания красивых и элегантных визуализаций данных. Она предоставляет удобные функции и стили для упрощения процесса построения графиков, делая их более привлекательными и понятными.


## Использование
<details>
<summary>Простой график</summary>

### Пример 1: Построение простого графика

```python
import EleganPlot as elegan

# Данные для графика
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

# Использование функций из пакета
fig, ax = elegan.create_figure_and_axes(theme='frauch', dpi=200)

# Построение графика
ax = elegan.plot_line(x, y, ax=ax, title="Simple graph")
fig.show()
```
![alt text](https://github.com/AlFrauch/EleganPlot/blob/main/pictures/example_1.png)
</details>

<details>
<summary>Простой график с градиентной тенью</summary>

### Пример 2: Построение простого графика c градиентом

```python
import EleganPlot as elegan

# Данные для графика
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

# Использование функций из пакета
fig, ax = elegan.create_figure_and_axes(theme='frauch', dpi=200)

# Построение графика
ax = elegan.plot_line(x, y, ax=ax, title="Simple graph", gradient=True)
fig.show()
```

![alt text](https://github.com/AlFrauch/EleganPlot/blob/main/pictures/example_2.png)
</details>

## Вклад

Мы приветствуем вклад в развитие EleganPlot. Пожалуйста, создавайте pull request'ы и открывайте issues для улучшения проекта.