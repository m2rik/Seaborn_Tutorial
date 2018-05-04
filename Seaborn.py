
#Simple Seaborn Tutorial, p. = palette
#used to stylize and visualize matplot libs plots and graphics, 
#fitting in and visualizing linear regression models
#plot time series data
#based on numpy and matplotlib

import numpy as np
import seaborn as sb 
import pandas as pd 
from matplotlib import pyplot as plt 

df =sb.load_dataset('tips')
#print df.head()

#print sb.get_dataset_names() #There are a no. of datasets included in the package,view them using this


#Comes with features for figure aesthetics
#customized themes and high lever interface for customizing and controlling the look of matplotlib Figures.

#A default Matplotlib plot looks like:



def sinplot(flip=1):
	x=np.linspace(0,20,100)
	for i in range(1,5):
		plt.plot(x,np.sin(x+i*.5)*(7-i)*flip)
sinplot()
plt.show()


#The same plot can be changed to seaborn result using the set() function.
sb.set()
sinplot()
plt.show()


#Seaborn splits the matplotlib parameters into plot styles and scales.
#there are different types of themes available: Darkgrid ,White,Dark,White,Ticks.
sb.set_style('whitegrid')
sinplot()
plt.show()

#remove the axis spines using 
sb.despine()
plt.show()

#We can override the elements, customize various paramters
print sb.axes_style()#shows the available customization options.

#The scale of plots can be set using the function
#set_context()

#Seaborn provides a color pallate which can be used to give colors to our plots,differrent paramters that can be customized are shown below.
#desat = proportion to desaturate each other.
#n_color = no.of coolors in the palette.
sb.color_palette(palette = None, n_colors = None, desat = None)

#Seaborn.palplot() also deals with the color palettes- it plots hte color p. as horizontal arrays.
current_palette=sb.color_palette()
sb.palplot(current_palette)
plt.show()

#There are sequential color palettesto express the distribution of data from relatively lower ot higher valeus in a range.
sb.palplot(sb.color_palette('Greens')) #can append s in the eg.
plt.show()

#Then there are diverging colro palettes whihc show a plot ranging from -1 to +1
#show them by the color codes. ("BrBG", 7)

#seaborn.distplot() gives a dist of the dataset.

#eg.
df = sb.load_dataset('iris')
sb.distplot(df['petal_length'],kde = False) #kernel estimation plot is removed.
#kde=kernel destiny estimates-stimate pdf of a continous random variable.used for non parametrix analysis
sb.distplot(df['petal_length'],hist=False)
plt.show()

#just the distplot will display the parametric dist of the dataset.
sb.distplot(df['petal_length'])
plt.show()

#jointplot() are used to plot bivariate -it creates a multipanel figure that projects the bivariate relationship.
df = sb.load_dataset('iris')
sb.jointplot(x = 'petal_length',y = 'petal_width',data = df,kind ='hex')
plt.show()

#Hexagonal binning is used in bivariate data analysis when the data is sparse in density i.e., when the data is very scattered and difficult to analyze through scatterplots.

#pairwise relationship -the relationship between each and every variable 
sb.pairplot(df) #relationship for (n,2) combination of variable in a DF as a matrix of plots and the diagonal plots are univariate plots
plt.show()

#Plotting categorial data
df = sb.load_dataset('iris')
sb.stripplot(x = "species", y = "petal_length", data = df,jitter = True)#stripplot represents the data in sorted order along any one of the axis
plt.show()

#Jitter adds some random noise to the data. This parameter will adjust the positions along the categorical axis
#instead of jitter we can also use swarmplot
df = sb.load_dataset('iris')
sb.swarmplot(x = "species", y = "petal_length", data = df)
plt.show()

#Distribution of observations ,Violin Plots are a combination of the box plot with the kernel density estimates
df = sb.load_dataset('iris')
sb.boxplot(x = "species", y = "petal_length", data = df)
plt.show()
#The quartile and whisker values from the boxplot are shown inside the violin. As the violin plot uses KDE, the wider portion of violin indicates the higher density and narrow region represents relatively lower density. The Inter-Quartile range in boxplot and higher density portion in kde fall in the same region of each category of violin plot

#Statistical estimation
#The barplot() shows the relation between a categorical variable and a continuous variable. The data is represented in rectangular bars where the length the bar represents the proportion of the data in that category
df = sb.load_dataset('titanic')
sb.barplot(x = "sex", y = "survived", hue = "class", data = df)#estimating the central tendancy which cant be done by estimation ofhte whole data
plt.show()

#A special case in barplot is to show the no of observations in each category rather than computing a statistic for a second variable. For this, we use countplot().
#Point plots serve same as bar plots but in a different style. Rather than the full bar, the value of the estimate is represented by the point at a certain height on the other axis.
df = sb.load_dataset('titanic')
sb.pointplot(x = "sex", y = "survived", hue = "class", data = df)
plt.show()

#plotting wide form data
df = sb.load_dataset('iris')
sb.boxplot(data = df, orient = "h")#These functions accept vectors of Pandas or NumPy objects rather than variables in a DataFrame
plt.show()


#The major advantage of using Seaborn for many developers in Python world is because it can take pandas DataFrame object as parameter


#Multipanel Categorial Plots
#Factorplot draws a categorical plot on a FacetGrid. Using ‘kind’ parameter we can choose the plot like boxplot, violinplot, barplot and stripplot. FacetGrid uses pointplot by default
#Facet grid forms a matrix of panels defined by row and column by dividing the variables. Due of panels, a single plot looks like multiple plots. It is very helpful to analyze all combinations in two discrete variable

#Regression Variables
#non-linear, higher order can be visualized using the lmplot() and regplot().These can fit a polynomial regression model to explore simple kinds of nonlinear trends in the dataset
df = sb.load_dataset('anscombe')
sb.lmplot(x = "x", y = "y", data = df.query("dataset == 'II'"),order = 2)
plt.show()

#By drawing multiple instances of the same plot on different subsets of your dataset is a useful approach to explore multidimensional data
#A FacetGrid can be drawn with up to three dimensions − row, col, and hue. The first two have obvious correspondence with the resulting array of axes; think of the hue variable as a third dimension along a depth axis, where different levels are plotted with different colors
df = sb.load_dataset('tips')
g = sb.FacetGrid(df, col = "time")
g.map(plt.hist, "tip") #visualize the data on the grid
plt.show() 

#PairGrid allows us to draw a grid of subplots using the same plot type to visualize data.

#Unlike FacetGrid, it uses different pair of variable for each subplot. It forms a matrix of sub-plots. It is also sometimes called as “scatterplot matrix”
df = sb.load_dataset('iris')
g = sb.PairGrid(df)
g.map_upper(plt.scatter)
g.map_lower(sb.kdeplot, cmap = "Blues_d")
g.map_diag(sb.kdeplot, lw = 3, legend = False);
plt.show()