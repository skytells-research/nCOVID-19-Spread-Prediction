# Skytells AI Research
# nCOVID-19 Spread Prediction
# Created 27/03/2020
# Updated 04/04/2020
import numpy as np

def sir_step(S, I, b, k):
    """
    compute partial derivatives for the SIR disease spread model
    """

    S_dot = -b*S*I
    I_dot = b*S*I - k*I
    R_dot = k*I
    return S_dot, I_dot, R_dot

def sir_simulate(steps, I0, b, k):
    """
    run SIR disease spread simulation

    steps - number of days to simulate
    I0 - initially infected population rate
    b - transition rate from S to I
    k - transition rate from I to R

    Is - infected population rate by day
    Rs - recovered population rate by day
    """

    Ss = np.empty((steps + 1))
    Is = np.empty((steps + 1))
    Rs = np.empty((steps + 1))

    Ss[0] = 1
    Is[0] = I0
    Rs[0] = 0

    for i in range(steps):
        S_dot, I_dot, R_dot = sir_step(Ss[i], Is[i], b, k)
        Ss[i + 1] = Ss[i] + S_dot
        Is[i + 1] = Is[i] + I_dot
        Rs[i + 1] = Rs[i] + R_dot

    return Is, Rs
