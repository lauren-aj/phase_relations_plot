#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


# In[11]:


fig,axs = plt.subplots(1,1,figsize=(8,6))
plt.rcParams["font.family"] = 'Cambria'
line = 6
mark = 10

######## making a hexagon out of triangles
# top vertice of all triangles at centre point of hexagon
# x-axis between -1 and 1
# y-axis between -2 and 2
# can change these numbers but need to keep the proportions

# right top traingle
p1 = np.array([[0,0],[1,1],[0,2]]) 
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = 'red')
axs.add_patch(p1)
# right triangle
p1 = np.array([[0,0],[1,1],[1,-1]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = 'blue')
axs.add_patch(p1)
#right bottom
p1 = np.array([[0,0],[1,-1],[0,-2]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = 'yellow')
axs.add_patch(p1)
# bottom left
p1 = np.array([[0,0],[-1,-1],[0,-2]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = 'green')
axs.add_patch(p1)
#left
p1 = np.array([[0,0],[-1,1],[-1,-1]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = 'pink')
axs.add_patch(p1)
#top left
p1 = np.array([[0,0],[-1,1],[0,2]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = 'purple')
axs.add_patch(p1)

#####
#change facecolor to white to keep the shape but lose the colouring
#just need the x-y coordinates to make more shapes 


plt.xlim(-2,2)
plt.ylim(-2,2)
plt.rcParams["font.family"] = 'Cambria'
plt.rcParams['hatch.linewidth'] = 3
plt.rcParams["axes.edgecolor"] = "black"
plt.rcParams["axes.linewidth"] = 1.4
plt.show()
#plt.savefig("sub_minerals.png", format="png", dpi=1000,bbox_inches='tight')
#plt.close()


# In[12]:


fig,axs = plt.subplots(1,1,figsize=(8,6))
plt.rcParams["font.family"] = 'Cambria'
line = 6
mark = 10

######## making a hexagon out of triangles
# top vertice of all triangles at centre point of hexagon
# x-axis between -1 and 1
# y-axis between -2 and 2
# can change these numbers but need to keep the proportions

# right top traingle
p1 = np.array([[0,0],[-0.5,1],[0.5,1]]) 
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = 'red')
axs.add_patch(p1)
# right triangle
p1 = np.array([[0,0],[0.5,1],[1,0]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = 'blue')
axs.add_patch(p1)
#right bottom
p1 = np.array([[0,0],[1,0],[0.5,-1]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = 'yellow')
axs.add_patch(p1)
# bottom left
p1 = np.array([[0,0],[-0.5,-1],[0.5,-1]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = 'green')
axs.add_patch(p1)
#left
p1 = np.array([[0,0],[-0.5,-1],[-1,0]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = 'pink')
axs.add_patch(p1)
#top left
p1 = np.array([[0,0],[-1,0],[-0.5,1]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = 'purple')
axs.add_patch(p1)

#####
#change facecolor to white to keep the shape but lose the colouring
#just need the x-y coordinates to make more shapes 


plt.xlim(-2,2)
plt.ylim(-2,2)
plt.rcParams["font.family"] = 'Cambria'
plt.rcParams['hatch.linewidth'] = 3
plt.rcParams["axes.edgecolor"] = "black"
plt.rcParams["axes.linewidth"] = 1.4
plt.show()
#plt.savefig("sub_minerals.png", format="png", dpi=1000,bbox_inches='tight')
#plt.close()


# In[49]:


fig,axs = plt.subplots(1,1,figsize=(8,6))
plt.rcParams["font.family"] = 'Cambria'
line = 6
mark = 10

######## making a octogon out of triangles
# top vertice of all triangles at centre point of hexagon
# x-axis between -1 and 1
# y-axis between -2 and 2
# can change these numbers but need to keep the proportions

# top right traingle
p1 = np.array([[0,0],[0,1],[0.5,0.6]]) 
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = 'red')
axs.add_patch(p1)
# right triangle
p1 = np.array([[0,0],[0.5,0.6],[0.6,0]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = 'blue')
axs.add_patch(p1)

p1 = np.array([[0,0],[0.5,-0.6],[0.6,0]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = 'blue')
axs.add_patch(p1)
#right bottom
p1 = np.array([[0,0],[0.5,-0.6],[0,-1]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = 'yellow')
axs.add_patch(p1)

# top right traingle
p1 = np.array([[0,0],[0,-1],[-0.5,-0.6]]) 
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = 'red')
axs.add_patch(p1)
# right triangle
p1 = np.array([[0,0],[-0.5,-0.6],[-0.6,0]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = 'blue')
axs.add_patch(p1)

p1 = np.array([[0,0],[-0.5,0.6],[-0.6,0]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = 'blue')
axs.add_patch(p1)
#right bottom
p1 = np.array([[0,0],[-0.5,0.6],[0,1]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = 'yellow')
axs.add_patch(p1)

#####
#change facecolor to white to keep the shape but lose the colouring
#just need the x-y coordinates to make more shapes 


plt.xlim(-2,2)
plt.ylim(-2,2)
plt.rcParams["font.family"] = 'Cambria'
plt.rcParams['hatch.linewidth'] = 3
plt.rcParams["axes.edgecolor"] = "black"
plt.rcParams["axes.linewidth"] = 1.4
plt.show()
#plt.savefig("sub_minerals.png", format="png", dpi=1000,bbox_inches='tight')
#plt.close()


# In[ ]:


#subduction points
GPC900 = [1300,1]
GPC901 = [1400,1]
GPC902 = [1100,1]
YPC625 = [1300,1.5]

fig,axs = plt.subplots(1,1,figsize=(8,6))
plt.rcParams["font.family"] = 'Cambria'
line = 6
mark = 10

plt.text(GPC900[0]-60, GPC900[1]+0.17, '1 GPa, 1300 °C', fontsize = 15)
plt.text(GPC900[0]-30, GPC900[1]+0.11, '~24 hrs', fontsize = 15)
#Silicate melt #4F3395 - right top - purple 
p1 = np.array([[GPC900[0],GPC900[1]],[GPC900[0]+15,GPC900[1]+0.04],[GPC900[0],GPC900[1]+0.08]]) 
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "#4F3395")    #
axs.add_patch(p1)
#Sulphate melt #FFCC00 - right - yellow
p1 = np.array([[GPC900[0],GPC900[1]],[GPC900[0]+15,GPC900[1]+0.04],[GPC900[0]+15,GPC900[1]-0.04]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "#FFCC00")
axs.add_patch(p1)
#Sillimanite #4B7DCD - right bottom - blue
p1 = np.array([[GPC900[0],GPC900[1]],[GPC900[0]+15,GPC900[1]-0.04],[GPC900[0],GPC900[1]-0.08]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "#4B7DCD")
axs.add_patch(p1)
#Spinel #26744D - bottom left green
p1 = np.array([[GPC900[0],GPC900[1]],[GPC900[0]-15,GPC900[1]-0.04],[GPC900[0],GPC900[1]-0.08]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "white")
axs.add_patch(p1)
#Anhydrite #BC003F - top left - red
p1 = np.array([[GPC900[0],GPC900[1]],[GPC900[0]-15,GPC900[1]+0.04],[GPC900[0],GPC900[1]+0.08]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "white")
axs.add_patch(p1)
#Quartz  #F57323 - left - orange
p1 = np.array([[GPC900[0],GPC900[1]],[GPC900[0]-15,GPC900[1]+0.04],[GPC900[0]-15,GPC900[1]-0.04]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "white")
axs.add_patch(p1)


#GPC901
plt.text(GPC901[0]-50, GPC901[1]+0.17, '1 GPa, 1400 °C', fontsize = 15)
plt.text(GPC901[0]-20, GPC901[1]+0.11, '~2 hrs', fontsize = 15)
#Silicate melt #4F3395 - right top - purple
p1 = np.array([[GPC901[0],GPC901[1]],[GPC901[0]+15,GPC901[1]+0.04],[GPC901[0],GPC901[1]+0.08]]) 
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "#4F3395")
axs.add_patch(p1)
#Sulphate melt #FFCC00 - right - yellow
p1 = np.array([[GPC901[0],GPC901[1]],[GPC901[0]+15,GPC901[1]+0.04],[GPC901[0]+15,GPC901[1]-0.04]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "#FFCC00")
axs.add_patch(p1)
#Sillimanite #4B7DCD - right bottom - blue
p1 = np.array([[GPC901[0],GPC901[1]],[GPC901[0]+15,GPC901[1]-0.04],[GPC901[0],GPC901[1]-0.08]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "white")
axs.add_patch(p1)
#Spinel #26744D - bottom left green
p1 = np.array([[GPC901[0],GPC901[1]],[GPC901[0]-15,GPC901[1]-0.04],[GPC901[0],GPC901[1]-0.08]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "white")
axs.add_patch(p1)
#Anhydrite #BC003F - top left - red
p1 = np.array([[GPC901[0],GPC901[1]],[GPC901[0]-15,GPC901[1]+0.04],[GPC901[0],GPC901[1]+0.08]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "white")
axs.add_patch(p1)
#Quartz  #F57323 - left - orange
p1 = np.array([[GPC901[0],GPC901[1]],[GPC901[0]-15,GPC901[1]+0.04],[GPC901[0]-15,GPC901[1]-0.04]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "white")
axs.add_patch(p1)

#GPC902
plt.text(GPC902[0]-55, GPC902[1]+0.17, '1 GPa, 1100 °C', fontsize = 15)
plt.text(GPC902[0]-25, GPC902[1]+0.11, '~24 hrs', fontsize = 15)
#Silicate melt #4F3395 - right top - purple
p1 = np.array([[GPC902[0],GPC902[1]],[GPC902[0]+15,GPC902[1]+0.04],[GPC902[0],GPC902[1]+0.08]]) 
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "#4F3395")
axs.add_patch(p1)
#Sulphate melt #FFCC00 - right - yellow
p1 = np.array([[GPC902[0],GPC902[1]],[GPC902[0]+15,GPC902[1]+0.04],[GPC902[0]+15,GPC902[1]-0.04]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "white")
axs.add_patch(p1)
#Sillimanite #4B7DCD - right bottom - blue
p1 = np.array([[GPC902[0],GPC902[1]],[GPC902[0]+15,GPC902[1]-0.04],[GPC902[0],GPC902[1]-0.08]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "white")
axs.add_patch(p1)
#Spinel #26744D - bottom left green
p1 = np.array([[GPC902[0],GPC902[1]],[GPC902[0]-15,GPC902[1]-0.04],[GPC902[0],GPC902[1]-0.08]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "#26744D")
axs.add_patch(p1)
#Anhydrite #BC003F - top left - red
p1 = np.array([[GPC902[0],GPC902[1]],[GPC902[0]-15,GPC902[1]+0.04],[GPC902[0],GPC902[1]+0.08]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "#BC003F")
axs.add_patch(p1)
#Quartz  #F57323 - left - orange
p1 = np.array([[GPC902[0],GPC902[1]],[GPC902[0]-15,GPC902[1]+0.04],[GPC902[0]-15,GPC902[1]-0.04]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "#F57323")
axs.add_patch(p1)

#YPC625
plt.text(YPC625[0]-55, YPC625[1]+0.17, '1.5 GPa, 1300 °C', fontsize = 15)
plt.text(YPC625[0]-25, YPC625[1]+0.11, '~26 hrs', fontsize = 15)
#Silicate melt #4F3395 - right top - purple
p1 = np.array([[YPC625[0],YPC625[1]],[YPC625[0]+15,YPC625[1]+0.04],[YPC625[0],YPC625[1]+0.08]]) 
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "#4F3395")
axs.add_patch(p1)
#Sulphate melt #FFCC00 - right - yellow
p1 = np.array([[YPC625[0],YPC625[1]],[YPC625[0]+15,YPC625[1]+0.04],[YPC625[0]+15,YPC625[1]-0.04]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "#FFCC00")
axs.add_patch(p1)
#Sillimanite #4B7DCD - right bottom - blue
p1 = np.array([[YPC625[0],YPC625[1]],[YPC625[0]+15,YPC625[1]-0.04],[YPC625[0],YPC625[1]-0.08]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "#4B7DCD")
axs.add_patch(p1)
#Spinel #26744D - bottom left green
p1 = np.array([[YPC625[0],YPC625[1]],[YPC625[0]-15,YPC625[1]-0.04],[YPC625[0],YPC625[1]-0.08]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "white")
axs.add_patch(p1)
#Anhydrite #BC003F - top left - red
p1 = np.array([[YPC625[0],YPC625[1]],[YPC625[0]-15,YPC625[1]+0.04],[YPC625[0],YPC625[1]+0.08]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "white")
axs.add_patch(p1)
#Quartz  #F57323 - left - orange
p1 = np.array([[YPC625[0],YPC625[1]],[YPC625[0]-15,YPC625[1]+0.04],[YPC625[0]-15,YPC625[1]-0.04]])
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "#F57323")
axs.add_patch(p1)

axs.set_ylim(0.5,2)
axs.set_ylabel('Pressure (GPa)', fontsize=25, fontname = 'Cambria')
#axs.yaxis.set_label_coords(-0.06, 0.76)
axs.set_xlim(1000,1500)
axs.tick_params(axis='both',labelsize = 25)
axs.set_xlabel('Temperature (°C)', fontsize =25, fontname = 'Cambria')
axs.tick_params(axis="x", pad=10)
axs.label_outer()


################
# Legend 
#Silicate melt #4F3395 - right top - purple
silT = 1010
silP = 1.9
p1 = np.array([[silT,silP],[silT+15,silP+0.04],[silT,silP+0.08]]) 
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "#4F3395")
axs.add_patch(p1)
plt.text(silT+20, silP+0.02, 'Silicate Melt', fontsize = 15)
#Sulphate melt #FFCC00 - right - yellow
T = 1010
P = 1.8
p1 = np.array([[T,P],[T+15,P+0.04],[T,P+0.08]]) 
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "#FFCC00")
axs.add_patch(p1)
plt.text(T+20, P+0.02, 'Sulphate Melt', fontsize = 15)
#Sillimanite #4B7DCD - right bottom - blue
T = 1010
P = 1.7
p1 = np.array([[T,P],[T+15,P+0.04],[T,P+0.08]]) 
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "#4B7DCD")
axs.add_patch(p1)
plt.text(T+20, P+0.02, 'Sillimanite', fontsize = 15)
#Spinel #26744D - bottom left green
T = 1010
P = 1.6
p1 = np.array([[T,P],[T+15,P+0.04],[T,P+0.08]]) 
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "#26744D")
axs.add_patch(p1)
plt.text(T+20, P+0.02, 'Spinel', fontsize = 15)
#Anhydrite #BC003F - top left - red
T = 1010
P = 1.5
p1 = np.array([[T,P],[T+15,P+0.04],[T,P+0.08]]) 
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "#BC003F")
axs.add_patch(p1)
plt.text(T+20, P+0.02, 'Anhydrite', fontsize = 15)
#Quartz  #F57323 - left - orange
T = 1010
P = 1.4
p1 = np.array([[T,P],[T+15,P+0.04],[T,P+0.08]]) 
p1 = Polygon(p1, edgecolor='black', alpha = 1, facecolor = "#F57323")
axs.add_patch(p1)
plt.text(T+20, P+0.02, 'Quartz', fontsize = 15)

plt.rcParams["font.family"] = 'Cambria'
plt.rcParams['hatch.linewidth'] = 3
plt.rcParams["axes.edgecolor"] = "black"
plt.rcParams["axes.linewidth"] = 1.4
plt.show()
#plt.savefig("sub_minerals.png", format="png", dpi=1000,bbox_inches='tight')
#plt.close()


# In[ ]:




