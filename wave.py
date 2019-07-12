# J. C. (Jack) Cook
# July 11, 2019

# TODO: recreate Mathmatica's representation of a transverse wave
# SOURCE: Matlab guy, PDF Doc, PDf Doc2 and animation guy
# Contributor: Cole Carey

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as an
import random
from copy import deepcopy

"""MIT License

Copyright (c) 2019 J. C. (Jack) Cook

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""


def main():
    # longitudinal or transverse
    val = 'longitudinal'
    t = [t for t in range(0, 500)]  # time domain
    # wave vector
    k1 = 0.4
    k2 = 0.2
    # coordinates of ray (determined by wave vector)
    x = [x for x in range(0, 50)]
    xes = []  # x values for the 15 different lines
    for wave in range(1, 10):
        lst = [x[i] + random.uniform(-0.5, 0.5) for i in range(len(x))]
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
            ax.plot(xes[i], uyes[i], linestyle='none', marker='o', color='k', markersize=2)
        elif val == 'longitudinal':
            ax.plot(uxes[i], [i for j in range(len(uxes[i]))], linestyle='none', marker='o',
                    color='#0A3A4A', markersize=2, zorder=1)
            if i % 5 == 0:
                ax.scatter(uxes[i][i], i, color='#D13737', s=8, zorder=2)

    def grapher():
        ax.set_xlim([-10, 60])
        ax.set_ylim([-10, 30])
        ax.set_title("2D wave equation " + val)
        ax.set_xlabel('x')
        ax.set_ylabel('y')

    grapher()
    ax.text(10, 10, 't = ' + str(0), transform=ax.transAxes, fontsize=12,
            verticalalignment='top')

    def updatePoint(point, color, new_point):
        old_point = point.get_offsets()
        newpt = deepcopy(old_point)
        newpt[0][0] = new_point[0]
        newpt[0][1] = new_point[1]
        point.set_offsets(newpt)
        point.set_facecolors(color)
        point.axes.figure.canvas.draw_idle()

    def init():
        lines = ax.lines
        for i in range(len(lines)):
            lines[i].set_xdata([np.nan] * len(x))
            lines[i].set_ydata([np.nan] * len(x))
        points = ax.collections
        new_point = [10, 10]
        for i in range(len(points)):
            updatePoint(points[i], 'w', new_point)

        return ax.lines

    def animate(iter):
        grapher()
        ax.texts[0].remove()  # remove the text we have
        ax.text(0.05, 0.95, 't = ' + str(iter), transform=ax.transAxes, fontsize=12,
                verticalalignment='top')
        if val == 'transverse':
            uyes = [[k2 * A * np.sin(w * t[iter] - kxnew[i][j]) for j in range(len(xes[i]))] for i in range(len(xes))]
        elif val == 'longitudinal':
            uxes = [[k1 * A * np.sin(w * t[iter] - kxnew[i][j]) for j in range(len(xes[i]))] for i in range(len(xes))]
            uxes = [[uxes[i][j] + xes[i][j] for j in range(len(xes[i]))] for i in range(len(xes))]
        ptcount = 0
        points = ax.collections
        for i in range(len(ax.lines)):
            if val == 'transverse':
                ax.lines[i].set_xdata(xes[i])
                uyes[i] = [uyes[i][j] + i for j in range(len(uyes[i]))]
                ax.lines[i].set_ydata(uyes[i])
            elif val == 'longitudinal':
                ax.lines[i].set_xdata(uxes[i])
                ax.lines[i].set_ydata(i)
                if i % 5 == 0:
                    new_point = [uxes[i][i], i]
                    updatePoint(points[ptcount], '#D13737', new_point)
                    ptcount += 1
        return ax.lines

    ani = an.FuncAnimation(fig, animate, len(t), init_func=init)

    writer=an.writers['ffmpeg'](fps=20)
    dpi = 100
    ani.save(val + '.mp4', writer=writer, dpi=dpi)
    plt.show()


if __name__ == "__main__":
    main()
