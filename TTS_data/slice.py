# coding:utf-8
import numpy as np
import pandas as pd

def data_4(l):
    rng = np.random.default_rng()
    data0 = rng.permutation(l, axis=0)
    dat_e=data0[:data0.shape[0]]     # 0.05 , 7个
    dat_k=data0[10:20]
    dat_r=data0[:10]
    sim_t=data0[:10]
    sim_e=data0[20:25]
    return dat_e,dat_k,dat_r,sim_t,sim_e

def t_14():
    d0 = np.loadtxt( '0.csv', delimiter=',')
    d1 = np.loadtxt( '1.csv', delimiter=',')
    d2 = np.loadtxt( '2.csv', delimiter=',')
    d3 = np.loadtxt( '3.csv', delimiter=',')
    d4 = np.loadtxt( '4.csv', delimiter=',')
    d5 = np.loadtxt( '5.csv', delimiter=',')
    d6 = np.loadtxt( '6.csv', delimiter=',')
    d7 = np.loadtxt( '7.csv', delimiter=',')
    d0,t0,r0,s0,v0 = data_4(d0)
    d1,t1,r1,s1,v1 = data_4(d1)
    d2,t2,r2,s2,v2 = data_4(d2)
    d3,t3,r3,s3,v3 = data_4(d3)
    d4,t4,r4,s4,v4 = data_4(d4)
    d5,t5,r5,s5,v5 = data_4(d5)
    d6, t6, r6,s6,v6 = data_4(d6)
    d7, t7, r7,s7,v7 = data_4(d7)
    label = np.loadtxt('label.csv', delimiter=',')

    l=label[:d0.shape[0]].T
    d = np.concatenate((d0, d1, d2, d3, d4, d5,d6,d7), axis=0)
    l = l.reshape(-1)

    t = label[:t0.shape[0]].T
    dt = np.concatenate((t0,t1,t2,t3,t4,t5,t6,t7), axis=0)
    t = t.reshape(-1)

    s = label[:r0.shape[0]].T
    dr = np.concatenate((r0, r1, r2, r3, r4,r5,r6,r7), axis=0)
    s = s.reshape(-1)

    a_0=label[:s0.shape[0]].T
    a_s=np.concatenate((s0, s1, s2, s3, s4,s5,s6,s7), axis=0)
    a_0 = a_0.reshape(-1)

    b_0 = label[:v0.shape[0]].T
    b_s = np.concatenate((v0, v1, v2, v3, v4, v5, v6, v7), axis=0)
    b_0 = b_0.reshape(-1)

    return d,l,dt,t,dr,s,a_s,a_0,b_s,b_0


data,label,dt,t,dr,s,a_s,a_0,b_s,b_0=t_14()

data=pd.DataFrame(data.reshape(data.shape[0],-1))
label=pd.DataFrame(label)


data.to_csv('train.csv',header=False,index=False)
label.to_csv('tr_la.csv',header=False,index=False)



