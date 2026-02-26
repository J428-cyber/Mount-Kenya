import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Resolve the CSV file path relative to this script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'mountain.csv')

# Check if file exists before proceeding
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"CSV file not found at: {csv_path}\n"
                            f"Current working directory: {os.getcwd()}\n"
                            f"Script directory: {script_dir}")

# Load the data
df = pd.read_csv(csv_path)
print("CSV loaded successfully.")
print("Columns:", df.columns.tolist())
print("Shape:", df.shape)
print(df.head())

# Ensure required columns exist
required_columns = ['X', 'Y', 'Z']
if not all(col in df.columns for col in required_columns):
    raise ValueError(f"CSV must contain columns: {required_columns}")

# Convert categorical X if needed
if df['X'].dtype == 'object':
    df['X'] = pd.Categorical(df['X']).codes

# Create 3D plot using modern syntax
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')  # Updated from deprecated gca(projection='3d')

ax.plot_trisurf(df['X'], df['Y'], df['Z'], cmap=plt.cm.jet, linewidth=0.2, antialiased=True)

ax.set_title("Mount Kenya 3D Plot")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("Z axis (Elevation)")

plt.tight_layout()
plt.show()
