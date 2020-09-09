# Generate a 2-D histogram
plt.hist2d(hp, mpg, range=((40,235),(8,48)), bins=(20,20))

# Add a color bar to the histogram
plt.colorbar()

# Add labels, title, and display the plot
plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hist2d() plot')
plt.show()
