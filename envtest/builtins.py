import numpy as np
from scipy.ndimage import gaussian_filter
from scipy import misc
import io
import pandas as pd


__all__ = ['rand_array', 'smooth_image', 'my_mat_solve', 'summarize_csv_text']


def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)

def my_mat_solve(A, b):
    return A.inv()*b

def summarize_csv_text(csv_text: str):
    df = pd.read_csv(io.StringIO(csv_text))
    return df.describe()