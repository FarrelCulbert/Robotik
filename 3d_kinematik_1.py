import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider

# Panjang segmen lengan
L_base = 0.5  # Panjang dasar tetap (segmen keempat)
L1 = 1.0  # Panjang segmen pertama
L2 = 1.0  # Panjang segmen kedua

# Fungsi kinematika maju untuk menghitung posisi segmen lengan
def forward_kinematics(theta1, theta2, theta3):
    # Konversi ke radian
    theta1 = np.radians(theta1)
    theta2 = np.radians(theta2)
    theta3 = np.radians(theta3)

    # Koordinat dasar segmen keempat (dasar tetap)
    x = [0, 0]  # Menghubungkan ke titik dasar
    y = [0, 0]
    z = [0, L_base]  # Garis vertikal dari 0 ke L_base

    # Pertama segmen
    x.append(x[-1] + L1 * np.cos(theta1) * np.cos(theta2))
    y.append(y[-1] + L1 * np.sin(theta1) * np.cos(theta2))
    z.append(z[-1] + L1 * np.sin(theta2))

    # Kedua segmen
    x.append(x[-1] + L2 * np.cos(theta1) * np.cos(theta2 + theta3))
    y.append(y[-1] + L2 * np.sin(theta1) * np.cos(theta2 + theta3))
    z.append(z[-1] + L2 * np.sin(theta2 + theta3))

    # Ketiga segmen


    return x, y, z

# Membuat plot 3D dan slider untuk interaksi
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Inisialisasi sudut sendi
theta1 = 0
theta2 = 0
theta3 = 0

# Plot lengan awal
x, y, z = forward_kinematics(theta1, theta2, theta3)
line, = ax.plot(x, y, z, marker='o', label='Lengan Kinematik 3D')

# Plot garis base
base_line, = ax.plot([0, 0], [0, 0], [0, L_base], 'k-', label='Base Line')  # Garis dasar dengan garis putus-putus

# Set batas plot
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([0, 3])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Menambahkan slider untuk mengubah sudut sendi
axcolor = 'lightgoldenrodyellow'
ax_theta1 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
ax_theta2 = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_theta3 = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor=axcolor)

slider_theta1 = Slider(ax_theta1, 'Theta1', -180, 180, valinit=theta1)
slider_theta2 = Slider(ax_theta2, 'Theta2', -90, 90, valinit=theta2)
slider_theta3 = Slider(ax_theta3, 'Theta3', -90, 90, valinit=theta3)

# Fungsi update ketika slider diubah
def update(val):
    theta1 = slider_theta1.val
    theta2 = slider_theta2.val
    theta3 = slider_theta3.val
    x, y, z = forward_kinematics(theta1, theta2, theta3)
    line.set_xdata(x)
    line.set_ydata(y)
    line.set_3d_properties(z)

    # Pastikan garis base tetap ada
    base_line.set_xdata([0, 0])
    base_line.set_ydata([0, 0])
    base_line.set_3d_properties([0, L_base])

    fig.canvas.draw_idle()

# Menyambungkan fungsi update ke slider
slider_theta1.on_changed(update)
slider_theta2.on_changed(update)
slider_theta3.on_changed(update)

plt.show()
