#!/usr/bin/env python
"""
Thredds (global)
==================================
"""
# Plot resolution
import matplotlib as mpl
mpl.rcParams['savefig.dpi'] = 1200
# Datetime, OceanDrift
from datetime import datetime, timedelta
from opendrift.models.oceandrift import OceanDrift

# Basic ocean drift module: current + 2% of wind
o = OceanDrift()

# Adding readers for global Thredds datasets:
# - Ocean forecast from global HYCOM model
# - Weather forecast from NOAA/NCEP
#o.add_readers_from_list([
#    'https://tds.hycom.org/thredds/dodsC/GLBy0.08/latest',
#    'https://pae-paha.pacioos.hawaii.edu/thredds/dodsC/ncep_global/NCEP_Global_Atmospheric_Model_best.ncd'])

###----------------------------------------------------------------
# Switching to HYCOM hindcast
# See temporal coverage: 
# https://opendrift.github.io/gallery/example_thredds_resources.html
###----------------------------------------------------------------
o.add_readers_from_list([
    'https://tds.hycom.org/thredds/dodsC/GLBy0.08/expt_93.0/uv3z',
    'https://pae-paha.pacioos.hawaii.edu/thredds/dodsC/ncep_global/NCEP_Global_Atmospheric_Model_best.ncd'
])

###========================================
### PTT 177084 that drifted for 4 hours max.
###========================================

### 1. Backward simulation for a month from popoff point
###----------------------------------------------------------------
o.seed_elements(lat=-54.59494, lon=-34.40048, time=datetime(2019,9,26,7,32,35), number=10000, radius=1500)
ncfile = 'outputBAC.nc'
o.run(time_step=timedelta(minutes=-30), duration=timedelta(hours=-4), outfile=ncfile)
o.animation(filename='animationBAC.mp4')
o.plot(filename='simulationBAC.png')
o.plot(background=['x_sea_water_velocity','y_sea_water_velocity'],filename='simulationBAC_uv.png')
