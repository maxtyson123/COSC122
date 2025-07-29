"""Program to do a specified number of steps of Euler's Method
   to a final time,
   and show a plot of the Euler's method solution.
"""
import matplotlib.pyplot as plt
import numpy as np
from trio import sleep


def euler_step(dydt, t0, y0, h):
    """One step of Euler's method.
    DE function dydt(t, y), initial t = t0, initial y = y0, step size = h.
    Return y1 = y0 + h*f(t0,y0) at end of step.
    """
    dydt_value = dydt(t0, y0)
    y1 = y0 + h * dydt_value
    return y1


def eulers_method_n_steps_t_final(dydt, t0, y0, tf, n_steps):
    """Do n_steps steps of Euler's method from t0 to tf.
    DE function dydt(t, y), initial t = t0, initial y = y0,
    to final t tf, n_steps steps.
    Return numpy arrays of t and y values.
    """
    t_values = np.linspace(t0, tf, n_steps + 1)
    y_values = np.zeros(n_steps + 1)
    h = (tf - t0) / n_steps
    y_values[0] = y0
    y = y0
    for i_step in range(n_steps):
        t = t_values[i_step]
        y = euler_step(dydt, t, y, h)
        y_values[i_step + 1] = y

    return t_values, y_values


def plot_solution(t_values,
                  y_values,
                  sol_func=None,
                  x_axis_label="t",
                  y_axis_label="y"):
    """Plot the approximate solution curve
    as given by t_values and y_values,
    and plot analytical solution function sol_func if not None.
    """
    axes = plt.axes()
    # plot markers or dotted line depending on number of points in solution
    if len(t_values) > 51:
        ls = '--'
        mkr = ''
    else:
        ls = ''
        mkr = '.'
    axes.plot(t_values,
              y_values,
              color='C0',
              linestyle=ls,
              marker=mkr)
    if sol_func:
        axes.plot(t_values,
                  sol_func(t_values),
                  color='C3')
        axes.legend(['Euler', 'Analytical'])
    axes.grid(True)
    axes.set_xlabel(x_axis_label)
    axes.set_ylabel(y_axis_label)
    axes.set_title("Solution to a DE by Euler's method")
    plt.show()


def draw_example():
    """Perform several iterations of Euler's method
    and plot the Euler's Method solution"""

    # DE Function
    dydt = lambda t, y: np.exp(-t) - 4 * y

    # Initial conditions
    t0 = 0
    y0 = 5

    # number of steps and final t
    n_steps = 50
    t_final = 20

    # Eulers method with plot of solution
    t_values, y_values = eulers_method_n_steps_t_final(dydt,
                                                       t0,
                                                       y0,
                                                       t_final,
                                                       n_steps)

    plot_solution(t_values, y_values)