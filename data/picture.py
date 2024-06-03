# coding:utf-8
import numpy as np
from matplotlib import pyplot as plt
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"



n_d=np.loadtxt('noise/0.csv',delimiter=',')
d_n_d = np.loadtxt('de_noise/0.csv',delimiter=',')
nor_d = np.loadtxt( 'nor_data/0.csv',delimiter=',')

n1 = n_d[800:880]
d1 = d_n_d[800:880]
nor1 = nor_d[800:880]
"""
plt.figure(figsize=(12,15), dpi=80)
plt.figure(1)
ax1 = plt.subplot(611)
yl = range(1, 81)
plt.plot(yl, n1[:,0],'--', label='noise')
plt.plot(yl, d1[:,0], label='delete_noise')
plt.xticks([])
plt.yticks(fontproperties='Times New Roman', size=15)

ax2 = plt.subplot(612)
yl = range(1, 81)
plt.plot(yl, n1[:,1],'--', label='few_train')
plt.plot(yl, d1[:,1], label='few_train')
plt.xticks([])
plt.yticks(fontproperties='Times New Roman', size=15)

ax3 = plt.subplot(613)
yl = range(1, 81)
plt.plot(yl, n1[:,2],'--', label='few_train')
plt.plot(yl, d1[:,2], label='few_train')
plt.xticks([])
plt.yticks(fontproperties='Times New Roman', size=15)

ax4 = plt.subplot(614)
yl = range(1, 81)
plt.plot(yl, n1[:,3],'--', label='few_train')
plt.plot(yl, d1[:,3], label='few_train')
plt.xticks([])
plt.yticks(fontproperties='Times New Roman', size=15)

ax5 = plt.subplot(615)
yl = range(1, 81)
plt.plot(yl, n1[:,4],'--', label='few_train')
plt.plot(yl, d1[:,4], label='few_train')
plt.xticks([])
plt.yticks(fontproperties='Times New Roman', size=15)

ax6 = plt.subplot(616)
yl = range(1, 81)
plt.plot(yl, n1[:,5],'--', label='few_train')
plt.plot(yl, d1[:,5], label='few_train')
plt.xticks(fontproperties='Times New Roman', size=15)
plt.yticks(fontproperties='Times New Roman', size=15)
plt.xlabel('time spot', fontsize=15)
plt.show()

"""
plt.figure(figsize=(12,15), dpi=80)
plt.figure(1)
ax1 = plt.subplot(611)
yl = range(1, 81)
plt.plot(yl, nor1[:,0],c='r', label='nor')
plt.xticks([])
plt.yticks(fontproperties='Times New Roman', size=15)

ax2 = plt.subplot(612)
yl = range(1, 81)
plt.plot(yl, nor1[:,1],c='m', label='nor')
plt.xticks([])
plt.yticks(fontproperties='Times New Roman', size=15)

ax3 = plt.subplot(613)
yl = range(1, 81)
plt.plot(yl, nor1[:,2],c='g', label='nor')
plt.xticks([])
plt.yticks(fontproperties='Times New Roman', size=15)

ax4 = plt.subplot(614)
yl = range(1, 81)
plt.plot(yl, nor1[:,3],c='y', label='nor')
plt.xticks([])
plt.yticks(fontproperties='Times New Roman', size=15)

ax5 = plt.subplot(615)
yl = range(1, 81)
plt.plot(yl, nor1[:,4],c='blue', label='nor')
plt.xticks([])
plt.yticks(fontproperties='Times New Roman', size=15)

ax6 = plt.subplot(616)
yl = range(1, 81)
plt.plot(yl, nor1[:,5],c='b', label='nor')
plt.xticks(fontproperties='Times New Roman', size=15)
plt.yticks(fontproperties='Times New Roman', size=15)
plt.xlabel('time spot', fontsize=15)

plt.show()


