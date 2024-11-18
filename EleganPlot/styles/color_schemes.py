def get_colors(scheme_name):
    """
    Возвращает список цветов для выбранной цветовой схемы.

    Параметры:
    - scheme_name: название цветовой схемы ('default', 'vibrant', 'pastel' и т.д.)

    Возвращает:
    - Список цветовых кодов
    """
    if scheme_name == 'default':
        return ['#1f77b4']  # Синий цвет по умолчанию
    elif scheme_name == 'vibrant':
        return ['#e45756', '#4c78a8', '#f58518', '#72b7b2', '#54a24b']
    elif scheme_name == 'pastel':
        return ['#aec6cf', '#ffb3ba', '#ffdfba', '#ffffba', '#baffc9']
    else:
        raise ValueError(f"Цветовая схема '{scheme_name}' не найдена.")