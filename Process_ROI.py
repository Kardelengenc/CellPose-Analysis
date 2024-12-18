import numpy as np
from scipy.ndimage import binary_dilation
from skimage.measure import regionprops

def process_roi(all_mask, num_regions, hexagonality_score):
    """
    Process each ROI and calculate properties.

    Parameters:
        analyze_masks (numpy.ndarray): Mask array with labeled regions.
        num_regions (int): Number of regions to process.
        hexagonality_score (function): A function to calculate hexagonality metrics.

    Returns:
        dict: Data dictionary containing calculated properties for each region.
    """
    # Initialize data dictionary
    data = {
        'centroid': np.zeros((num_regions, 2)),
        'neighbor_counts': np.zeros(num_regions),
        'aspect_ratio': np.zeros(num_regions),
        'circularity': np.zeros(num_regions),
        'area': np.zeros(num_regions),
        'perimeter': np.zeros(num_regions),
        'polyAve': np.zeros(num_regions),
        'hexAve': np.zeros(num_regions),
        'hexSd': np.zeros(num_regions)
    }


    # Iterate through each region
    for i in range(1, num_regions + 1):

        region_mask = (all_mask == i)

        # Dilate the mask to find neighbors
        se = np.ones((3, 3))
        dilated_mask = binary_dilation(region_mask, structure=se)

        # Get neighboring region labels
        neighbors = np.unique(all_mask[dilated_mask & ~region_mask])
        neighbor_counts = len(neighbors[neighbors > 0])

        # Get region properties
        props = regionprops(region_mask.astype(int))

        if len(props) > 0:
            props = props[0]

            # Calculate hexagonality metrics
            dataHex = hexagonality_score(neighbor_counts, props)

            # Save data
            data['centroid'][i - 1, :] = props.centroid
            data['neighbor_counts'][i - 1] = neighbor_counts
            data['aspect_ratio'][i - 1] = dataHex['aspect_ratio']
            data['circularity'][i - 1] = dataHex['circularity_score']
            data['area'][i - 1] = props.area
            data['perimeter'][i - 1] = props.perimeter
            data['polyAve'][i - 1] = dataHex['polyAve']
            data['hexAve'][i - 1] = dataHex['hexAve']
            data['hexSd'][i - 1] = dataHex['hexSd']

    return data
