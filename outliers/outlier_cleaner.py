#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    from scipy import stats
    errors = []
    for i in range(len(predictions)):
        errors.append(abs(net_worths[i]-predictions[i]))
    ranks = stats.rankdata(errors,'max')
    for i in range(len(errors)):
        if (ranks[i] <= .9*len(errors)):
            cleaned_data.append((ages[i], net_worths[i], errors[i]))
    print len(cleaned_data)
    return cleaned_data
