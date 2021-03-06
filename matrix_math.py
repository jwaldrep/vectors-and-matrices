import functools
import math


class ShapeException(Exception):
    pass


def shape(array):
    """Take a vector or matrix and return a tuple with the
    number of rows (for a vector) or the number of rows and columns
    (for a matrix.)"""
    try:
        return (len(array), len(array[0]))
    except TypeError:
        return (len(array),)


def vector_walk(x, y, op=sum, filter=lambda x_, y_: True):
    if shape(x) != shape(y):
        raise ShapeException
    try:
        return [op([x_val, y[idx_r][idx_c]])
                for idx_r, row in enumerate(x)
                for idx_c, x_val in row
                if filter(idx_r, idx_c)
                ]
    except TypeError:
        return [op([x_val, y[idx_r]]) for idx_r, x_val in enumerate(x)]


def sub(a_list):
    if len(a_list) != 2:
        raise ShapeException
    return a_list[0] - a_list[1]


def times(a_list):
    if len(a_list) != 2:
        raise ShapeException
    return a_list[0] * a_list[1]


def is_equal(idx_x, idx_y):
    return idx_x == idx_y


def vector_add(x, y):
    return vector_walk(x, y, op=sum)


def vector_sub(x, y):
    return vector_walk(x, y, op=sub)


def vector_sum(*vectors):
    return functools.reduce(vector_add, vectors)


def dot(x, y):
    return sum(vector_walk(x, y, op=times, filter=is_equal))


def vector_multiply(x, scalar):
    scalar_matrix = vector_walk(x, x, op=lambda x_: scalar)
    return vector_walk(x, scalar_matrix, op=times)


def vector_mean(*vectors):
    sum_vector = vector_sum(*vectors)
    n = len(vectors)
    return vector_multiply(sum_vector, 1 / n)


def magnitude(x):
    return math.sqrt(dot(x, x))


def matrix_row(x, n):
    return x[n]


def matrix_col(x, n):
    return [val for row in x for idx, val in enumerate(row) if idx == n]


def matrix_cols(x):
    for col in [val for row in x for idx, val in enumerate(row)]:
        yield col


def matrix_scalar_multiply(matrix, scalar):
    return [[i*scalar for i in row] for row in matrix]


def matrix_vector_multiply(matrix, vector):
    if shape(matrix)[1] != shape(vector)[0]:
        raise ShapeException

    step1 = [[val * vector[idx] for idx, val in enumerate(row)]
             for row in matrix]
    return [sum(x) for x in step1]


def matrix_matrix_multiply(x, y):
    if shape(x)[1] != shape(y)[0]:
        raise ShapeException

    y_transposed = [[row[i] for row in y] for i in range(len(y[0]))]

    return [[dot(row, col) for col in y_transposed] for row in x]

    # return [[dot(matrix_row(x, j), matrix_row(y_transposed, i))
    #         for i, val in enumerate(row)]
    #         for j, row in enumerate(x)]

    # return [[dot(row, val) for i,val in enumerate(matrix_cols(y))
    #        if j < len(y)]
    #        for j, row in enumerate(x)]
