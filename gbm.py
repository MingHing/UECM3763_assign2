import pylab as p
import numpy as np

# Setup parameters
mu = 0.1; sigma = 0.26; S0 = 39;
n_path = 1000;   #number of simulations
n = 1000;        #number of partitions

# Create Brownian paths
t = p.linspace(0,3,n+1);
dB = p.randn(n_path, n+1) / p.sqrt(n/3); dB[:,0] = 0;
B = dB.cumsum(axis=1);  #cumulative sum of each row

# Calculate stock prices
nu = mu - sigma*sigma/2.0
S = p.zeros_like(B); S[:,0] = S0
S[:,1:] = S0*p.exp(nu*t[1:]+sigma*B[:,1:])

#Plot 5 realizations of GBM
S5 = S[0:5]
p.plot(t,S5.transpose())
p.xlabel('Time , $t$')
p.ylabel('Stock price, $RM$')
p.title('5 realization of GBM with $\mu$ =' + str(mu) + ' and $\sigma$ =' +str(sigma))
p.show()

#Calculate
S3 = p.array(S[:,-1])
E_S3 = np.mean(S3)
Var_S3 = np.var(S3)
print('Expectation value of S(3)= ' + str(E_S3))
print('Variance of S(3)= ' + str(Var_S3))

mask = S3 > 39
P_S3 = sum(mask) / len(mask)
S3_39 = S3 * mask
E_S3_39 = sum(S3_39) / sum(mask)
print('P[S(3) > 39] = ' +str(P_S3))
print('E[S(3) | S(3)>39] = ' +str(E_S3_39))
