import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1025787461 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    mean_x = np.mean(x) 
    std_x = np.std(x, ddof=1) 
    vt = np.vectorize(lambda t: mean_x + t * std_x / np.sqrt(n))
    v = np.vectorize(lambda x: x / 14)
    velocities = v(x)
    mean_v = np.mean(velocities)
    std_v = np.std(velocities, ddof=1)
    t_value = t.ppf(1 - p / 2, n - 1)
    left_bound = vt(mean_v - t_value)
    right_bound = vt(mean_v + t_value)# Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return left_bound, right_bound
