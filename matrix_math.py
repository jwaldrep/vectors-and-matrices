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

def vector_walk(x, y, op=sum):
    if shape(x) != shape(y):
        raise ShapeException
    try:
        return [op([x_val, y[idx_r][idx_c]])
                for idx_r, row in enumerate(x)
                for idx_c, x_val in row]
    except TypeError:
        return [x_val + y[idx_r] for idx_r, x_val in enumerate(x)]

def vector_add(x, y):
    return vector_walk(x, y, op=sum)

def vector_sub(x, y):
    pass
def vector_sum(x, y):
    pass
def dot(x, y):
    pass
def vector_multiply(x, y):
    pass
def vector_mean(x, y):
    pass
def magnitude(x):
    pass
def matrix_row(x, y):
    pass
def matrix_col(x, y):
    pass
def matrix_scalar_multiply(x, y):
    pass
def matrix_matrix_multiply(x, y):
    pass
def matrix_vector_multiply(x, y):
    pass
