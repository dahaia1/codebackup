import numpy as np
import matplotlib.pyplot as plt
import os

def generate_gear_contour(z, m=1):
    """Generate gear profile coordinates"""
    r_pitch = m * z / 2
    ra = r_pitch + m
    rf = max(r_pitch - 1.25*m, 0.1*m)
    
    theta = np.linspace(0, 2*np.pi, 1000)
    radii = np.full_like(theta, rf)
    tooth_angle = 2*np.pi/z
    
    for i, angle in enumerate(theta):
        if (angle % tooth_angle) < np.pi/z:
            radii[i] = ra
            
    return radii * np.cos(theta), radii * np.sin(theta)

def save_gear_svg(z, folder='gears'):
    """Save gear as SVG without any labels"""
    m = 8.0/z  # Auto-scale modulus
    x, y = generate_gear_contour(z, m)
    
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.plot(x, y, 'k', linewidth=0.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    os.makedirs(folder, exist_ok=True)
    plt.savefig(f"{folder}/gear_{z:03d}.svg", 
                bbox_inches='tight', 
                pad_inches=0, 
                transparent=True)
    plt.close()

# Generate gears from 3 to 100 teeth
for z in range(3, 101):
    save_gear_svg(z)

print(f"Generated {98} gear SVGs in 'gears' folder")
