import numpy as np

def interpolate_nan(fl):
    nans, x_ = np.isnan(fl), lambda z: z.nonzero()[0]
    fl[nans] = np.interp(x_(nans), x_(~nans), fl[~nans])
    return fl

def normalize_flux_minmax(fl):
    flux_min = np.min(fl)
    flux_max = np.max(fl)
    flux_norm = (fl - flux_min) / (flux_max - flux_min)
    return flux_norm