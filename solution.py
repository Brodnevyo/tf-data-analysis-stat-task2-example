import pandas as pd
import numpy as np

rom scipy import stats


chat_id = 1025787461 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    x = 2 * x / 14**2
    n = len(x)
    mean = np.median(x)
    std = np.std(x, ddof=1)
    t = stats.t.ppf((1 + p) / 2, n - 1)
    lower = mean - t * std / np.sqrt(n)
    upper = mean + t * std / np.sqrt(n)
    return (lower, upper)
