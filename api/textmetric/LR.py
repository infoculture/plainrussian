from sklearn.linear_model import LinearRegression
import csv
from math import sqrt
debugMode = True

###########################################################################
# PART 1: PREPARATIONS                                                    #
###########################################################################

def getMetricsFromCSV():
    """
    Reads 'metrics.csv'.
    Returns a list of dictionaries (one for each row).
    """
    with open('metrics.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        listOfDicts =  [row for row in reader]
        
    for d in listOfDicts:
        for key in d:
            if key in ['filename', 'name']: pass            # str
            elif key == 'grade': d[key] = int(d[key])       # int
            elif key == 'wsyllabes': d[key] = eval(d[key])  # dict
            else: d[key] = float(d[key])                    # float
            
    return listOfDicts

###########################################################################

def calculateCoefficients(xs, ys):
    """
    Takes a list of xs and a list of ys, for example:
    * xs: [ (1.2, 3.4), (1.5, 3.3), ... ]
    * ys: [          3,          5, ... ]
    
    Returns a list of coefficients and an intercept,
    such that (hopefully):
        y = x[0] * coef_[0] + x[1] * coef_[1] + intercept
    """
    model = LinearRegression()
    model.fit(xs, ys)
    return (model.coef_, model.intercept_)

###########################################################################
# PART 2: EVALUATION                                                      #
###########################################################################

def checkPredictions(grades, IB_predictions, KD_predictions):
    """
    Takes a list of real grades and two lists of predictions.
    Compares the accuracy of predictions.
    """
    length = len(grades)
    assert len(IB_predictions) == len(KD_predictions) == length
    
    IB_errors = [ pair[0]-pair[1] for pair in zip(IB_predictions, grades)]
    KD_errors = [ pair[0]-pair[1] for pair in zip(KD_predictions, grades)]

    IB_sum_of_errors = sum( abs(e) for e in IB_errors )
    KD_sum_of_errors = sum( abs(e) for e in KD_errors )
    print("Сумма отклонений (ИБ): ", "%.2f" % IB_sum_of_errors)
    print("Сумма отклонений (КД): ", "%.2f" % KD_sum_of_errors)

    #https://ru.wikipedia.org/wiki/Абсолютное_отклонение
    IB_mean_abs_error = IB_sum_of_errors / length
    KD_mean_abs_error = KD_sum_of_errors / length
    print("Среднее абс. отклонение (ИБ): ", "%.2f" % IB_mean_abs_error)
    print("Среднее абс. отклонение (КД): ", "%.2f" % KD_mean_abs_error)

    #https://ru.wikipedia.org/wiki/Среднеквадратическое_отклонение
    IB_sum_of_squares = sum( e**2 for e in IB_errors )
    KD_sum_of_squares = sum( e**2 for e in KD_errors )
    IB_mean_sq_error = sqrt( IB_sum_of_squares / length )
    KD_mean_sq_error = sqrt( KD_sum_of_squares / length )
    print("Среднее кв. отклонение (ИБ): ", "%.2f" % IB_mean_sq_error)
    print("Среднее кв. отклонение (КД): ", "%.2f" % KD_mean_sq_error)
    
###########################################################################
# PART 3: SPECIFIC METRICS                                                #
###########################################################################

def fit_Flesch_Kincaid_grade(listOfDicts):
    """
    Takes data as a list of dictionaries created by 'getMetricsFromCSV()'.
    Returns parameters for F-K formula that best fit the data.
    
    If debugMode is on, checks the accuracy of predictions.
    """
    
    xs = [ (d['avg_slen'], d['avg_syl']) for d in listOfDicts ]
    ys = [ d['grade'] for d in listOfDicts ]
    
    coeffs, intercept = calculateCoefficients(xs, ys)

    if debugMode:
        print("FLESCH-KINCAID GRADE (KD):")
        print("GRADE = {:.2f} * {} + {:.2f} * {} + {:.2f}".format(
               coeffs[0], 'avg_syl', coeffs[1], 'avg_slen', intercept))

        IB_predictions = [ d['index_fk_rus']
                        for d in listOfDicts ]
        KD_predictions = [ x[0]*coeffs[0] + x[1]*coeffs[1] + intercept
                        for x in xs ]
        checkPredictions(ys, IB_predictions, KD_predictions)
                
    return coeffs, intercept
    
###########################################################################

if __name__ == "__main__":

    listOfDicts = getMetricsFromCSV()    
    fit_Flesch_Kincaid_grade(listOfDicts)


