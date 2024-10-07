import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    #Use Pandas to import the data from epa-sea-level.csv.
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    #Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
    fig, ax = plt.subplots()
    ax = plt.scatter(x="Year", y="CSIRO Adjusted Sea Level", data=df)

    # Create first line of best fit
    # Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. 
    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']
    fit1 = linregress(x, y)

    # Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
    years_extended =np.arange(df['Year'].max()+1,2050+1)
    per_data = pd.Series(years_extended )
    df_future=pd.DataFrame(per_data, columns=['Year'])

    df_ext=pd.concat([df, df_future], ignore_index=True)
    x=df_ext['Year']

    # Use the slope and intercept to construct the best fit line
    y_pred = fit1.intercept + fit1.slope * x
    ax=plt.plot(x, y_pred, color='red', label=f'Best fit line: y={fit1.slope:.2f}x+{fit1.intercept:.2f}')

    # Create second line of best fit
    #Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. 
    df_rec=df[df['Year'] >= 2000 ]
    x2=df_rec['Year']
    y2=df_rec['CSIRO Adjusted Sea Level']
    fit2 = linregress(x2, y2)

    # Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
    df_ext2=pd.concat([df_rec, df_future], ignore_index=True)
    x_ext2=df_ext2['Year']
    y_rec = fit2.intercept + fit2.slope * x_ext2
    ax=plt.plot(x_ext2, y_rec, color='green', label=f'Best fit line: y={fit2.slope:.2f}x+{fit2.intercept:.2f}')


    # Add labels and title
    #The x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level.
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()