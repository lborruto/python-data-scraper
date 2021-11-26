import matplotlib.pyplot as plt
import numpy as np

def draw3 ():

    labels = ['2015', '2016', '2017', '2018', '2019', '2020', '2021']
    demande_means = [20, 34, 30, 35, 27, 30, 31]
    offre_means = [10000, 32, 34, 20, 25,27,20]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, demande_means, width, label='Demande')
    rects2 = ax.bar(x + width/2, offre_means, width, label='Offre')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Quantités')
    ax.set_title("Comparaison de l'offres et de la demande par rapport au années  ")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_xlabel('Années')
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()