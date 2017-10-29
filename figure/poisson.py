from pylab import *
from scipy.special import loggamma as lgamma

figure('poissoniana', figsize=[ 4.51,  2.7 ]).set_tight_layout(True)
clf()

poisson = lambda k, mu: exp(k * log(mu) - lgamma(k + 1) - mu)

n = 10

ks = arange(n + 1)

bar(ks, poisson(ks, 2), label="$\\mu=2$", width=.8, color='gray')
bar(ks, poisson(ks, 5), label="$\\mu=5$", width=.5, color='lightgray')
	
xlabel('$k$')
ylabel('$P(k;\mu)$')

legend(loc=0)

savefig('poisson.pdf')