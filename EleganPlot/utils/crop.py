

def crop_figures(objects, fig, bias=0.2):
    bbox = objects.get_window_extent(renderer=fig.canvas.get_renderer())
    fig.set_size_inches(bbox.width / fig.dpi + bias, bbox.height / fig.dpi + bias)
    return fig

