import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize as opt
from scipy import stats as sta

sig_3tev = np.array([ [0.5,1.23,0.0023] , [0.75,1.007,0.0027] , [0.9,0.901,0.0014] , [1.0,0.847,0.0021] , [1.1,0.792,0.0017] , [1.25,0.729,0.0014] , [1.5,0.682,0.0014] ])
sig_6tev = np.array([ [0.5,2.701,0.011] , [0.75,2.341,0.0060] , [0.9,2.146,0.0036] , [1.0,2.021,0.0104] , [1.1,1.970,0.0057] , [1.25,1.844,0.0095] , [1.5,1.730,0.0043] ])
sig_clic = np.array([ [0.5,0.89,0.0010] , [0.90,0.664,0.0010] , [1.0,0.621,0.0010] , [1.1,0.586,0.0010] , [1.5,0.491,0.0010] ])

def fit_parab(x,a,b,c):
	return a*x**2 + b*x + c

p3tev,c3tev = opt.curve_fit(fit_parab,sig_3tev[:,0],sig_3tev[:,1],p0=[1.0,-2.0,0.5],sigma=sig_3tev[:,2])
p6tev,c6tev = opt.curve_fit(fit_parab,sig_6tev[:,0],sig_6tev[:,1],p0=[1.5,-2.0,1.0],sigma=sig_6tev[:,2])
pclic,cclic = opt.curve_fit(fit_parab,sig_clic[:,0],sig_clic[:,1],p0=[1.5,-2.0,1.0],sigma=sig_clic[:,2])

print(p3tev)
print(c3tev)
chis3,pchi3 = sta.chisquare(sig_3tev[:,1],fit_parab(sig_3tev[:,1],p3tev[0],p3tev[1],p3tev[2]),ddof=3)
print(chis3)
print(pchi3)

print(p6tev)
print(c6tev)

print(pclic)
print(cclic)

xfit = np.linspace(min(sig_3tev[:,0])-0.1,max(sig_3tev[:,0])+0.1,num=50)
yfit3 = fit_parab(xfit,p3tev[0],p3tev[1],p3tev[2])
yfit6 = fit_parab(xfit,p6tev[0],p6tev[1],p6tev[2])
yfitc = fit_parab(xfit,pclic[0],pclic[1],pclic[2])

plt.grid(b='on',which='major',axis='both',alpha=0.9,aa=True)

plt.errorbar(sig_3tev[:,0],sig_3tev[:,1],yerr=sig_3tev[:,2],fmt='r.',label='_nolegend_')
plt.errorbar(sig_6tev[:,0],sig_6tev[:,1],yerr=sig_6tev[:,2],fmt='b.',label='_nolegend_')
plt.errorbar(sig_clic[:,0],sig_clic[:,1],yerr=sig_clic[:,2],fmt='g.',label='_nolegend_')

lb0 = '$\mu^+\mu^-$ Collider:'
p0, = plt.plot([1],[1],'w.',label='$\mu^+\mu^-$ Collider:')
lb1 = "$\sqrt{s}=6\ TeV$"
p1, = plt.plot(xfit,yfit6,'b-',linewidth=2,label="$\sqrt{s}=6\ TeV$")
lb2 = "$\sqrt{s}=3\ TeV$"
p2, = plt.plot(xfit,yfit3,'r-',linewidth=2,label="$\sqrt{s}=3\ TeV$")
lb3 = '$e^+e^-$ Collider:'
p3, = plt.plot([1],[1],'w.',linewidth=2,label='$e^+e^-$ Collider:')
lb4 = "$\sqrt{s}=3\ TeV$"
p4, = plt.plot(xfit,yfitc,'g-',linewidth=2,label="$\sqrt{s}=3\ TeV$")

plt.legend()
l1 = plt.legend([p0,p1,p2],[lb0,lb1,lb2],loc=1)
l2 = plt.legend([p3,p4],[lb3,lb4], loc=3)
plt.gca().add_artist(l1)

plt.ylim(ymin=0)

plt.xlabel("$\lambda / \lambda_{SM}$",horizontalalignment='right',fontsize=18)
plt.ylabel("$\sigma (fb)$       ",verticalalignment='top',rotation='horizontal',fontsize=18)
plt.title("Two-Higgs Cross Section vs. Higgs Self-Coupling")

plt.show()
