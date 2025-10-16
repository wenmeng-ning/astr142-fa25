'''
This is a quick demo on astroquery 
'''

from astroquery.simbad import Simbad
from astroquery.vizier import Vizier
from astropy import coordinates as coord
import astropy.units as u
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Query for some basic info of M31 in SIMBAD
Simbad.add_votable_fields('otypes','flux(V)','rvz_radvel')  # include object type, V-magnitude, radial velocity
obj = Simbad.query_object("M31")
print("SIMBAD entry for M31:")
print(obj)

ra_m31 = obj['RA'][0]
dec_m31 = obj['DEC'][0]
otype = obj['OTYPES'][0]
vmag_m31 = obj['FLUX_V'][0]
rv_m31 = obj['RVZ_RADVEL'][0]

print(f"RA = {ra_m31}, Dec = {dec_m31}")
print(f"Object type = {otype}")
print(f"V magnitude ≈ {vmag_m31}")
print(f"Radial velocity ≈ {rv_m31} km/s")

# Set up coordinate object for M31
m31_coord = coord.SkyCoord(ra_m31, dec_m31, unit=(u.hourangle, u.deg), frame='icrs')

# Query catalog in VizieR for M31 clusters
Vizier.ROW_LIMIT = -1  # no row limit, get entire table
catalog_id = "V/143"   
tables = Vizier.get_catalogs(catalog_id)
tbl = tables[0]
print(tbl.columns)
tbl.write('M31_clusters_rbc_full.csv',overwrite=True)

# Example: histogram of V magnitudes
df = tbl.to_pandas()
df_confirmed = df[df['f']==1]
plt.hist(df_confirmed['Vmag'].dropna(), bins=30, color='skyblue', edgecolor='black')
plt.xlabel('V magnitude')
plt.ylabel('Number of clusters')
plt.title('Distribution of V-mag for confirmed M31 GCs')
plt.gca().invert_xaxis() 
plt.show()
