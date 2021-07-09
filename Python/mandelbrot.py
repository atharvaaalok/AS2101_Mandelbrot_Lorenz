from matplotlib import pyplot as plt
import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True

# plt.style.use('seaborn')


# creating arrays of numbers
start = -2
stop = 2
count = 10000
xpoints = np.linspace(start, stop, count)
ypoints = np.linspace(start, stop, count)

xx, yy = np.meshgrid(xpoints, ypoints)
# xx_initial = xx
# yy_initial = yy
complex_points_original = xx + yy * 1j
in_set = np.abs(complex_points_original) < 2
# print(in_set)
complex_points_squared = complex_points_original[in_set]
complex_points_original = complex_points_original[in_set]
# print(xx)
# print(yy)
# print(complex_points)



# perform the iteration step of the mandelbrot set
total_iterations = 50
for iter in range(total_iterations):
    print(iter)
    complex_points_squared = np.square(complex_points_squared) + complex_points_original
    in_set = np.abs(complex_points_squared) < 2
    complex_points_squared = complex_points_squared[in_set]
    complex_points_original = complex_points_original[in_set]
    # xx = np.square(xx) - np.square(yy)
    # yy = 2*xx*yy


in_set = np.abs(complex_points_squared) < 2
# print(complex_points[in_set])
# print(complex_points[np.logical_not(in_set)])

xx_inset = complex_points_original[in_set].real
yy_inset = complex_points_original[in_set].imag

# xx_notinset = complex_points_original[np.logical_not(in_set)].real
# yy_notinset = complex_points_original[np.logical_not(in_set)].imag



fig, ax = plt.subplots()


ax.scatter(xx_inset, yy_inset, c = "black", s = .1, marker = ".", linewidths = 0)


# ax.legend()
axis_fontsize = 10
ax.set_title(r"Mandelbrot Set: $z_{n+1} = z_{n}^2 + c$", fontsize = axis_fontsize + 2)
ax.set_xlabel("Real Axis", fontsize = axis_fontsize)
ax.set_ylabel("Imaginary Axis", fontsize = axis_fontsize)



axis_label_size = 10
ax.tick_params(axis='x', labelsize = axis_label_size)
ax.tick_params(axis='y', labelsize = axis_label_size)

# set background color to light blue - using hex color code
ax.set_facecolor('#EBF5FB')
ax.margins(0)

# set ratio of unit on x and y axis to 1
ax.set_aspect(1)

# fig.set_dpi(1200)

# ax.grid(True)

plt.tight_layout()

# uncomment the next line to save the figure in high resolution
# plt.savefig("Mandelbrot.png", dpi = 1200)

plt.show()