import numpy as np

def hexagonality_score(neighbor_counts, props):
    # Fetch necessary values
    neighbors = neighbor_counts
    area = props.area
    perimeter = props.perimeter
    area_hull = props.convex_area
    perim_hull = 6 * np.sqrt(props.convex_area / (1.5 * np.sqrt(3)))
    min_feret_diam = props.minor_axis_length  # Approximation of MinFeretDiameter
    max_feret_diam = props.major_axis_length  # Approximation of MaxFeretDiameter
    perimeter_neighbors = np.nan

    # If neighbors are 0, set perimeter_neighbors to NaN
    if neighbors == 0:
        perimeter_neighbors = np.nan
    else:
        perimeter_neighbors = perimeter / neighbors

    # Initialize return data
    data = {'polyAve': np.nan, 'hexAve': np.nan, 'hexSd': np.nan, 'aspect_ratio': np.nan, 'circularity_score': np.nan}

    # Calculate polygonality and hexagonality metrics if neighbors > 2
    if neighbors > 2:
        # Polygonality metrics
        poly_size_ratio = 1.0 - abs(1.0 - perimeter_neighbors / np.sqrt((4 * area) / (neighbors / np.tan(np.pi / neighbors))))
        poly_area_ratio = 1.0 - abs(1.0 - area / (0.25 * neighbors * perimeter_neighbors ** 2 / np.tan(np.pi / neighbors)))
        poly_ave = 10 * (poly_size_ratio + poly_area_ratio) / 2

        # Hexagonality metrics
        apoth1 = np.sqrt(3) * perimeter / 12
        apoth2 = np.sqrt(3) * max_feret_diam / 4
        apoth3 = min_feret_diam / 2
        side1 = perimeter / 6
        side2 = max_feret_diam / 2
        side3 = min_feret_diam / np.sqrt(3)
        side4 = perim_hull / 6

        # Unique area calculations
        area1 = 0.5 * (3 * np.sqrt(3)) * side1 ** 2
        area2 = 0.5 * (3 * np.sqrt(3)) * side2 ** 2
        area3 = 0.5 * (3 * np.sqrt(3)) * side3 ** 2
        area4 = 3 * side1 * apoth2
        area5 = 3 * side1 * apoth3
        area6 = 3 * side2 * apoth3
        area7 = 3 * side4 * apoth1
        area8 = 3 * side4 * apoth2
        area9 = 3 * side4 * apoth3
        area10 = area_hull
        area11 = area

        # Create a list of all unique areas
        list_area = [area1, area2, area3, area4, area5, area6, area7, area8, area9, area10, area11]
        area_array = []

        # Calculate area ratio statistics
        sum_area = 0
        for ib in range(len(list_area)):
            for ic in range(ib + 1, len(list_area)):
                area_ratio = 1.0 - abs(1.0 - list_area[ib] / list_area[ic])
                if not np.isfinite(area_ratio):
                    continue
                area_array.append(area_ratio)
                sum_area += area_ratio

        area_ratio_ave = sum_area / len(area_array)

        # Standard deviation for area ratios
        sqrdTmp = np.sum((np.array(area_array) - area_ratio_ave) ** 2)
        area_ratio_sd = np.sqrt(sqrdTmp / len(area_array))

        # Hexagon area ratio
        hex_area_ratio = area_ratio_ave

        # Perimeter ratio calculations
        apoth4 = np.sqrt(3) * perim_hull / 12
        apoth5 = np.sqrt(4 * area_hull / (4.5 * np.sqrt(3)))
        perim1 = np.sqrt(24 * area / np.sqrt(3))
        perim2 = np.sqrt(24 * area_hull / np.sqrt(3))
        perim3 = perimeter
        perim4 = perim_hull
        perim5 = 3 * max_feret_diam
        perim6 = 6 * min_feret_diam / np.sqrt(3)
        perim7 = 2 * area / apoth1
        perim8 = 2 * area / apoth2
        perim9 = 2 * area / apoth3
        perim10 = 2 * area / apoth4
        perim11 = 2 * area / apoth5
        perim12 = 2 * area_hull / apoth1
        perim13 = 2 * area_hull / apoth2
        perim14 = 2 * area_hull / apoth3

        # Create a list of all unique perimeters
        list_perim = [perim1, perim2, perim3, perim4, perim5, perim6, perim7, perim8, perim9, perim10, perim11, perim12, perim13, perim14]
        perim_array = []

        # Perimeter ratio statistics
        sum_perim = 0
        for ib in range(len(list_perim)):
            for ic in range(ib + 1, len(list_perim)):
                perim_ratio = 1.0 - abs(1.0 - list_perim[ib] / list_perim[ic])
                perim_array.append(perim_ratio)
                sum_perim += perim_ratio

        perim_ratio_ave = sum_perim / len(perim_array)

        # Standard deviation for perimeter ratios
        sqrdTmp2 = np.sum((np.array(perim_array) - perim_ratio_ave) ** 2)
        perim_ratio_sd = np.sqrt(sqrdTmp2 / len(perim_array))

        # Hexagonality Score Calculation
        hex_size_ratio = perim_ratio_ave
        hex_sd = np.sqrt((area_ratio_sd ** 2 + perim_ratio_sd ** 2) / 2)
        hex_ave = 10 * (hex_area_ratio + hex_size_ratio) / 2

        #Circularity Score Calculation
        circularity = np.nan if perimeter == 0 else 4 * np.pi * area / (perimeter ** 2)

        #Aspect Ratio Calculation
        aspect_ratio = max_feret_diam / min_feret_diam if min_feret_diam != 0 else np.nan

        # Final results
        data['polyAve'] = poly_ave
        data['hexAve'] = hex_ave
        data['hexSd'] = hex_sd
        data['aspect_ratio'] = aspect_ratio
        data['circularity_score'] = circularity
    else:
        if neighbors < 3:
            data['polyAve'] = np.nan
            data['hexAve'] = np.nan
            data['hexSd'] = np.nan

    return data
