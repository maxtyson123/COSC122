import numpy as np

from EMTH119.common.euler import eulers_method_n_steps_t_final, plot_solution


def plot_DE():
    """Perform several iterations of Euler's method
    and plot the Euler's Method solution"""

    # DE Function
    dydt = lambda t, y:  (5 * y) / (t**2) - y/2

    # Initial conditions
    t0 = 2
    y0 = 4

    # number of steps and final t
    n_steps = 30
    t_final = 8

    # Eulers method with plot of solution
    t_values, y_values = eulers_method_n_steps_t_final(dydt,
                                                       t0,
                                                       y0,
                                                       t_final,
                                                       n_steps)

    plot_solution(t_values, y_values)

def eulers_method_n_steps_list_t_final(dydt, t0, y0, tf, n_steps):
    """Do n_steps steps of Euler's method from t0 to tf.
       DE function dydt(t, y), initial t = t0, initial y = y0,
       to final t tf, n_steps steps.
       Return Python lists of t and y values.
    """
    return [ eulers_method_n_steps_t_final(dydt,t0,y0,tf, steps)[1][-1] for steps in n_steps ]

dydt = lambda t, y : (np.cos(t) - y) / (t + 1)
t0 = 0
y0 = 1
t_final = 1
n_steps_list = [2, 4, 8]
soln_list = eulers_method_n_steps_list_t_final(dydt,
                                               t0,
                                               y0,
                                               t_final,
                                               n_steps_list)
for i_soln in range (len(soln_list)):
    print(f"With {n_steps_list[i_soln]} steps,",
          f" solution = {soln_list[i_soln]:.4f}")

y = lambda x : (np.sin(x) + 1) / (x + 1)
print(f" solution = {y(1):.4f}")