import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1025787461 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    mean = np.mean(x)
    std = np.std(x, ddof=1)
    n = len(x)
    t_left = stats.t.ppf((1 - p) / 2, n - 1)
    t_right = stats.t.ppf((1 + p) / 2, n - 1)
    left = mean + t_left * std / np.sqrt(n)
    right = mean + t_right * std / np.sqrt(n)
    return left, right
