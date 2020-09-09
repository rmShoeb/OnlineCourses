# Generate a default contour map of the array Z
plt.subplot(2,2,1)
# u = np.linspace(-2, 2, 60)
# v = np.linspace(-5, 5, 80)
# X, Y = np.meshgrid(u, v)
# Z = X**2/25 + Y**2/4
plt.contour(X, Y, Z)

# Generate a contour map with 20 contours
plt.subplot(2,2,2)
plt.contour(X, Y, Z, 20)

# # Generate a default filled contour map of the array Z
plt.subplot(2,2,3)
plt.contourf(X, Y, Z)
plt.colorbar()

# # Generate a default filled contour map with 20 contours
plt.subplot(2,2,4)
plt.contourf(X, Y, Z, 20)
plt.colorbar()
# # Improve the spacing between subplots
plt.tight_layout()

# Display the figure
plt.show()

