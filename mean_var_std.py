import numpy as np

# Create a function named calculate() in mean_var_std.py that uses Numpy
# to output the mean, variance, standard deviation, max, min, and sum 
# of the rows, columns, and elements in a 3 x 3 matrix.

# The input of the function should be a list containing 9 digits. 
# The function should convert the list into a 3 x 3 Numpy array, and then return 
# a dictionary containing the mean, variance, standard deviation, max, min, and sum 
# along both axes and for the flattened matrix.

def calculate(list):
    if len(list)< 9:
        raise ValueError("List must contain nine numbers.")
    matrix = np.array(list).reshape(3,3)

    meanA1 = matrix.mean(axis=0).tolist()
    meanA2 = matrix.mean(axis=1).tolist()
    meanFlat = matrix.mean()
  
    varA1 = matrix.var(axis=0).tolist()
    varA2 = matrix.var(axis=1).tolist()
    varFlat = matrix.var()

    stdA1 = matrix.std(axis=0).tolist()
    stdA2 = matrix.std(axis=1).tolist()
    stdFlat = matrix.std()

    maximumA1 = matrix.max(axis=0).tolist()
    maximumA2 = matrix.max(axis=1).tolist()
    maximumFlat = matrix.max()

    minimumA1 = matrix.min(axis=0).tolist()
    minimumA2 = matrix.min(axis=1).tolist()
    minimumFlat = matrix.min()

    sumA1 = matrix.sum(axis=0).tolist()
    sumA2 = matrix.sum(axis=1).tolist()
    sumFlat = matrix.sum()

    calculations = {'mean': [meanA1, meanA2, meanFlat],
                    'variance': [varA1, varA2, varFlat],
                    'standard deviation': [stdA1, stdA2, stdFlat],
                    'max': [maximumA1, maximumA2, maximumFlat],
                    'min': [minimumA1, minimumA2, minimumFlat],
                    'sum': [sumA1, sumA2, sumFlat]}
    
    return calculations


# The returned dictionary should follow this format:

# {
#   'mean': [axis1, axis2, flattened],
#   'variance': [axis1, axis2, flattened],
#   'standard deviation': [axis1, axis2, flattened],
#   'max': [axis1, axis2, flattened],
#   'min': [axis1, axis2, flattened],
#   'sum': [axis1, axis2, flattened]
# }