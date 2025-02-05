# README for Cell Segmentation and Morphological Analysis Script

## Description

This Python script is designed to analyze segmented cellular regions obtained from **Cellpose**. The script processes the `seq.npy` file output by Cellpose to compute various morphological and organizational parameters, including:

- **Hexagonality Score**: Quantifies the hexagonal packing of cells.
- **Aspect Ratio**: Ratio of cell dimensions.
- **Circularity**: Measure of how circular each cell is.
- **Area and Perimeter**: Morphometric details of each cell.
- **Neighbor Counts**: Number of neighboring cells for each segmented region.
- **Polygonality Score**: Measurement of polygonal features.

The script also visualizes these properties and exports the results as a `.xlsx` file for further analysis.

---

## Features

- **Removes Edge Masks**: Eliminates segmented regions on the image edges.
- **Neighbor Analysis**: Detects and counts neighboring cells for each region.
- **Hexagonality and Polygonality Scores**: Calculates structural properties for cell organization.
- **Visualization**: Generates and saves comprehensive visualizations of all computed metrics.
- **Data Export**: Outputs a clean Excel file with all computed parameters.

---

## Requirements

### Dependencies
Ensure the following Python libraries are installed:

- `numpy`
- `pandas`
- `matplotlib`
- `scipy`
- `skimage`
- `cellpose`
- `openpyxl`

### Software
- **Cellpose**: Used for initial segmentation.

---

## Usage

### Input
The script requires:
1. A Cellpose segmentation file saved as `seq.npy`.
2. A proper setup with the required Python environment.

### Running the Script
1. Update the `FILEPATH` and `DATANAME` variables in the script to point to your data file location.
2. Run the script:
   ```bash
   python your_script_name.py
   ```
3. The script will process the segmentation file, generate visualizations, and save the computed parameters in an Excel file at the specified location.

---

## Output

1. **Visualizations**:
   - The script generates visual representations of properties like area, perimeter, neighbor counts, aspect ratio, hexagonality, polygonality, and circularity.
   - Images are displayed and saved in the working directory.
2. **Excel File**:
   - Saved as `Result.xlsx` in the specified directory.
   - Includes columns for neighbor counts, area, perimeter, aspect ratio, hexagonality, hexagonality standard deviation, and polygonality.

---

## Examples

### Example Command
```bash
# Example: Update FILEPATH and DATANAME in the script
FILEPATH = r"C:\path\to\segmentation\data"
DATANAME = "segmented_cells"

python analyze_cells.py
```

Expected output:
- Images of metrics saved as `.png` files.
- Results in `Result.xlsx`.

---

## Contributing

To contribute:
1. Fork this repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature"
   ```
4. Push your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## References

This project makes use of the following tools and resources:

1. **Cellpose: A Generalist Algorithm for Cell Segmentation**  
   - Website: [https://www.cellpose.org/](https://www.cellpose.org/)  
   - Paper: Stringer, C., Wang, T., Michaelos, M., & Pachitariu, M. (2021). "Cellpose: a generalist algorithm for cellular segmentation." *Nature Methods*, 18(1), 100-106.  
     - [DOI: 10.1038/s41592-020-01018-x](https://doi.org/10.1038/s41592-020-01018-x)

2. **Nyxus: Feature Extraction for Microscopy and Medical Imaging**  
   - Website: [https://nyxus.readthedocs.io/](https://nyxus.readthedocs.io/)  
   - Paper: Pylvänäinen, J., et al. (2022). "Nyxus: A comprehensive image feature extraction tool for microscopy and biomedical imaging." *Bioinformatics*, 38(3), 855-862.  

If you use this script in your research, please consider citing these tools accordingly.

---

## License

No License

---

## Contact

For questions or issues, please contact:
- **Kardelen Genc**: kardelengenc0@gmail.com
