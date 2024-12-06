import numpy as np

def interpolate_nan(fl):
    nans, x_ = np.isnan(fl), lambda z: z.nonzero()[0]
    fl[nans] = np.interp(x_(nans), x_(~nans), fl[~nans])
    return fl

def normalize_flux_median(fl,wavelength):
    #flux_min = np.min(fl)
    #flux_max = np.max(fl)
    #flux_norm = (fl - flux_min) / (flux_max - flux_min)
    red_chip = []
    green_chip = []
    blue_chip = []
    for i in range(len(fl)):
        if wavelength[i] < 15811:
            blue_chip.append(fl[i])
        elif wavelength[i] < 16441:
            green_chip.append(fl[i])
        else:
            red_chip.append(fl[i])
    
    blue_chip = np.array(blue_chip)
    green_chip = np.array(green_chip)
    red_chip = np.array(red_chip)
    
    median_blue = np.median(blue_chip)
    median_green = np.median(green_chip)
    median_red = np.median(red_chip)
    
    norm_blue = blue_chip / median_blue
    norm_green = green_chip / median_green
    norm_red = red_chip / median_red
    
    flux_norm = np.concatenate((norm_blue,norm_green,norm_red))

    return flux_norm

def standarize_output(y):
    y = np.array(y)
    mean_y = np.mean(y,axis=0)
    std_y = np.std(y,axis=0)
    y = (y - mean_y) / std_y
    return y
    