import datetime
import joanne

list_of_vars = [
    "launch_time",
    "height",
    # "latitude",
    # "longitude",
    # "pressure",
    # "temperature",
    # "relative_humidity",
    # "wind_speed",
    # "wind_direction",
    # "u_wind",
    # "v_wind",
    # "potential_temperature",
    # "specific_humidity",
    # "precipitable_water",
    # "static_stability",
    # "low_height_flag",
    # "cloud_flag",
    # "Platform",
    # "flight_height",
    # "flight_lat",
    # "flight_lon",
    "xc",
    "yc",
    # "dx",
    # "dy",
    "mean_u",
    "dudx",
    "dudy",
    "sondes_regressed",
    "mean_v",
    "dvdx",
    "dvdy",
    "mean_q",
    "dqdx",
    "dqdy",
    "mean_T",
    "dTdx",
    "dTdy",
    "mean_p",
    "dpdx",
    "dpdy",
    "divergence",
    "vorticity",
    # "density",
    # "mean_density",
    "vertical_velocity",
    "pressure_velocity",
    "h_adv_q",
    "h_adv_T",
    "h_adv_p",
]

nc_attrs = {
    "launch_time": {
        "standard_name": "time",
        "long_name": "Time of dropsonde launch",
        "units": "seconds since 1970-01-01 00:00:00 UTC",
        "calendar": "gregorian",
        "axis": "T",
    },
    "height": {
        "standard_name": "geopotential_height",
        "long_name": "Geopotential Height",
        "description": "Height obtained by integrating upwards the atmospheric thickness estimated from the hypsometric equation",
        "units": "gpm",
        "axis": "Z",
        "positive": "up",
    },
    "latitude": {
        "standard_name": "latitude",
        "long_name": "North Latitude",
        "units": "degree_north",
        "axis": "X",
    },
    "longitude": {
        "standard_name": "longitude",
        "long_name": "East Longitude",
        "units": "degree_east",
        "axis": "Y",
    },
    "pressure": {
        "standard_name": "air_pressure",
        "long_name": "Atmospheric Pressure",
        "units": "hPa",
        "coordinates": "launch_time longitude latitude height",
    },
    "temperature": {
        "standard_name": "air_temperature",
        "long_name": "Dry Bulb Temperature",
        "units": "degree_Celsius",
        "coordinates": "launch_time longitude latitude height",
    },
    "potential_temperature": {
        "standard_name": "potential_temperature",
        "long_name": "potential temperature",
        "units": "K",
        "coordinates": "launch_time longitude latitude height",
    },
    "relative_humidity": {
        "standard_name": "relative_humidity",
        "long_name": "Relative Humidity",
        "units": "%",
        "coordinates": "launch_time longitude latitude height",
    },
    "specific_humidity": {
        "standard_name": "specific_humidity",
        "long_name": "Specific humidity",
        "units": "kg kg-1",
        "coordinates": "launch_time longitude latitude height",
    },
    "wind_speed": {
        "standard_name": "wind_speed",
        "long_name": "Wind Speed",
        "units": "m s-1",
        "coordinates": "launch_time longitude latitude height",
    },
    "u_wind": {
        "standard_name": "eastward_wind",
        "long_name": "u-component of the wind",
        "units": "m s-1",
        "coordinates": "launch_time longitude latitude height",
    },
    "v_wind": {
        "standard_name": "northward_wind",
        "long_name": "v-component of the wind",
        "units": "m s-1",
        "coordinates": "launch_time longitude latitude height",
    },
    "wind_direction": {
        "standard_name": "wind_from_direction",
        "long_name": "Wind Direction",
        "units": "degree",
        "coordinates": "launch_time longitude latitude height",
    },
    "precipitable_water": {
        "standard_name": "precipitable_water",
        "long_name": "integrated water vapour in the measured column",
        "units": "kg m-2",
        "coordinates": "launch_time",
    },
    "static_stability": {
        "standard_name": "static_stability",
        "long_name": "static stability",
        "description": "gradient of potential temperature along the pressure grid",
        "units": " K hPa-1",
        "coordinates": "launch_time longitude latitude height",
    },
    "low_height_flag": {
        "long_name": "flag to indicate if flight height at launch was low",
        "flag_values": "1, 0",
        "flag_meanings": "flight height below 4 km flight height at or above 4 km",
        "valid_range": "0, 1",
    },
    "cloud_flag": {
        "long_name": "flag to indicate presence of cloud",
        "flag_values": "1, 0",
        "flag_meanings": "cloud no_cloud",
        "valid_range": "0, 1",
    },
    "Platform": {
        "standard_name": "platform",
        "long_name": "platform from which the sounding was made",
        "coordinates": "launch_time",
    },
    "flight_height": {
        "standard_name": "height",
        "long_name": "height of the aircraft when the dropsonde was launched",
        "units": "m",
        "coordinates": "launch_time",
    },
    "flight_lat": {
        "standard_name": "latitude",
        "long_name": "north latitude of the aircraft when the dropsonde was launched",
        "units": "degree_north",
        "coordinates": "launch_time",
    },
    "flight_lon": {
        "standard_name": "longitude",
        "long_name": "east longitude of the aircraft when the dropsonde was launched",
        "units": "degree_east",
        "coordinates": "launch_time",
    },
    "xc": {
        "standard_name": "circle_center_x",
        "long_name": "mean zonal distance from zero longitude of all regressed sondes in circle",
        "units": "m",
        "coordinates": "circle height",
    },
    "yc": {
        "standard_name": "circle_center_y",
        "long_name": "mean meridional distance from zero latitude of all regressed sondes in circle",
        "units": "m",
        "coordinates": "circle height",
    },
    "dx": {
        "standard_name": "delta_x",
        "long_name": "zonal distance of sonde from xc of circle",
        "units": "m",
        "coordinates": "launch_time height",
    },
    "dy": {
        "standard_name": "delta_y",
        "long_name": "meridional distance of sonde from yc of circle",
        "units": "m",
        "coordinates": "launch_time height",
    },
    "mean_u": {
        "standard_name": "eastward_wind",
        "long_name": "intercept value from regressed eastward wind in circle",
        "units": "m s-1",
        "coordinates": "circle height",
    },
    "dudx": {
        "long_name": "zonal gradient of eastward wind",
        "units": "s-1",
        "coordinates": "circle height",
    },
    "dudy": {
        "long_name": "meridional gradient of eastward wind",
        "units": "s-1",
        "coordinates": "circle height",
    },
    "sondes_regressed": {
        # "standard_name": "longitudinal gradient of eastward wind",
        "long_name": "number of sondes regressed",
        # "units": "s-1",
        "coordinates": "circle height",
    },
    "mean_v": {
        "standard_name": "northward_wind",
        "long_name": "intercept value from regressed northward wind in circle",
        "units": "m s-1",
        "coordinates": "circle height",
    },
    "dvdx": {
        "long_name": "zonal gradient of northward wind",
        "units": "s-1",
        "coordinates": "circle height",
    },
    "dvdy": {
        "long_name": "meridional gradient of northward wind",
        "units": "s-1",
        "coordinates": "circle height",
    },
    "mean_q": {
        "standard_name": "specific_humidity",
        "long_name": "intercept value from regressed specific humidity in circle",
        "units": "kg kg-1",
        "coordinates": "circle height",
    },
    "dqdx": {
        "long_name": "zonal gradient of specific humidity",
        "units": "m-1",
        "coordinates": "circle height",
    },
    "dqdy": {
        "long_name": "meridional gradient of specific humidity",
        "units": "m-1",
        "coordinates": "circle height",
    },
    "mean_T": {
        "standard_name": "temperature",
        "long_name": "intercept value from regressed temperature in circle",
        "units": "degree_Celsius",
        "coordinates": "circle height",
    },
    "dTdx": {
        "long_name": "zonal gradient of temperature",
        "units": "degree_Celsius m-1",
        "coordinates": "circle height",
    },
    "dTdy": {
        "long_name": "meridional gradient of temperature",
        "units": "degree_Celsius m-1",
        "coordinates": "circle height",
    },
    "mean_p": {
        "standard_name": "pressure",
        "long_name": "intercept value from regressed pressure in circle",
        "units": "hPa",
        "coordinates": "circle height",
    },
    "dpdx": {
        "long_name": "zonal gradient of pressure",
        "units": "hPa m-1",
        "coordinates": "circle height",
    },
    "dpdy": {
        "long_name": "meridional gradient of pressure",
        "units": "hPa m-1",
        "coordinates": "circle height",
    },
    "divergence": {
        "standard_name": "divergence",
        "long_name": "horizontal mass divergence",
        "units": "s-1",
        "coordinates": "circle height",
    },
    "vorticity": {
        "standard_name": "vorticity",
        "long_name": "horizontal mass divergence",
        "units": "s-1",
        "coordinates": "circle height",
    },
    "density": {
        "standard_name": "air_density",
        "long_name": "air density",
        "units": "kg m-3",
        "coordinates": "launch_time height",
    },
    "mean_density": {
        "standard_name": "air_density",
        "long_name": "mean air density across all sondes in circle",
        "units": "kg m-3",
        "coordinates": "circle height",
    },
    "vertical_velocity": {
        "standard_name": "vertical_velocity",
        "long_name": "large-scale atmospheric vertical velocity",
        "units": "m s-1",
        "coordinates": "circle height",
    },
    "pressure_velocity": {
        "standard_name": "pressure_velocity",
        "long_name": "large-scale atmospheric pressure velocity",
        "units": "hPa h-1",
        "coordinates": "circle height",
    },
    "h_adv_q": {
        "standard_name": "q_advection",
        "long_name": "horizontal advection of specific humidity",
        "units": "s-1",
        "coordinates": "circle height",
    },
    "h_adv_T": {
        "standard_name": "T_advection",
        "long_name": "horizontal advection of temperature",
        "units": "degree_Celsius s-1",
        "coordinates": "circle height",
    },
    "h_adv_p": {
        "standard_name": "p_advection",
        "long_name": "horizontal advection of pressure",
        "units": "hPa s-1",
        "coordinates": "circle height",
    },
}

nc_dims = {
    "launch_time": ["circle", "sounding"],
    "height": ["height"],
    "latitude": ["circle", "sounding", "height"],
    "longitude": ["circle", "sounding", "height"],
    "pressure": ["circle", "sounding", "height"],
    "temperature": ["circle", "sounding", "height"],
    "relative_humidity": ["circle", "sounding", "height"],
    "wind_speed": ["circle", "sounding", "height"],
    "wind_direction": ["circle", "sounding", "height"],
    "u_wind": ["circle", "sounding", "height"],
    "v_wind": ["circle", "sounding", "height"],
    "potential_temperature": ["circle", "sounding", "height"],
    "specific_humidity": ["circle", "sounding", "height"],
    "precipitable_water": ["circle", "sounding"],
    "static_stability": ["circle", "sounding", "height"],
    "low_height_flag": ["circle", "sounding"],
    "cloud_flag": ["circle", "sounding", "height"],
    "Platform": ["circle", "sounding"],
    "flight_height": ["circle", "sounding"],
    "flight_lat": ["circle", "sounding"],
    "flight_lon": ["circle", "sounding"],
    "xc": ["circle", "height"],
    "yc": ["circle", "height"],
    "dx": ["circle", "sounding", "height"],
    "dy": ["circle", "sounding", "height"],
    "mean_u": ["circle", "height"],
    "dudx": ["circle", "height"],
    "dudy": ["circle", "height"],
    "sondes_regressed": ["circle", "height"],
    "mean_v": ["circle", "height"],
    "dvdx": ["circle", "height"],
    "dvdy": ["circle", "height"],
    "mean_q": ["circle", "height"],
    "dqdx": ["circle", "height"],
    "dqdy": ["circle", "height"],
    "mean_T": ["circle", "height"],
    "dTdx": ["circle", "height"],
    "dTdy": ["circle", "height"],
    "mean_p": ["circle", "height"],
    "dpdx": ["circle", "height"],
    "dpdy": ["circle", "height"],
    "divergence": ["circle", "height"],
    "vorticity": ["circle", "height"],
    "density": ["circle", "sounding", "height"],
    "mean_density": ["circle", "height"],
    "vertical_velocity": ["circle", "height"],
    "pressure_velocity": ["circle", "height"],
    "h_adv_q": ["circle", "height"],
    "h_adv_T": ["circle", "height"],
    "h_adv_p": ["circle", "height"],
}

nc_global_attrs = {
    "Title": "Level-3B : Circle Products",
    "Campaign_ID": "EUREC4A",
    "Project_ID": "JOANNE",
    "Instrument": "Vaisala RD-41",
    "Data Processing for Level-2": "BatchAspen v3.4.3",
    "Author": "Geet George",
    "Author Email": "geet.george@mpimet.mpg.de",
    "version": joanne.__version__,
    "Reference Study": "https://doi.org/10.1175/JAS-D-18-0141.1",
    "Conventions": "CF-1.7",
    "featureType": "trajectory",
    "Creation Time": str(datetime.datetime.utcnow()) + " UTC",
}
