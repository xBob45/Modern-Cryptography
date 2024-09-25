import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
import statsmodels.api as sm
import math
import numpy
import plotly.graph_objs as go


title=""

def getPoints(x1,y1,z1,x2,y2,z2):
    xval=[]
    yval=[]
    zval=[]
    xval.append(0)
    yval.append(0)
    zval.append(0)
    count=0
    for a in range(-10,10):
        for b in range(-10,10):
            xnew=a*x1+b*x2
            xval.append(xnew)

            ynew=a*y1+b*y2
            yval.append(ynew)

            znew=a*z1+b*z2
            zval.append(znew)
    
    return xval,yval,zval


x1,y1,z1 = -5,1,0
x2,y2,z2 = 10,1,13

title = f"x1={x1}, y1={y1}, z1={z1}, x2={x2}, y2={y2}, z2={z2}"

xval, yval, zval = getPoints(x1, y1, z1, x2, y2, z2)    


# Create a 3D scatter plot using Plotly
fig = go.Figure(data=[go.Scatter3d(
    x=xval,
    y=yval,
    z=zval,
    mode='markers',
    marker=dict(
        size=3,
        color=np.sqrt(np.array(xval)**2 + np.array(yval)**2 + np.array(zval)**2),  # Color based on distance from origin
        colorscale='Viridis',
        opacity=0.8
    )
)])


# Update layout for better visuals
fig.update_layout(
    title=title,
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    ),
    width=700,
    margin=dict(r=20, b=10, l=10, t=10)
)

# Show the plot
fig.show()