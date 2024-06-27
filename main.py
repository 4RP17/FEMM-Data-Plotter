import matplotlib.pyplot as plt
import numpy as np

def plot_data_from_file(filename):
    
    # Load the data from the file, skipping the first two lines
    data = np.loadtxt(filename, skiprows=2)
    
    # Extract columns
    lengths = data[:, 0]
    magnetic_field = data[:, 1]

    # Print key parameters
    print(f"\nNumber of data points: {len(lengths)} \n")
    print(f"Number of skip points: 2 \n")
    print(f"Minimum Length: {np.min(lengths)} mm \n")
    print(f"Maximum Length: {np.max(lengths)} mm \n")
    print(f"Minimum Magnetic Field: {np.min(magnetic_field)} Tesla \n")
    print(f"Maximum Magnetic Field: {np.max(magnetic_field)} Tesla \n")
    print(f"Mean Magnetic Field: {np.mean(magnetic_field)} Tesla \n")
    
    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(lengths, magnetic_field, marker='o', linestyle='-', linewidth=0.4, markersize=1, color='g')
    plt.title('Magnetic Field vs. Length')
    plt.xlabel('Length (mm)')
    plt.ylabel('Magnetic Field (Tesla)')

    # Use the function with a specified tick gap, e.g., 2 mm
    tick_gap = 2

    # Calculate tick positions
    min_length = np.min(lengths)
    max_length = np.max(lengths)
    ticks = np.arange(min_length, max_length + tick_gap, tick_gap)
    
    # Set the ticks on the x-axis
    plt.xticks(ticks)
    
    plt.grid(True)
    plt.show()

# Use the function
plot_data_from_file('data.txt')
