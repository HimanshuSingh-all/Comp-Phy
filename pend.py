



import numpy as np 
import matplotlib.pyplot as plt

## vec is of the form [t x dx/dt]
gamma=0.0
g=9.8
def rhs(vec):
    return np.array( [1,vec[2], -gamma*vec[2]-g*np.sin(vec[1]) ] )


def mod_euler(init_vec:list, t_final, step):
    
    soln=np.array([init_vec])
    while step+soln[-1,0]<t_final:

        tmpv= soln[-1,:]+step*rhs(soln[-1,:]) 
        soln=np.vstack( [ soln, soln[-1,:]+step/2*(rhs(soln[-1,:]) + rhs(tmpv) )] )
        ##soln[-1, :]
        #print(soln[-1])
    return soln

def euler_cromer(init_vec:list, t_final, step):
    
    soln=np.array([init_vec])
    while step+soln[-1,0]<t_final:
        soln=np.vstack([soln, soln[-1]])
        soln[-1,0]+=step
        for i in range(1,soln.shape[1]):
            print(i)
            soln[-1,soln.shape[1]-i]+=rhs(soln[-1])[soln.shape[1]-i]*step
    return soln

init=[0,0.05,0.0]
t_final=10

soln=mod_euler(init,t_final,0.1)
soln1=euler_cromer(init,t_final,0.1)
#plt.plot(soln[:,0],soln[:,1])
plt.plot(soln1[:,0],soln1[:,1])
plt.show()
