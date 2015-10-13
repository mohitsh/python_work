import numpy as np
import matplotlib.pyplot as plt
import pandas

import statsmodels
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

x = np.linspace(-5,5,21)
X,Y = np.meshgrid(x,x)
np.random.seed(1)

Z = -5 +3*X -0.5*Y + 8*np.random.normal(size = X.shape)
X = X.flatten()
Y = Y.flatten()
Z = Z.flatten()

data = pandas.DataFrame({'x':X,'y':Y,'z':Z})
model = ols("z~x+y",data).fit()
print model.summary()
