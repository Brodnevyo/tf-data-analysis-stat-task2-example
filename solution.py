import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1025787461 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    x_mean = np.median(x)
    s = np.std(x, ddof=1)
    t_value = t.ppf((1 + p) / 2, n - 1)
    margin_of_error = t_value * s / np.sqrt(n)
    lower_bound = x_mean - margin_of_error
    upper_bound = x_mean + margin_of_error
    acceleration_lower_bound = 2 * lower_bound / (14 ** 2)
    acceleration_upper_bound = 2 * upper_bound / (14 ** 2)
    return (acceleration_lower_bound, acceleration_upper_bound)
