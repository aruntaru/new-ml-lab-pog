'''
Implement the non-parametric Locally Weighted Regression algorithm in order to
fit data points. Select appropriate data set for your experiment and draw graphs.

'''
import numpy as np
from bokeh.plotting import figure, show
from bokeh.layouts import gridplot

def plot_lwr(tau):
    # prediction
    domain = np.linspace(-3, 3, num=300)
    prediction = [local_regression(x0, X, Y, tau) for x0 in domain]
    plot = figure(plot_width=400, plot_height=400)
    plot.title.text = 'tau=%g' % tau
    plot.scatter(X, Y, alpha=.3)
    plot.line(domain, prediction, line_width=2, color='red')
    return plot

def local_regression(x0, X, Y, tau):
    # add bias term
    x0 = np.r_[1, x0] # r_ => Translates slice objects to concatenation along the first axis
    X = np.c_[np.ones(len(X)), X] # c_ => Translates slice objects to concatenation along the second axis.
    # fit model: normal equations with kernel
    xw = X.T * radial_kernel(x0, X, tau)
    beta = np.linalg.pinv(xw @ X) @ xw @ Y
    # predict value
    return x0 @ beta

def radial_kernel(x0, X, tau):
    return np.exp(np.sum((X - x0) ** 2, axis=1) / (-2 * tau * tau))

n = 1000
# generate dataset
X = np.linspace(-3, 3, num = n)
Y = np.log(np.abs(X ** 2 - 1) + .5)
# jitter X (Draw random samples from a normal (Gaussian) distribution)
X += np.random.normal(scale=.1, size=n)

show(gridplot([
    [plot_lwr(10.), plot_lwr(1.)],
    [plot_lwr(0.1), plot_lwr(0.01)]
]))





