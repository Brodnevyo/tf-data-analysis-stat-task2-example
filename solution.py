import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1025787461 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    std_dev = np.sqrt(2) / np.sqrt(n)
    z_value = norm.ppf((1 + p) / 2)
    interval = z_value * std_dev
    mean = np.mean(x)
    distance_interval = (mean - interval, mean + interval)
    acceleration_interval = tuple(2 * d / 14**2 for d in distance_interval)
    return acceleration_interval
