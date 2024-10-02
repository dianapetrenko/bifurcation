import matplotlib.pyplot as plt
import numpy as np
import time
from math_utils import Histogram


# def euler_recursive(t, y, h, n):
#     global iter
#     iter += 1
#     # Base case: stop when t exceeds n
#     y_new = y + h * 10*y*(1-y)
#     if iter >= n or abs(y_new - y) < eps:
#         return y
#     else:
#         # Recursive call with updated time and y
#         print(f"Approximate solution at iter={iter} t={t} is y={y_new}")
#         # n_coords.append(t)
#         # y_coords.append(y_new)

#         return euler_recursive(t + h, y_new, h, n)


def euler_loop(y, h, n):
    """
    Find solutions to the logistic equation using Euler's 
    approximation method
    ======================
    t = t_(n-1) + h
    h = increment value
    y = approximation at t
    n = number of iterations
    ======================
    output:
    y_new = the new solution found after each iteration
    y_values = ALL of the solutions found (NOT convergences)
    """
    y_values = []
    # iteration counter
    iter = 0
    # initialize to y0
    y_new = y
    # find all solutions up to the specified num of iterations
    while iter < n:
        # logistic function
        y_new = y + h * 10*y*(1-y)
        iter += 1
        # t += h   
        # save solution into array
        y_values.append(y_new)
        # print(f"Approximate solution at iter={iter} t={t} is y={y_new}")
        # 
        if abs(y_new - y) < eps:
            break
        y = y_new

    return y_new, y_values

    
if __name__ == "__main__":
    # precision
    eps = 10**-5
    xmin = 0
    xmax = 1.4
    nbins = int(
        (xmax - xmin) / 10**-8
    )
    threshold = 0.95
    h_min = 0.18
    h_max = 0.3
    histogram = Histogram(xmin, xmax, nbins)

    # Initial conditions
    # x0 = 0
    y0 = 0.1
    # y0 = 0.45
    n_iter_max = 10**3

    Xs = []
    Ys = []
    h_values = np.arange(h_min, h_max, 0.001)

    start = time.time()

    for h in h_values:
        histogram.reset_freqs()
        y_approx, y_approxes = euler_loop(y0, h, n_iter_max)

        # Discard the first 20 % of data as it's not converged
        y_start = int(len(y_approxes) * 0.2)
        # discard 20% of the initial run
        for y in y_approxes[y_start:]:
            histogram.add(y)
        # x = np.arange(0, len(y_approxes))
        # print(histogram.freqs)
        bins = histogram.get_bins_above_threshold(threshold)
        # print(bins)
        for bin in bins:
            value = histogram.get_x(bin)
            Xs.append(h)
            Ys.append(value)
            # print(value)

    end = time.time()
    runtime = end - start
    print(f"{runtime=} seconds")

    # print(Xs)
    # print(Ys)

    plt.xlim(h_min, h_max)
    plt.ylim(xmin, xmax)

    plt.scatter(Xs, Ys, s=0.05)
    plt.show()
