import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    # 将长度为9的列表转化为3*3的numpy矩阵
    matrix = np.array(list).reshape(3,3)
    mean = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean()]
    variance = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var()]
    sd = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std()]
    max = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max()]
    min = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min()]
    sum = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum()]

    calculations = {
    'mean': mean,
    'variance': variance,
    'standard deviation': sd,
    'max': max,
    'min': min,
    'sum': sum
    }
    return calculations