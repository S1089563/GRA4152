import argparse, textwrap

#Logistic regression function
def my_logistic_regression(penalty, fit_intercept, max_iter, tol):
    from sklearn.linear_model import LogisticRegression

    #define a logistic regression model with your input parameters
    clf = LogisticRegression(penalty=penalty, fit_intercept=fit_intercept, max_iter=max_iter, tol=tol)
    return clf



#create argparse object and description
parser = argparse.ArgumentParser(prog="Logistic Regression estimation",
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 #1.
                                 description=textwrap.dedent(
                                     '''\
                                        Logistic regression estimation
                                     -----------------------------------
                                     In order to estimate a Logistic regression, you need to specify 4 parameters:
                                       a. penalty ("l1","l2" (default),"elasticnet", None): specifies the norm of the penalty
                                       b. fit_intercept (bool): specifies if a constant (bias or intercept) should be added to the decision function
                                       c. max_iter (int, default = 100): max. number of iterations taken for the solvers to converge
                                       d. tol (float, default = 1e-4): tolerance for the stopping criteria'''),
                                #2.
                                 epilog=textwrap.dedent(
                                     '''\
                                        --------------------------------
                                        The model used is borrowed from sklearn, for more information you can go to:
                                        https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
                                        '''
                                 )   
                                 )
parser.print_help()

#3.
parser.add_argument('--penalty', default='l2', choices=['l1', 'l2', 'elasticnet', None],
                    help='specifies the norm of the penalty.\
                        Can be one of the follwing values: "l1", "l2", "elasticnet", None')
#4
parser.add_argument('--fit_intercept', action='store_false',
                    help='Specifies if an intercept should be added to the decision function.\
                        If given, its value is True')
#5
parser.add_argument('--tol', type=float, default=1e-4
                    ,help='Specifies the tolerance for the stopping criteria. Its default value is 1e-4')
parser.add_argument('--max_iter', type=int, default=100,
                    help='max. number of iterations taken for the solvers to converge. Its default value is 100')

args = parser.parse_args()
print(args)

