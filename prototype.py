import matplotlib.pylab as plt
import numpy as np
import scipy.integrate

# this code generates plots of the drug mass over time for two different models and 
# demonstrates the use of numerical integration to solve the corresponding ODE system.

def dose(t, X):
      """
    Function to calculate the dose at time t.
    Returns the value of X.
    """
    return X

def rhs(t, y, Q_p1, V_c, V_p1, CL, X):
      """
    Function to calculate the derivatives of q_c and q_p1.
    Represents the right-hand side of the ODE system.
    """
    q_c, q_p1 = y
    transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
    dqc_dt = dose(t, X) - q_c / V_c * CL - transition
    dqp1_dt = transition
    return [dqc_dt, dqp1_dt]

model1_args = {
    'name': 'model1',
    'Q_p1': 1.0,
    'V_c': 1.0,
    'V_p1': 1.0,
    'CL': 1.0,
    'X': 1.0,
}

model2_args = {
    'name': 'model2',
    'Q_p1': 2.0,
    'V_c': 1.0,
    'V_p1': 1.0,
    'CL': 1.0,
    'X': 1.0,
}

t_eval = np.linspace(0, 1, 1000) # Creating an array of time points for evaluation
y0 = np.array([0.0, 0.0]) # Initial condition array for q_c and q_p1

fig = plt.figure() # Creating a figure object for plotting
for model in [model1_args, model2_args]:
    args = [
        model['Q_p1'], model['V_c'], model['V_p1'], model['CL'], model['X']
    ]
    sol = scipy.integrate.solve_ivp(
        fun=lambda t, y: rhs(t, y, *args),
        t_span=[t_eval[0], t_eval[-1]],
        y0=y0, t_eval=t_eval
    )
    plt.plot(sol.t, sol.y[0, :], label=model['name'] + '- q_c')
    plt.plot(sol.t, sol.y[1, :], label=model['name'] + '- q_p1')

plt.legend()  # Displaying legend
plt.ylabel('drug mass [ng]')  # Labeling y-axis
plt.xlabel('time [h]')  # Labeling x-axis
plt.show()  # Displaying the plot
