import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import seaborn as sns
import matplotlib.patches as mpatches
pd.set_option('display.max_columns',None)
df = pd.read_csv('World Cup.csv')
df = df[ (df['fixture'] == 'France v Argentina')  & (df['player'] == 'Lionel Messi') & (df['event_type'] == 'Pass')]
df = df.reset_index(drop=True)
df['x'] = df['x']*1.3
df['y'] = df['y']*.9
df['pass_end_x'] = df['pass_end_x']*1.3
df['pass_end_y'] = df['pass_end_y']*.9
fig, ax = plt.subplots()
fig.set_size_inches(7, 5)

for i in range(len(df)):
    plt.plot([df["x"][i],df["pass_end_x"][i]],
             [df["y"][i],df["pass_end_y"][i]], 
             color="blue")
    plt.plot(df["x"][i],df["y"][i],"o", color="green") 
    #Create figure
fig=plt.figure()
fig.set_size_inches(7, 5)
ax=fig.add_subplot(1,1,1)

#Pitch Outline & Centre Line
plt.plot([0,0],[0,90], color="black")
plt.plot([0,130],[90,90], color="black")
plt.plot([130,130],[90,0], color="black")
plt.plot([130,0],[0,0], color="black")
plt.plot([65,65],[0,90], color="black")

#Left Penalty Area
plt.plot([16.5,16.5],[65,25],color="black")
plt.plot([0,16.5],[65,65],color="black")
plt.plot([16.5,0],[25,25],color="black")

#Right Penalty Area
plt.plot([130,113.5],[65,65],color="black")
plt.plot([113.5,113.5],[65,25],color="black")
plt.plot([113.5,130],[25,25],color="black")

#Left 6-yard Box
plt.plot([0,5.5],[54,54],color="black")
plt.plot([5.5,5.5],[54,36],color="black")
plt.plot([5.5,0.5],[36,36],color="black")

#Right 6-yard Box
plt.plot([130,124.5],[54,54],color="black")
plt.plot([124.5,124.5],[54,36],color="black")
plt.plot([124.5,130],[36,36],color="black")

#Prepare Circles
centreCircle = plt.Circle((65,45),9.15,color="black",fill=False)
centreSpot = plt.Circle((65,45),0.8,color="black")
leftPenSpot = plt.Circle((11,45),0.8,color="black")
rightPenSpot = plt.Circle((119,45),0.8,color="black")

#Draw Circles
ax.add_patch(centreCircle)
ax.add_patch(centreSpot)
ax.add_patch(leftPenSpot)
ax.add_patch(rightPenSpot)

#Prepare Arcs
leftArc = Arc((11,45),height=18.3,width=18.3,angle=0,theta1=310,theta2=50,color="black")
rightArc = Arc((119,45),height=18.3,width=18.3,angle=0,theta1=130,theta2=230,color="black")

#Draw Arcs
ax.add_patch(leftArc)
ax.add_patch(rightArc)

#Tidy Axes
plt.axis('off')
success = ''
for i in range(len(df)):
    if df['outcome'][i] == 1:
        success = 'green'
    else: 
        success = 'red'
    plt.plot([df["x"][i],df["pass_end_x"][i]],[df["y"][i],df["pass_end_y"][i]], color=success,label = 'Inline label')
    plt.plot(df["x"][i],df["y"][i],"o", color="blue")
    plt.plot(df["pass_end_x"][i],df["pass_end_y"][i],"o", color="black")
#plt.legend(('Start','Stop','Completed', 'Incomplete'),
#           loc='upper right')
plt.title('Messi vs France (World Cup 2018)')
#Display Pitch
red_patch = mpatches.Patch(color='red', label='Incomplete')
green_patch = mpatches.Patch(color='green', label='Complete')
white_patch = mpatches.Patch(color='blue', label='Pass Start')
black_patch = mpatches.Patch(color='black', label='Pass End')

plt.legend(handles=[red_patch,green_patch,white_patch,black_patch],loc = 'upper right')
plt.show()
plt.savefig('Messi_vs_France.png')

#from plotly import __version__
#from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
#plotly.tools.set_credentials_file(username='kmkrieg', api_key='F80NQI41ebRomwnRz2hS')
#data = []
#figure = go.Figure()
#for i in range(len(df)):
#    if df['outcome'][i] == 1:
#        success = 'green'
#    else: 
#        success = 'red'
#    #plt.plot([df["x"][i],df["pass_end_x"][i]],[df["y"][i],df["pass_end_y"][i]], color=success)
#    start = go.Scatter(x=df['x'][i],y=df['y'][i])
#    end = go.Scatter(x=df['pass_end_x'][i],y=df['pass_end_y'][i])
#    data = [start, end]
#    figure.append_trace(data,i,i)
#py.offline.iplot(figure, filename='force-displacement-data', image='jpeg')