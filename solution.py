import pandas as pd
import numpy as np

from scipy.stats import t


chat_id = 1025787461 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    df = n - 1
    s = np.std(x, ddof=1)
    t_value = t.ppf((1 + p) / 2, df)
    interval = t_value * s / np.sqrt(n)
    mean = np.mean(x)
    return (mean - interval, mean + interval)
