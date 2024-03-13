from typing import List

def is_shock(curr_time: float, prev_time: float, shock_times: List[float]) -> bool:
    res = False
    if curr_time == prev_time == 0.0:
        res = True
    else:
        for shock_time in shock_times:
            if curr_time < shock_time:
                break
            elif prev_time < shock_time <= curr_time:
                res = True
                break

    return res

def runge_kutta4(y, x, dx, f):
    """computes 4th order Runge-Kutta for dy/dx.
    y is the initial value for y
    x is the initial value for x
    dx is the difference in x (e.g. the time step)
    f is a callable function (y, x) that you supply 
    to compute dy/dx for the specified values.
    """
    
    k1 = dx * f(y, x)
    k2 = dx * f(y + 0.5*k1, x + 0.5*dx)
    k3 = dx * f(y + 0.5*k2, x + 0.5*dx)
    k4 = dx * f(y + k3, x + dx)
    
    return y + (k1 + 2*k2 + 2*k3 + k4) / 6.