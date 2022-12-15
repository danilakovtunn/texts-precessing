import numpy as np

def kfold_split(num_objects, num_folds):
    """Split [0, 1, ..., num_objects - 1] into equal num_folds folds (last fold can be longer) and returns num_folds train-val 
       pairs of indexes.

    Parameters:
    num_objects (int): number of objects in train set
    num_folds (int): number of folds for cross-validation split

    Returns:
    list((tuple(np.array, np.array))): list of length num_folds, where i-th element of list contains tuple of 2 numpy arrays,
                                       the 1st numpy array contains all indexes without i-th fold while the 2nd one contains
                                       i-th fold
    """
    lst = []
    indexes = set(np.arange(num_objects))
    kol = num_objects//num_folds
    j = 0
    for i in range(num_folds):
        fold = np.arange(j, j + kol)
        if i == num_folds - 1:
            fold = np.arange(j, num_objects)
        j += kol
        lst.append( (np.array(list(indexes^set(fold))), fold) )
    return lst

def knn_cv_score(X, y, parameters, score_function, folds, knn_class):
    """Takes train data, counts cross-validation score over grid of parameters (all possible parameters combinations) 

    Parameters:
    X (2d np.array): train set
    y (1d np.array): train labels
    parameters (dict): dict with keys from {n_neighbors, metrics, weights, normalizers}, values of type list,
                       parameters['normalizers'] contains tuples (normalizer, normalizer_name), see parameters
                       example in your jupyter notebook
    score_function (callable): function with input (y_true, y_predict) which outputs score metric
    folds (list): output of kfold_split
    knn_class (obj): class of knn model to fit

    Returns:
    dict: key - tuple of (normalizer_name, n_neighbors, metric, weight), value - mean score over all folds
    """
    dict = {}
    
    for normalizers in parameters['normalizers']:

        for i in range(len(folds)):
            X_train = X[folds[i][0]]
            y_train = y[folds[i][0]]

            X_test = X[folds[i][1]]
            y_test = y[folds[i][1]]

            if normalizers[0] is not None:
                normalizers[0].fit(X_train)
                X_train = normalizers[0].transform(X_train)
                X_test = normalizers[0].transform(X_test)

            for n_neighbors in parameters['n_neighbors']:
                for metrics in parameters['metrics']:
                    for weights in parameters['weights']:
                        KNN = knn_class(n_neighbors=n_neighbors, metric=metrics, weights=weights)
                        KNN.fit(X_train, y_train)

                        y_predict = KNN.predict(X_test)

                        if (normalizers[1], n_neighbors, metrics, weights) not in dict.keys():
                            dict[(normalizers[1], n_neighbors, metrics, weights)] = score_function(y_test, y_predict) / len(folds)
                        else:
                            dict[(normalizers[1], n_neighbors, metrics, weights)] += score_function(y_test, y_predict) / len(folds)

    return dict