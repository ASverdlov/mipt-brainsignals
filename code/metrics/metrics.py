import numpy as np

def _check_features_array(A):
    return A

def _check_array(Y):
    return Y

def _check_regression_answers(Y_true, Y_pred):
    '''

    :param Y_true:
    :param Y_pred:
    :return:
    '''
    if Y_true.ndim == 1:
        Y_true = Y_true.reshape((-1, 1))

    if Y_pred.ndim == 1:
        Y_pred = Y_pred.reshape((-1, 1))

    return Y_true, Y_pred


def residual_square_sum(Y_true, Y_pred):
    """
    Residual sum of squares.

    :param Y_true: array-like of shape = (n_samples) or (n_samples, n_features)
        True responses.

    :param Y_pred: array-like of shape = (n_samples) or (n_samples, n_features)
        Predicted responses.

    :return score: float
        Value of metric.
    """
    Y_true, Y_pred = _check_regression_answers(Y_true, Y_pred)

    score = ((Y_true - Y_pred) ** 2).sum()

    return score


def total_square_sum(Y_true):
    """
    Total sum of squares.

<<<<<<< HEAD
    :param Y_true: array-like of shape = (n_samples) or (n_samples, n_features)
        True responses.

    :return score: float
        Value of metric.
    """
    Y_true = _check_array(Y)
=======
    :param Y_true:
    :return:
    '''
    Y_true = _check_array(Y_true)
>>>>>>> 09f69cc4550ef63d6a7ab97c8b187ba11fe54e90

    score = ((Y_true - Y_true.mean()) ** 2).sum()

    return score


def determination_coefficient(Y_true, Y_pred, adjusted=True):
    """

    :param Y_true:
    :param Y_pred:
    :param adjusted:
    :return:
    """
    rss = residual_square_sum(Y_true, Y_pred)
    tss = total_square_sum(Y_true)
    #print("RSS", "TSS", rss, tss)
    if adjusted:
        # check Y_pred is 2d
        m, k = Y_true.shape
        #print("M", "K", m, k)
        score = 1 - (rss / tss) * ((m - k) / (m - 1))
    else:
        score = 1 - rss / tss
    #print(score)
    return score


def variance_inflation_factor(Y_true, Y_pred):
    '''

    :param Y_true:
    :param Y_pred:
    :return:
    '''

    r2 = determination_coefficient(Y_true, Y_pred)
    score = 1 / (1 - r2)

    return score


<<<<<<< HEAD
def mallowss_Cp(Y_true, Y_pred, Y_pred_p, p):
    """
=======
def mallows_Cp(Y_true, Y_pred, Y_pred_p, p):
    '''
>>>>>>> 09f69cc4550ef63d6a7ab97c8b187ba11fe54e90

    :param Y_true:
    :param Y_pred:
    :param Y_pred_p:
    :param p:
    :return:
    """
    m = Y_true.shape[0]

    # check that p is int or bool array
    rss = residual_square_sum(Y_true, Y_pred)
    rss_p = residual_square_sum(Y_true, Y_pred_p)

    score = rss_p / rss - m + 2 * p
    return score

def bayesian_information_criterion(Y_true, Y_pred, p):
    '''

    :return:
    '''
    m = Y_true.shape[0]

    rss = residual_square_sum(Y_true, Y_pred)
    score = rss + p * np.log(m)

    return score

def condition_number_xtx(X):
    '''

    :param X:
    :return:
    '''
    X = _check_array(X)

    eigenvalues = (np.linalg.svd(X)[1]) ** 2
    eigenvalues = eigenvalues[np.nonzero(eigenvalues)]
    l_max, l_min = np.max(eigenvalues), np.min(eigenvalues)
    score = l_max / l_min

    return score


