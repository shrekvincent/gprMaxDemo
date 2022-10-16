import os
import numpy as np
from gprMax.gprMax import api
from tools.outputfiles_merge import get_output_data, merge_files
 
 
 
#文件路径+文件名
dmax=os.getcwd() #项目目录
filename = os.path.join(dmax,'dancenggangjinBscan.in')
print(filename)
#正演  n：仿真次数（A扫描次数）->B扫描，
api(filename, n=50)  
merge_files("liutaolunwenBscan", removefiles=True)
 
# 获取回波数据
# A B扫描时out文件名不一样
filename = os.path.join(dmax,"dancenggangjin_merged.out")
rxnumber = 1
rxcomponent = 'Ez'
outputdata, dt = get_output_data(filename, rxnumber, rxcomponent)
print(outputdata)
# 保存回波数据
#np.savetxt('Bscan_merged.txt',outputdata,delimiter=' ')
 
## B扫描绘图
from tools.plot_Bscan import mpl_plot
plt = mpl_plot(filename,outputdata, dt*1e9, rxnumber, rxcomponent)
plt.ylabel('Time [ns]')
plt.show()
