def fill_color_axes(axes, facecolor, labelcolor, label_size):
    axes.set_facecolor(facecolor)
    axes.tick_params(axis='both', which='both', labelsize=label_size, labelcolor=labelcolor, colors=labelcolor)
    for spine in axes.spines.values():
        spine.set_edgecolor(labelcolor)