import datetime
import joanne

list_of_vars = [
    "sounding",
    "circle",
    # "launch_time",
    "alt",
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
    "platform_id",
    "flight_altitude",
    # "flight_lat",
    # "flight_lon",
    "circle_lon",
    "circle_lat",
    "circle_diameter",
    "circle_time",
    # "dx",
    # "dy",
    "u",
    "dudx",
    "dudy",
    # "sondes_regressed",
    "segment_id",
    "sonde_id",
    "v",
    "dvdx",
    "dvdy",
    "q",
    "dqdx",
    "dqdy",
    "ta",
    "dtadx",
    "dtady",
    "p",
    "dpdx",
    "dpdy",
    "D",
    "vor",
    # "density",
    # "mean_density",
    "W",
    "se_dudx",
    "se_dudy",
    "se_dvdx",
    "se_dvdy",
    "se_dqdx",
    "se_dqdy",
    "se_dpdx",
    "se_dpdy",
    "se_dtadx",
    "se_dtady",
    "se_D",
    "se_vor",
    "se_W",
    "omega",
    # "h_adv_q",
    # "h_adv_ta",
    # "h_adv_p",
    # "h_adv_u",
    # "h_adv_v",
]

nc_attrs = {
    "sounding": {
        "standard_name": "sounding",
        "long_name": "sonde number",
        "units": "",
        # "axis": "T",
    },
    "circle": {
        "standard_name": "time",
        "long_name": "circle number",
        "units": "",
        # "axis": "T",
    },
    "launch_time": {
        "standard_name": "time",
        "long_name": "time of dropsonde launch",
        "units": "seconds since 2020-01-01",
        "calendar": "gregorian",
        # "axis": "T",
    },
    "sonde_id": {
        "description": "unique sonde ID",
        "long_name": "sonde identifier",
        "units": "",
        "coordinates": "circle segment_id sounding",
    },
    "alt": {
        "standard_name": "geopotential_height",
        "long_name": "geopotential height",
        "description": "height obtained by integrating upwards the atmospheric thickness estimated from the hypsometric equation",
        "units": "m",
        "axis": "Z",
        "positive": "up",
    },
    "latitude": {
        "standard_name": "latitude",
        "long_name": "latitude",
        "units": "degree_north",
        "axis": "Y",
    },
    "longitude": {
        "standard_name": "longitude",
        "long_name": "longitude",
        "units": "degree_east",
        "axis": "X",
    },
    # "p": {
    #     "standard_name": "air_pressure",
    #     "long_name": "atmospheric pressure",
    #     "units": "Pa",
    #     "coordinates": "launch_time longitude latitude alt",
    # },
    # "ta": {
    #     "standard_name": "air_temperature",
    #     "long_name": "dry bulb temperature",
    #     "units": "K",
    #     "coordinates": "launch_time longitude latitude alt",
    # },
    # "potential_temperature": {
    #     "standard_name": "air_potential_temperature",
    #     "long_name": "air potential temperature",
    #     "units": "K",
    #     "coordinates": "launch_time longitude latitude alt",
    # },
    # "relative_humidity": {
    #     "standard_name": "relative_humidity",
    #     "long_name": "relative humidity",
    #     "units": "",
    #     "coordinates": "launch_time longitude latitude alt",
    # },
    # "specific_humidity": {
    #     "standard_name": "specific_humidity",
    #     "long_name": "specific humidity",
    #     "units": "kg kg-1",
    #     "coordinates": "launch_time longitude latitude alt",
    # },
    # "wind_speed": {
    #     "standard_name": "wind_speed",
    #     "long_name": "wind speed",
    #     "units": "m s-1",
    #     "coordinates": "launch_time longitude latitude alt",
    # },
    # "u_wind": {
    #     "standard_name": "eastward_wind",
    #     "long_name": "u-component of the wind",
    #     "units": "m s-1",
    #     "coordinates": "launch_time longitude latitude alt",
    # },
    # "v_wind": {
    #     "standard_name": "northward_wind",
    #     "long_name": "v-component of the wind",
    #     "units": "m s-1",
    #     "coordinates": "launch_time longitude latitude alt",
    # },
    # "wind_direction": {
    #     "standard_name": "wind_from_direction",
    #     "long_name": "wind direction",
    #     "units": "degree",
    #     "coordinates": "launch_time longitude latitude alt",
    # },
    # "precipitable_water": {
    #     "standard_name": "precipitable_water",
    #     "long_name": "integrated water vapour in the measured column",
    #     "units": "kg m-2",
    #     "coordinates": "launch_time",
    # },
    # "static_stability": {
    #     "standard_name": "static_stability",
    #     "long_name": "static stability",
    #     "description": "gradient of potential temperature along the pressure grid",
    #     "units": " K hPa-1",
    #     "coordinates": "launch_time longitude latitude alt",
    # },
    # "low_height_flag": {
    #     "long_name": "flag to indicate if flight height at launch was low",
    #     "flag_values": "1, 0",
    #     "units": "",
    #     "flag_meanings": "flight height below 4 km flight height at or above 4 km",
    #     "valid_range": "0, 1",
    # },
    # "cloud_flag": {
    #     "long_name": "flag to indicate presence of cloud",
    #     "flag_values": "1, 0",
    #     "units": "",
    #     "flag_meanings": "cloud no_cloud",
    #     "valid_range": "0, 1",
    # },
    "platform_id": {
        "standard_name": "platform_id",
        "long_name": "platform which flew the circle",
        "coordinates": "circle segment_id circle_lon circle_lat circle_time",
        "units": "",
    },
    "flight_altitude": {
        "standard_name": "altitude",
        "long_name": "mean altitude of the aircraft during the circle",
        "units": "m",
        "coordinates": "circle segment_id circle_lon circle_lat circle_time",
        "positive": "up",
    },
    "segment_id": {
        "description": "unique segment ID",
        "long_name": "segment (circle) identifier",
        "cf_role": "trajectory_id",
        "units": "",
    },
    # "flight_lat": {
    #     "standard_name": "latitude",
    #     "long_name": "latitude of the aircraft when the dropsonde was launched",
    #     "units": "degree_north",
    #     "coordinates": "launch_time",
    # },
    # "flight_lon": {
    #     "standard_name": "longitude",
    #     "long_name": "longitude of the aircraft when the dropsonde was launched",
    #     "units": "degree_east",
    #     "coordinates": "launch_time",
    # },
    "circle_lon": {  # mean lon for circles at all levels fitted as least square fit to all sondes
        "standard_name": "longitude",
        "long_name": "longitude of fitted circle for all regressed sondes in circle",
        "units": "degree_east",
        # "coordinates": "circle",
        "axis": "X",
    },
    "circle_lat": {  # mean y for circles at all levels fitted as least square fit to all sondes
        "standard_name": "latitude",
        "long_name": "latitude of fitted circle for all regressed sondes in circle",
        "units": "degree_north",
        # "coordinates": "circle",
        "axis": "Y",
    },
    "circle_diameter": {  # mean diameter for circles at all levels fitted as least square fit to all sondes
        # "standard_name": "circle_diameter",
        "long_name": "diameter of fitted circle for all regressed sondes in circle",
        "units": "m",
        "coordinates": "circle segment_id circle_lon circle_lat",
    },
    "circle_time": {
        # "standard_name": "circle_time",
        "long_name": "mean launch time of all sondes in circle",
        # "units": "seconds since 1970-01-01 00:00:00 UTC",
        # "calendar": "gregorian",
        "axis": "T",
    },
    "dx": {
        # "standard_name": "delta_x",
        "long_name": "zonal distance of sonde from center of circle",
        "units": "m",
        "coordinates": "sounding alt",
    },
    "dy": {
        # "standard_name": "delta_y",
        "long_name": "meridional distance of sonde from center of circle",
        "units": "m",
        "coordinates": "sounding alt",
    },
    "u": {
        "standard_name": "eastward_wind",
        "long_name": "mean eastward wind in circle",
        "units": "m s-1",
        "coordinates": "circle segment_id circle_lon circle_lat circle_time alt",
    },
    "dudx": {
        "standard_name": "eastward_derivative_of_eastward_wind",
        "long_name": "zonal gradient of eastward wind",
        "units": "s-1",
        "coordinates": "circle segment_id circle_lon circle_lat circle_time alt",
        "ancillary_variables": "se_dudx",
    },
    "dudy": {
        "standard_name": "northward_derivative_of_eastward_wind",
        "long_name": "meridional gradient of eastward wind",
        "units": "s-1",
        "coordinates": "circle segment_id circle_lon circle_lat circle_time alt",
        "ancillary_variables": "se_dudy",
    },
    "sondes_regressed": {
        "long_name": "number of sondes regressed",
        "units": "",
        "coordinates": "circle segment_id circle_lon circle_lat circle_time alt",
    },
    "v": {
        "standard_name": "northward_wind",
        "long_name": "mean northward wind in circle",
        "units": "m s-1",
        "coordinates": "circle segment_id circle_lon circle_lat circle_time alt",
    },
    "dvdx": {
        "standard_name": "eastward_derivative_of_northward_wind",
        "long_name": "zonal gradient of northward wind",
        "units": "s-1",
        "coordinates": "circle segment_id circle_lon circle_lat circle_time alt",
        "ancillary_variables": "se_dvdx",
    },
    "dvdy": {
        "standard_name": "northward_derivative_of_northward_wind",
        "long_name": "meridional gradient of northward wind",
        "units": "s-1",
        "coordinates": "circle segment_id circle_lon circle_lat circle_time alt",
        "ancillary_variables": "se_dvdy",
    },
    "q": {
        "standard_name": "specific_humidity",
        "long_name": "mean specific humidity in circle",
        "units": "kg kg-1",
        "coordinates": "circle segment_id circle_lon circle_lat circle_time alt",
    },
    "dqdx": {
        "standard_name": "eastward_derivative_of_specific_humidity",
        "long_name": "zonal gradient of specific humidity",
        "units": "kg kg-1 m-1",
        "coordinates": "circle segment_id circle_lon circle_lat circle_time alt",
        "ancillary_variables": "se_dqdx",
    },
    "dqdy": {
        "standard_name": "northward_derivative_of_specific_humidity",
        "long_name": "meridional gradient of specific humidity",
        "units": "kg kg-1 m-1",
        "coordinates": "circle segment_id circle_lon circle_lat circle_time alt",
        "ancillary_variables": "se_dqdy",
    },
    "ta": {
        "standard_name": "air_temperature",
        "long_name": "mean air temperature in circle",
        "units": "K",
        "coordinates": "circle segment_id circle_lon circle_lat circle_time alt",
    },
    "dtadx": {
        "standard_name": "eastward_derivative_of_air_temperature",
        "long_name": "zonal gradient of temperature",
        "units": "K m-1",
        "coordinates": "circle segment_id circle_lon circle_lat circle_time alt",
        "ancillary_variables": "se_dtadx",
    },
    "dtady": {
        "standard_name": "northward_derivative_of_air_temperature",
        "long_name": "meridional gradient of temperature",
        "units": "K m-1",
        "coordinates": "circle segment_id circle_lon circle_lat circle_time alt",
        "ancillary_variables": "se_dtady",
    },
    "p": {
        "standard_name": "air_pressure",
        "long_name": "mean air pressure in circle",
        "units": "Pa",
        "coordinates": "circle segment_id circle_lon circle_lat circle_time alt",
    },
    "dpdx": {
        "standard_name": "eastward_derivative_of_air_pressure",
        "long_name": "zonal gradient of pressure",
        "units": "Pa m-1",
        "coordinates": "circle segment_id circle_lon circle_lat circle_time alt",
        "ancillary_variables": "se_dpdx",
    },
    "dpdy": {
        "standard_name": "northward_derivative_of_air_pressure",
        "long_name": "meridional gradient of pressure",
        "units": "Pa m-1",
        "coordinates": "circle segment_id circle_lon circle_lat circle_time alt",
        "ancillary_variables": "se_dpdy",
    },
    "D": {
        "standard_name": "divergence_of_wind",
        "long_name": "area averaged horizontal mass divergence",
        "units": "s-1",
        "coordinates": "circle segment_id circle_lon circle_lat circle_time alt",
        "ancillary_variables": "se_D",
    },
    "vor": {
        "standard_name": "atmosphere_upward_relative_vorticity",
        "long_name": "area averaged horizontal relative vorticity",
        "units": "s-1",
        "coordinates": "circle segment_id circle_lon circle_lat circle_time alt",
        "ancillary_variables": "se_vor",
    },
    "density": {
        "standard_name": "air_density",
        "long_name": "air density",
        "units": "kg m-3",
        "coordinates": "launch_time alt",
    },
    "mean_density": {
        "standard_name": "air_density",
        "long_name": "mean air density across all sondes in circle",
        "units": "kg m-3",
        "coordinates": "circle segment_id circle_lon circle_lat circle_time alt",
    },
    "W": {
        "standard_name": "upward_air_velocity",
        "long_name": "area averaged vertical air velocity",
        "units": "m s-1",
        "coordinates": "circle segment_id circle_lon circle_lat circle_time alt",
        "ancillary_variables": "se_W",
    },
    "omega": {
        "standard_name": "vertical_air_velocity_expressed_as_tendency_of_pressure",
        "long_name": "area averaged atmospheric pressure velocity",
        "units": "Pa s-1",
        "coordinates": "circle segment_id circle_lon circle_lat circle_time alt",
    },
    # "h_adv_q": {
    #     "standard_name": "q_advection",
    #     "long_name": "horizontal advection of specific humidity",
    #     "units": "kg kg-1 s-1",
    #     "coordinates": "circle alt",
    # },
    # "h_adv_ta": {
    #     "standard_name": "T_advection",
    #     "long_name": "horizontal advection of temperature",
    #     "units": "K s-1",
    #     "coordinates": "circle alt",
    # },
    # "h_adv_p": {
    #     "standard_name": "p_advection",
    #     "long_name": "horizontal advection of pressure",
    #     "units": "Pa s-1",
    #     "coordinates": "circle alt",
    # },
    # "h_adv_u": {
    #     "standard_name": "u_advection",
    #     "long_name": "horizontal advection of eastward wind",
    #     "units": "m s-1 s-1",
    #     "coordinates": "circle alt",
    # },
    # "h_adv_v": {
    #     "standard_name": "v_advection",
    #     "long_name": "horizontal advection of northward wind",
    #     "units": "m s-1 s-1",
    #     "coordinates": "circle alt",
    # },
    "se_dudx": {
        "standard_name": "eastward_derivative_of_eastward_wind standard_error",
        "units": "s-1",
    },
    "se_dudy": {
        "standard_name": "northward_derivative_of_eastward_wind standard_error",
        "units": "s-1",
    },
    "se_dvdx": {
        "standard_name": "eastward_derivative_of_northward_wind standard_error",
        "units": "s-1",
    },
    "se_dvdy": {
        "standard_name": "northward_derivative_of_northward_wind standard_error",
        "units": "s-1",
    },
    "se_dqdx": {
        "standard_name": "eastward_derivative_of_specific_humidity standard_error",
        "units": "kg kg-1 m-1",
    },
    "se_dqdy": {
        "standard_name": "northward_derivative_of_specific_humidity standard_error",
        "units": "kg kg-1 m-1",
    },
    "se_dpdx": {
        "standard_name": "eastward_derivative_of_air_pressure standard_error",
        "units": "Pa m-1",
    },
    "se_dpdy": {
        "standard_name": "northward_derivative_of_air_pressure standard_error",
        "units": "Pa m-1",
    },
    "se_dtadx": {
        "standard_name": "eastward_derivative_of_air_temperature standard_error",
        "units": "K m-1",
    },
    "se_dtady": {
        "standard_name": "northward_derivative_of_air_temperature standard_error",
        "units": "K m-1",
    },
    "se_D": {"standard_name": "divergence_of_wind standard_error", "units": "s-1",},
    "se_vor": {
        "standard_name": "atmosphere_upward_relative_vorticity standard_error",
        "units": "s-1",
    },
    "se_W": {"standard_name": "upward_air_velocity standard_error", "units": "m s-1",},
}

nc_dims = {
    "sounding": ["sounding"],
    "circle": ["circle"],
    "segment_id": ["circle"],
    "launch_time": ["circle", "sounding"],
    "sonde_id": ["circle", "sounding"],
    "alt": ["alt"],
    "latitude": ["circle", "sounding", "alt"],
    "longitude": ["circle", "sounding", "alt"],
    "pressure": ["circle", "sounding", "alt"],
    "temperature": ["circle", "sounding", "alt"],
    "relative_humidity": ["circle", "sounding", "alt"],
    "wind_speed": ["circle", "sounding", "alt"],
    "wind_direction": ["circle", "sounding", "alt"],
    "u_wind": ["circle", "sounding", "alt"],
    "v_wind": ["circle", "sounding", "alt"],
    "potential_temperature": ["circle", "sounding", "alt"],
    "specific_humidity": ["circle", "sounding", "alt"],
    "precipitable_water": ["circle", "sounding"],
    "static_stability": ["circle", "sounding", "alt"],
    "low_height_flag": ["circle", "sounding"],
    "cloud_flag": ["circle", "sounding", "alt"],
    "platform_id": ["circle"],
    "flight_altitude": ["circle"],
    "flight_lat": ["circle", "sounding"],
    "flight_lon": ["circle", "sounding"],
    "circle_lon": ["circle"],
    "circle_lat": ["circle"],
    "circle_diameter": ["circle"],
    "circle_time": ["circle"],
    "dx": ["circle", "sounding", "alt"],
    "dy": ["circle", "sounding", "alt"],
    "u": ["circle", "alt"],
    "dudx": ["circle", "alt"],
    "dudy": ["circle", "alt"],
    "sondes_regressed": ["circle", "alt"],
    "v": ["circle", "alt"],
    "dvdx": ["circle", "alt"],
    "dvdy": ["circle", "alt"],
    "q": ["circle", "alt"],
    "dqdx": ["circle", "alt"],
    "dqdy": ["circle", "alt"],
    "ta": ["circle", "alt"],
    "dtadx": ["circle", "alt"],
    "dtady": ["circle", "alt"],
    "p": ["circle", "alt"],
    "dpdx": ["circle", "alt"],
    "dpdy": ["circle", "alt"],
    "D": ["circle", "alt"],
    "vor": ["circle", "alt"],
    "density": ["sounding", "circle", "alt"],
    "mean_density": ["circle", "alt"],
    "W": ["circle", "alt"],
    "omega": ["circle", "alt"],
    "h_adv_q": ["circle", "alt"],
    "h_adv_ta": ["circle", "alt"],
    "h_adv_p": ["circle", "alt"],
    "h_adv_u": ["circle", "alt"],
    "h_adv_v": ["circle", "alt"],
    "se_dudx": ["circle", "alt"],
    "se_dudy": ["circle", "alt"],
    "se_dvdx": ["circle", "alt"],
    "se_dvdy": ["circle", "alt"],
    "se_dqdx": ["circle", "alt"],
    "se_dqdy": ["circle", "alt"],
    "se_dpdx": ["circle", "alt"],
    "se_dpdy": ["circle", "alt"],
    "se_dtadx": ["circle", "alt"],
    "se_dtady": ["circle", "alt"],
    "se_D": ["circle", "alt"],
    "se_vor": ["circle", "alt"],
    "se_W": ["circle", "alt"],
}

nc_global_attrs = {
    "title": "EUREC4A JOANNE Level-4",
    "doi" : f'{joanne.data_doi}'
    "created with": f"doi:{joanne.software_doi}",
    "Conventions": "CF-1.8",
    "campaign_id": "EUREC4A",
    "project_id": "JOANNE",
    "instrument_id": "Vaisala RD-41",
    "product_id": "Level-4",
    "AVAPS_software_version": "Version 4.1.2",
    "ASPEN_version": "BatchAspen v3.4.3",
    "JOANNE_version": joanne.__version__,
    "author": "Geet George",
    "author_email": "geet.george@mpimet.mpg.de",
    "featureType": "trajectory",
    "creation_time": str(datetime.datetime.utcnow()) + " UTC",
    "reference_study": "https://doi.org/10.1175/JAS-D-18-0141.1",
}
