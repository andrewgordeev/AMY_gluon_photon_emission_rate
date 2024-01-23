import numpy as np
import matplotlib.pyplot as plt

# Load calculated rates - adjust directories as needed (particularly for photonEmission_hydroInterface)
lin_rate = np.loadtxt('output_lin_modified.txt')
quad_rate = np.loadtxt('output_quad_modified.txt')
old_rate = np.loadtxt('../../photonEmission_hydroInterface/ph_rates/rate_QGP_2to2_total_eqrate.dat')

# Creating coordinate grids using meshgrid based on array dimensions
x_coords, y_coords = np.meshgrid(np.arange(80), np.arange(351))

# Flatten the coordinates and corresponding data for scatter plot
x_flat = x_coords.flatten()
x_flat = 0.05 + x_flat*0.05
y_flat = y_coords.flatten()
y_flat = 0.1 + y_flat*0.002
data_flat = (lin_rate+quad_rate-old_rate).flatten()/(old_rate).flatten()

# Scatter plot with color mapped by data - adjust vmin, vmax if needed
plt.scatter(x_flat, y_flat, c=data_flat, cmap=plt.cm.jet, marker='o', vmin = -1, vmax = 1)
plt.colorbar()
plt.xlabel(r'$k$ (GeV)')
plt.ylabel(r'$T$ (GeV)')
plt.title(r'$(\nu_{lin}+\nu_{quad} - \nu_{old})/\nu_{old}$')