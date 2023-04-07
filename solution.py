import pandas as pd
import numpy as np

from scipy import stats


chat_id = 1025787461 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    mean = np.mean(x)
    std = np.std(x, ddof=1)
    t = stats.t.ppf((1 + p) / 2, n - 1)
    left = mean - t * std / np.sqrt(n)
    right = mean + t * std / np.sqrt(n)
    return (left, right)
