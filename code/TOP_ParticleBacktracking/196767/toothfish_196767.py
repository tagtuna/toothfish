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
### PTT 196767 that drifted for at least 23 days
###========================================

### 1. Backward simulation for a month from popoff point
###----------------------------------------------------------------
o.seed_elements(lat=-51.04, lon=-40.85, time=datetime(2020,11,26,19,30,0), number=10000, radius=1500)
ncfile = 'outputBAC.nc'
o.run(time_step=timedelta(days=-1), duration=timedelta(days=-23), outfile=ncfile)
o.animation(filename='animationBAC.mp4')
o.plot(filename='simulationBAC.png')

