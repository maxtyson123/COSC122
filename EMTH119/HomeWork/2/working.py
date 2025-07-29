import numpy as np

from EMTH119.common.euler import eulers_method_n_steps_t_final, plot_solution


def question_6():
    """Use Euler’s method with 50 steps to solve the differential equation"""

    # DE Function
    dydt = lambda t, y: -3*t*y

    # Initial conditions
    t0 = 0
    y0 = 3

    # number of steps and final t
    n_steps = 50
    t_final = 2

    # Eulers method with plot of solution
    t_values, y_values = eulers_method_n_steps_t_final(dydt,
                                                       t0,
                                                       y0,
                                                       t_final,
                                                       n_steps)

    plot_solution(t_values, y_values)
    print(f"Question 6: {y_values[-1]:.4f}")

def question_7():
    """Use Euler’s method with [50,100, 200, 1000] steps to solve the differential equation"""

    # DE Function
    dydt1 = lambda t, y: 4*t-y
    dydt2 = lambda t, y: t + 2*t*y
    dydt  = [dydt1, dydt2]

    # Initial conditions
    t0 = 0
    y0 = [4, 3]

    # number of steps and final t
    n_steps = [50,100, 200, 1000]
    t_final = [2,1]

    # Eulers method with plot of solution
    for i in [0,1]:
        for steps in n_steps:
            t_values, y_values = eulers_method_n_steps_t_final(dydt[i],
                                                               t0,
                                                               y0[i],
                                                               t_final[i],
                                                               steps)

            plot_solution(t_values, y_values)
            print(f"Question 7: {i} | {steps} {' ' * ( 4 - len(str(steps))) } | {y_values[-1]:.4f}")

question_6()
question_7()