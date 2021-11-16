import numpy as np
import matplotlib.pyplot as plt

def draw ():

    year = [2015, 2016, 2017, 2018, 2019, 2020]
    utilisation_cartes_graphiques = {
        'Gaming': [70, 63, 55, 40, 37, 35],
        'Bureautique': [20, 17, 14, 10, 7, 5],
        'minage': [10, 20, 31, 50, 56, 60],
        
    }

    fig, ax = plt.subplots()
    ax.stackplot(year, utilisation_cartes_graphiques.values(),
                 labels=utilisation_cartes_graphiques.keys())
    ax.legend(loc='upper left')
    ax.set_title('Utilisation des cartes graphiques')
    ax.set_xlabel('Années')
    ax.set_ylabel('utilisation des cartes graphiques (en %)')

    plt.show()