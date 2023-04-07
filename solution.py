import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1025787461 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    num_bootstraps = 10000
    acceleration_bootstraps = []
    for i in range(num_bootstraps):
        x_bootstrap = np.random.choice(x, size=n, replace=True)
        x_mean_bootstrap = np.mean(x_bootstrap)
        acceleration_bootstrap = 2 * x_mean_bootstrap / (14 ** 2)
        acceleration_bootstraps.append(acceleration_bootstrap)
    acceleration_bootstraps.sort()
    lower_bound_index = int((1 - p) / 2 * num_bootstraps)
    upper_bound_index = int((1 + p) / 2 * num_bootstraps)
    lower_bound = acceleration_bootstraps[lower_bound_index]
    upper_bound = acceleration_bootstraps[upper_bound_index]
    return (lower_bound, upper_bound)
