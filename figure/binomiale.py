from pylab import *
from scipy.special import loggamma as lgamma

figure('binomiale', figsize=[ 4.51,  2.7 ]).set_tight_layout(True)
clf()

binom = lambda k, n, p: exp(lgamma(1 + n) - lgamma(1 + k) - lgamma(1 + n - k)) * p**k * (1-p)**(n-k)

n = 5

ks = arange(n + 1)

bar(ks, binom(ks, n, 0.5), label="$p=%.1f$" % 0.5, width=.8, color='gray')
bar(ks, binom(ks, n, 0.8), label="$p=%.1f$" % 0.8, width=.5, color='lightgray')
	
xlabel('$k$')
ylabel('$P(k;n,p)$')

legend(loc=0)

savefig('binomiale.pdf')