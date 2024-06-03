# coding:utf-8
import numpy as np
import torch
from matplotlib import pyplot as plt
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

"""
d0 = np.loadtxt('0x.csv',delimiter=',')
d1 = np.loadtxt('1x.csv',delimiter=',')

plt.subplots(figsize=(5.8, 5))
yl = range(1, 501)
plt.plot(yl, d0[:,0],c='r', label='few_train')
plt.plot(yl, d0[:,1],'--', c='b', label='few_val')
plt.xticks(fontproperties='Times New Roman', size=15)
plt.yticks(fontproperties='Times New Roman', size=15)
plt.xlabel('epoch', fontsize=15)
plt.ylabel('loss', fontsize=15)
plt.legend(['Tra_train', 'Tra_val'], fontsize=15)
plt.show()

plt.subplots(figsize=(5.8, 5))
yl = range(1, 501)
plt.plot(yl, d1[:,0], c='r', label='Full_train')
plt.plot(yl, d1[:,1],'--',  c='b', label='Full_val')
plt.xticks(fontproperties='Times New Roman', size=15)
plt.yticks(fontproperties='Times New Roman', size=15)
plt.xlabel('epoch', fontsize=15)
plt.ylabel('loss', fontsize=15)
plt.legend(['Full_train', 'Full_val'], fontsize=15)
plt.show()

"""

d0 = np.loadtxt('mix_loss.csv',delimiter=',')

plt.subplots(figsize=(5.8, 4.9))
yl = range(1, 501)
plt.plot(yl, d0[:,1], c='r', label='train')
plt.plot(yl, d0[:,0], c='b', label='val')
plt.xticks(fontproperties='Times New Roman', size=15)
plt.yticks(fontproperties='Times New Roman', size=15)
plt.xlabel('epoch', fontsize=15)
plt.ylabel('loss', fontsize=15)
plt.legend(['train', 'val'], fontsize=15)
plt.show()



