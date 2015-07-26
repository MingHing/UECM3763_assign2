import pylab as p
import numpy as np

#Setup parameters
alpha = 1; theta = 0.064; sigma = 0.27; R0 = 3;
n_path = 1000; n = 1000; t = 1.0;

#Create Brownian paths
dt = t/n
T = p.linspace(0,t,n+1)[:-1]
dB = p.randn(n_path,n+1)*p.sqrt(dt)
dB[:,0]=0
B = dB.cumsum(axis=1)
R = p.zeros_like(B)
R[:,0] = R0
col = 0
for col in range (n):
  R[:,col+1] = R[:,col] + alpha*(theta - R[:,col])*dt + sigma*R[:,col]*dB[:,col+1]
#Plot 5 realizations of mean reversal process
R_plot = R[0:5,:-1]
p.plot(T,R_plot.transpose())
p.xlabel('Time,$t$')
p.ylabel('R(t)')
p.title('5 realization of mean reversal process with $\\alpha$ = '+ str(alpha)+ ', $\\theta$ = '+str(theta)+ ' and $\\sigma$ = '+str(sigma))
p.show()

#Calculate
R1 = R[:,-1]
E_R1 = np.mean(R1)
print('The expectation value, E[R(1)] = ' +str(E_R1))
mask = R1 > 2
P_R1_2 = sum (mask) / n_path
print('P[R(1) > 2] = ' +str(P_R1_2))
