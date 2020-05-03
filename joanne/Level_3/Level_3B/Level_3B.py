# %%
import glob
import time
from datetime import date
from importlib import reload

import numpy as np
import xarray as xr
import yaml

import rgr_fn as rf
import ready_ds_for_regression as prep
import dicts

reload(prep)
reload(rf)
reload(dicts)

import joanne

# %%
circles = prep.get_circles()
prep.get_xy_coords_for_circles(circles)

# %%
start = time.perf_counter()

list_of_parameters = [
    "u_wind",
    "v_wind",
    "specific_humidity",
    "temperature",
    "pressure",
]

rf.get_circle_products(circles, list_of_parameters)

circles = prep.reswap_launchtime_sounding(circles)

finish = time.perf_counter()

print(f"Finished in {round(finish - start,2)} seconds ...")

# %%

lv3b_dataset = xr.concat(circles, dim="circle")

# %%

nc_data = {}

for var in dicts.list_of_vars:
    nc_data[var] = lv3b_dataset[var].values

    if var == 'launch_time' :
        nc_data[var] = lv3b_dataset[var].astype("float").values / 1e9

# %%

height = lv3b_dataset.height.values
sounding = lv3b_dataset.sounding.values
circle = lv3b_dataset.circle.values

to_save_ds = xr.Dataset(
    coords={"height": height, "sounding": sounding, "circle": circle}
)

for var in dicts.list_of_vars:
    prep.create_variable(
        to_save_ds, var, data=nc_data, dims=dicts.nc_dims, attrs=dicts.nc_attrs
    )

file_name = (
    "EUREC4A_JOANNE_Dropsonde-RD41_" + "Level_3B_v" + str(joanne.__version__) + ".nc"
)

save_directory = (
    "/Users/geet/Documents/JOANNE/Data/Level_3/Test_data/"  # Test_data/" #Level_3/"
)

comp = dict(zlib=True, complevel=4, fletcher32=True, _FillValue=np.finfo("float32").max)

encoding = {}

encoding = {
    var: comp for var in to_save_ds.data_vars if var not in ["Platform"]
}

for key in dicts.nc_global_attrs.keys():
    to_save_ds.attrs[key] = dicts.nc_global_attrs[key]

to_save_ds.to_netcdf(
    save_directory + file_name, mode="w", format="NETCDF4", encoding=encoding
)