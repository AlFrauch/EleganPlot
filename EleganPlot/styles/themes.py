import matplotlib.pyplot as plt

def apply_theme(theme_name):
    """
    Применяет выбранную тему оформления к графикам matplotlib.

    Параметры:
    - theme_name: название темы ('default', 'dark', 'minimalist' и т.д.)
    """
    if theme_name == 'default':
        plt.style.use('default')
    elif theme_name == 'dark':
        plt.style.use('dark_background')
    elif theme_name == 'frauch':
        plt.rcParams.update(theme_params['frauch']['rcParams'])
    else:
        # Можно добавить поддержку пользовательских тем
        raise ValueError(f"Тема '{theme_name}' не найдена.")


theme_params = {'frauch': {'rcParams':{
                                'text.usetex':True,
                                'figure.facecolor':'#2a2d31',
                                'axes.facecolor':'#2a2d31',
                                'axes.labelcolor':'#787878',
                                'axes.titlecolor':'#787878',
                                'axes.labelcolor':'#787878',
                                'figure.dpi': 300
                                        },
                            "other_params":{
                                'facecolor': '#2a2d31',
                                'labelcolor': '#787878',
                                'label_size': 12,
                                'color_plot' : ["#cd5f82", "#8c5096", '#55e1fa']
                            }



        }



                           }