from .utils.gradient import gradient_fill, gradient_fill_inverse
from .styles.themes import *
from .utils.fill import fill_color_axes


current_theme = 'frauch'
def create_figure_and_axes(theme='frauch',**kwargs):
    """
    Creates a matplotlib figure and axes with default styling.

    Returns:
    - fig: The created matplotlib Figure object.
    - ax: The created matplotlib Axes object.
    """
    global current_theme
    if theme is not None:
        current_theme = theme
    apply_theme(current_theme)
    fig, ax = plt.subplots(**kwargs)
    if current_theme == 'frauch':
        facecolor = theme_params[current_theme]["other_params"]['facecolor']
        labelcolor =theme_params[current_theme]["other_params"]['labelcolor']
        label_size = theme_params[current_theme]["other_params"]['label_size']
        fill_color_axes(ax, facecolor=facecolor, labelcolor=labelcolor, label_size=label_size)
    return fig, ax


def plot_line(x, y, ax=None, gradient=False, gradient_inverse=False, gradient_fill_max=False,
              gradient_fill_min=False, title=None, **kwargs):
    if ax is None:
        fig, ax = create_figure_and_axes()
    if current_theme == 'frauch':
        color_plot = theme_params[current_theme]["other_params"]['color_plot'][len(ax.lines)%3]
    else:
        color_plot = 'b'
    line, = ax.plot(x, y, color=color_plot, **kwargs)
    if gradient:
        gradient_fill(x, y, line=line, fill_color=color_plot, ax=ax,  gradient_fill_min=gradient_fill_min)

    if gradient_inverse:
        gradient_fill_inverse(x, y, line=line, fill_color=color_plot, ax=ax,  gradient_fill_max=gradient_fill_max)
    if title is not None:
        ax.set_title(title)
    return ax