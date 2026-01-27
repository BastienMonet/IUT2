import numpy as np


X = np.array([[6, 7], [5, 6], [7, 4]])
new_x = np.array([[7,7]])

y = np.array([1, 1, 0])

def un_plus_proche(X, new_x, y):
    # X - new_x will broadcast new_x across all rows of X
    distances = np.linalg.norm(X - new_x, axis=1)
    nearest_index = np.argmin(distances)
    return y[nearest_index]