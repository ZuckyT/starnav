import matplotlib.pyplot as plt
from astropy.time import Time
from astroplan.plots import plot_sky
from astroplan import FixedTarget
from astropy.coordinates import EarthLocation
import astropy.units as u
import numpy as np
from astroplan import Observer

observe_time = Time(['2021-12-13 21:27:00'])
observer = Observer(longitude=-81.3077*u.deg, latitude=41.46615*u.deg, elevation=0*u.m)
observe_time = observe_time + np.linspace(-4, 5, 10)*u.hour

vega = FixedTarget.from_name("vega")
polaris = FixedTarget.from_name("Polaris")

polaris_style = {'color': 'k'}
vega_style = {'color': 'g'}
deneb_style = {'color': 'r'}

plot_sky(polaris, observer, observe_time, style_kwargs=polaris_style)
#plot_sky(altair, observer, observe_time)
plot_sky(vega, observer, observe_time, style_kwargs=vega_style)
#plot_sky(deneb, observer, observe_time, style_kwargs=deneb_style)

plt.legend(loc='center left', bbox_to_anchor=(1.25, 0.5))
plt.show()
