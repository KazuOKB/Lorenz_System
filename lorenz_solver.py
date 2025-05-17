#!/usr/bin/env python3
import numpy as np

# Lorenz system parameters
SIGMA = 10.0
RHO = 110.0
BETA = 8.0 / 3.0

def lorenz(t, state):
    """
    Lorenz system:
      dx/dt = SIGMA * (y - x)
      dy/dt = RHO * x - y - x * z
      dz/dt = -BETA * z + x * y
    """
    x, y, z = state
    dx = SIGMA * (y - x)
    dy = RHO * x - y - x * z
    dz = -BETA * z + x * y
    return np.array([dx, dy, dz])

def rk4_step(f, t, state, dt):
    """Perform one Runge-Kutta 4th order step."""
    k1 = f(t, state)
    k2 = f(t + dt / 2.0, state + dt * k1 / 2.0)
    k3 = f(t + dt / 2.0, state + dt * k2 / 2.0)
    k4 = f(t + dt, state + dt * k3)
    return state + dt * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0

def integrate(f, t0, state0, dt, tmax):
    """Integrate ODE using fixed-step RK4 from t0 to tmax."""
    n_steps = int((tmax - t0) / dt)
    t = t0
    state = np.array(state0, dtype=float)
    # Prepare array to hold time and states: [t, x, y, z]
    traj = np.zeros((n_steps + 1, 4))
    traj[0] = [t, *state]
    for i in range(1, n_steps + 1):
        state = rk4_step(f, t, state, dt)
        t += dt
        traj[i] = [t, *state]
    return traj

if __name__ == '__main__':
    # Integration settings
    dt = 0.002
    tmax = 100.0
    initial_state = [1.0, 1.0, 1.0]

    # Run integration
    trajectory = integrate(lorenz, 0.0, initial_state, dt, tmax)

    # Save results to file
    np.savetxt('lorentz_data.txt', trajectory, fmt='%.6f', header='t x y z')
    print('Integration complete. Results saved to lorentz_data.txt')