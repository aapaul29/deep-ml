import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	m_old, n_old = len(a), len(a[0])
	m, n = new_shape[0], new_shape[1]
	if m_old * n_old != m * n:
		return []
	return np.array(a).reshape(new_shape).tolist()