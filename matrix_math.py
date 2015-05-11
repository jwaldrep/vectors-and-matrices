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

    """
    m = [3, 4]
    v = [1, 3, 0]

    assert shape(m) == (2,)
    assert shape(v) == (3,)
    assert shape([1]) == (1,)
    """

def matrix_vector_multiply(x, y):
    pass
def matrix_matrix_multiply(x, y):
    pass
def matrix_scalar_multiply(x, y):
    pass
def matrix_col(x, y):
    pass
def matrix_row(x, y):
    pass
def magnitude(x):
    pass
def vector_mean(x, y):
    pass
def vector_multiply(x, y):
    pass
def dot(x, y):
    pass
def vector_sum(x, y):
    pass
def vector_sub(x, y):
    pass
def vector_add(x, y):
    pass
