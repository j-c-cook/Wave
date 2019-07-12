# J. C. (Jack) Cook
# July 11, 2019

# TODO: recreate Mathmatica's representation of a transverse wave
# SOURCE: Matlab guy, PDF Doc, PDf Doc2 and animation guy

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as an
import random


def main():
    # longitudinal or transverse
    val = 'transverse'
    t = [t for t in range(0, 500)]  # time domain
    # wave vector
    k1 = 0.4
    k2 = 0.2
    # coordinates of ray (determined by wave vector)
    x = [x for x in range(0, 50)]
    xes = []  # x values for the 15 different lines
    for wave in range(1, 10):
        lst = [x[i] + random.uniform(0, 1) for i in range(len(x))]
        xes.append(lst)

    ynew = [[k2 / k1 * xes[i][j] for j in range(len(xes[i]))] for i in range(len(xes))]

    kxnew = [[(k1 * xes[i][j]) + (k2 * ynew[i][j]) for j in range(len(xes[i]))] for i in range(len(xes))]

    # Wave params
    A = 5  # amplitude
    w = 0.1  # angular frequency

    fig = plt.figure()
    ax = fig.add_subplot(111)

    if val == 'transverse':
        uyes = [[k2 * A * np.sin(w * 0 - kxnew[i][j]) for j in range(len(xes[i]))] for i in range(len(xes))]
    elif val == 'longitudinal':
        uxes = [[k1 * A * np.sin(w * 0 - kxnew[i][j]) for j in range(len(xes[i]))] for i in range(len(xes))]
    for i in range(len(xes)):
        if val == 'transverse':
            ax.plot(xes[i], uyes[i], linestyle='none', marker='o', color='k', markersize=3)
        elif val == 'longitudinal':
            ax.plot(uxes[i], [i for j in range(len(uxes[i]))], linestyle='none', marker='o', color='k', markersize=3)

    def grapher():
        ax.set_xlim([-10, 60])
        ax.set_ylim([-10, 30])
        ax.set_title("2D wave equation " + val)
        ax.set_xlabel('x')
        ax.set_ylabel('y')

    grapher()
    ax.text(10, 10, 't = ' + str(0), transform=ax.transAxes, fontsize=14,
            verticalalignment='top')

    def init():
        lines = ax.lines
        for i in range(len(lines)):
            lines[i].set_xdata([np.nan] * len(x))
            lines[i].set_ydata([np.nan] * len(x))
        return ax.lines

    def animate(iter):
        grapher()
        ax.texts[0].remove()  # remove the text we have
        ax.text(0.05, 0.95, 't = ' + str(iter), transform=ax.transAxes, fontsize=14,
                verticalalignment='top')
        if val == 'transverse':
            uyes = [[k2 * A * np.sin(w * t[iter] - kxnew[i][j]) for j in range(len(xes[i]))] for i in range(len(xes))]
        elif val == 'longitudinal':
            uxes = [[k1 * A * np.sin(w * t[iter] - kxnew[i][j]) for j in range(len(xes[i]))] for i in range(len(xes))]
            uxes = [[uxes[i][j] + xes[i][j] for j in range(len(xes[i]))] for i in range(len(xes))]

        for i in range(len(ax.lines)):
            if val == 'transverse':
                ax.lines[i].set_xdata(xes[i])
                uyes[i] = [uyes[i][j] + i for j in range(len(uyes[i]))]
                ax.lines[i].set_ydata(uyes[i])
            elif val == 'longitudinal':
                ax.lines[i].set_xdata(uxes[i])
                ax.lines[i].set_ydata(i)
        return ax.lines

    ani = an.FuncAnimation(fig, animate, len(t), init_func=init)

    writer=an.writers['ffmpeg'](fps=10)
    dpi = 100
    ani.save(val + '.mp4', writer=writer, dpi=dpi)
    plt.show()


if __name__ == "__main__":
    main()
