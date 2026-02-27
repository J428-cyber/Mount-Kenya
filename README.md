# Mount Kenya 3D Terrain Visualization

This project renders a 3D surface of Mount Kenya from CSV terrain data using Python, `pandas`, and `matplotlib`.

![Mount Kenya](Screenshot%20From%202026-02-26%2021-22-52.png)

## Project Goal

Turn raw coordinate data into a visual model of Mount Kenya so elevation patterns can be explored on-screen.

## Files

- `mount kenya.py`: Main script that loads data and draws the 3D terrain.
- `mountain.csv`: Source dataset (must include `X`, `Y`, and `Z` columns).
- `Screenshot From 2026-02-26 21-22-52.png`: Example output.

## Requirements

- Python 3.9+
- pandas
- numpy
- matplotlib

Install dependencies:

```bash
pip install pandas numpy matplotlib
```

## How to Run

From the project folder:

```bash
python "mount kenya.py"
```

The script:

1. Locates `mountain.csv` relative to the script path.
2. Validates that `X`, `Y`, and `Z` exist.
3. Converts `X` to numeric codes if it is categorical text.
4. Builds a 3D triangulated surface (`plot_trisurf`).

## Coordinate Challenges

Working with mountain coordinates is not always straightforward:

- Inconsistent coordinate systems:
  Latitude/longitude (degrees) and projected coordinates (meters) behave differently.
- Missing or noisy points:
  Real terrain datasets often have gaps and outliers that distort surfaces.
- Non-uniform spacing:
  Irregularly sampled points can create stretched triangles and visual artifacts.
- Mixed data types:
  Columns may contain text labels where numbers are expected.
- Scale mismatch:
  Horizontal distance and elevation may be in different units, making the terrain look too flat or too steep.

## Math Behind the Plot

This visualization relies on core math ideas:

- 3D points:
  Each row is a point `(x, y, z)`, where `z` is elevation.
- Triangulation:
  The surface is approximated by connecting nearby points into triangles.
- Interpolation on triangles:
  Heights between measured points are estimated across triangular faces.
- Coordinate mapping:
  Raw input values are transformed into plotting coordinates.
- Basic quality checks:
  Validating ranges and numeric types avoids invalid geometry.

## Common Errors and Fixes

- `FileNotFoundError`: Confirm `mountain.csv` is in the same folder as the script.
- `ValueError` for missing columns: Ensure CSV has `X`, `Y`, `Z`.
- Plot looks distorted: Check units and coordinate system consistency.

## Future Improvements

- Add coordinate system conversion (e.g., lat/lon to UTM).
- Add data cleaning for outlier removal.
- Export interactive 3D output (Plotly or PyVista).
- Add slope/gradient analysis for terrain difficulty mapping.
