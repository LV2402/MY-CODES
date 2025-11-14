"""
water_integration.py

Numerical integration methods to estimate daily water consumption:
 - Trapezoidal Rule (composite)
 - Simpson's 1/3 Rule (composite, with hybrid 3/8 if needed)
 - Simpson's 3/8 Rule (composite; falls back to Simpson 1/3 if n not divisible by 3)
 - Gaussian Quadrature (2-point and 3-point)
"""

import numpy as np

# --- Sample (realistic) data: Time in hours, usage in Million Litres/hour ---
x = np.array([0, 4, 8, 12, 16, 20, 24], dtype=float)
y = np.array([120, 150, 220, 300, 260, 180, 140], dtype=float)

# -------------------------
# Trapezoidal (composite)
# -------------------------
def trapezoidal(x, y):
    """Composite trapezoidal rule using numpy.trapz for arbitrary spacing."""
    return np.trapz(y, x)

# -------------------------
# Simpson's 1/3 (composite)
# -------------------------
def simpson13(x, y):
    """
    Composite Simpson's 1/3 rule.
    If number of intervals is odd, a hybrid approach is used:
    - apply Simpson's 3/8 on the first 3 intervals, then Simpson's 1/3 on the rest.
    This ensures robust handling for typical datasets.
    """
    n = len(x) - 1
    if n == 0:
        return 0.0
    # uniform step check (optional)
    h_arr = np.diff(x)
    if not np.allclose(h_arr, h_arr[0]):
        # For non-uniform spacing, fall back to trapezoidal (safer)
        return trapezoidal(x, y)
    h = h_arr[0]

    if n % 2 == 1 and n >= 3:
        # Use Simpson 3/8 on first 3 intervals (4 points), then Simpson 1/3 on remainder
        part1 = simpson38(x[:4], y[:4])
        if len(x) > 4:
            part2 = simpson13(x[3:], y[3:])  # overlap at the join point
        else:
            part2 = 0.0
        return part1 + part2
    elif n % 2 == 1 and n < 3:
        # Not enough intervals for Simpson; fallback to trapezoidal
        return trapezoidal(x, y)

    # Standard composite Simpson 1/3
    s = y[0] + y[-1]
    s += 4.0 * np.sum(y[1:-1:2])
    s += 2.0 * np.sum(y[2:-1:2])
    return (h / 3.0) * s

# -------------------------
# Simpson's 3/8 (composite)
# -------------------------
def simpson38(x, y):
    """
    Composite Simpson's 3/8 rule.
    Works when number of intervals is divisible by 3.
    If not possible, fall back to simpson13 (hybrid handled there).
    """
    n = len(x) - 1
    if n == 0:
        return 0.0
    h_arr = np.diff(x)
    if not np.allclose(h_arr, h_arr[0]):
        return trapezoidal(x, y)
    h = h_arr[0]

    if n % 3 != 0:
        # fallback; caller (simpson13) will handle hybrid usage
        return simpson13(x, y)

    s = y[0] + y[-1]
    for i in range(1, n):
        if i % 3 == 0:
            s += 2.0 * y[i]
        else:
            s += 3.0 * y[i]
    return (3.0 * h / 8.0) * s

# -------------------------
# Gaussian Quadrature
# -------------------------
def gaussian_quadrature(x, y, n_points=2):
    """
    Gaussian quadrature over [a,b] using 2- or 3-point Gauss-Legendre.
    We interpolate y values (linear) at the required sample points.
    """
    a, b = x[0], x[-1]
    mid = 0.5 * (a + b)
    half = 0.5 * (b - a)

    if n_points == 2:
        # nodes and weights for 2-point Gauss-Legendre
        t = np.array([-1.0/np.sqrt(3), 1.0/np.sqrt(3)])
        w = np.array([1.0, 1.0])
    elif n_points == 3:
        t = np.array([-np.sqrt(3/5), 0.0, np.sqrt(3/5)])
        w = np.array([5/9, 8/9, 5/9])
    else:
        raise ValueError("Only 2- and 3-point Gaussian quadrature supported.")

    # function approximator via linear interpolation on (x,y)
    f = lambda xi: np.interp(xi, x, y)

    integral = 0.0
    for wi, ti in zip(w, t):
        xi = mid + half * ti  # map from [-1,1] to [a,b]
        integral += wi * f(xi)
    return half * integral

# -------------------------
# Main: compute and print
# -------------------------
if __name__ == "__main__":
    t_trap = trapezoidal(x, y)
    t_s13 = simpson13(x, y)
    t_s38 = simpson38(x, y)
    t_g2  = gaussian_quadrature(x, y, n_points=2)
    t_g3  = gaussian_quadrature(x, y, n_points=3)

    print("Estimated total water consumption over 24 hours (Million Litres):")
    print(f" - Trapezoidal Rule       : {t_trap:.6f} ML")
    print(f" - Simpson's 1/3 Rule     : {t_s13:.6f} ML")
    print(f" - Simpson's 3/8 Rule     : {t_s38:.6f} ML")
    print(f" - Gaussian Quadrature 2-point : {t_g2:.6f} ML")
    print(f" - Gaussian Quadrature 3-point : {t_g3:.6f} ML")

    # Optional: plot the data and interpolation (uncomment if matplotlib installed)
    # import matplotlib.pyplot as plt
    # xs = np.linspace(x[0], x[-1], 400)
    # ys = np.interp(xs, x, y)
    # plt.plot(x, y, 'o', label='Sample points')
    # plt.plot(xs, ys, '-', label='Linear interp')
    # plt.fill_between(xs, ys, alpha=0.2)
    # plt.xlabel('Time (hours)')
    # plt.ylabel('Water usage (Million Litres/hour)')
    # plt.title('Daily Water Consumption Curve')
    # plt.legend()
    # plt.grid(True)
    # plt.show()
