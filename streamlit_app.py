
import streamlit as st
from datetime import datetime, timedelta, timezone
from skyfield.api import load, EarthSatellite, Topos
import matplotlib.pyplot as plt
import pandas as pd
import requests

# Load Skyfield timescale
ts = load.timescale()

# City coordinates
cities = {
    "Delhi": (28.6139, 77.2090),
    "Mumbai": (19.0760, 72.8777),
    "Bengaluru": (12.9716, 77.5946),
    "Kolkata": (22.5726, 88.3639),
    "Hyderabad": (17.3850, 78.4867)
}

# Fetch latest ISS TLE
@st.cache_data(ttl=3600)
def fetch_iss_tle():
    url = "https://celestrak.org/NORAD/elements/stations.txt"
    response = requests.get(url)
    lines = response.text.strip().split('\n')
    for i in range(len(lines)):
        if "ISS" in lines[i]:
            return lines[i], lines[i+1], lines[i+2]
    raise Exception("ISS TLE not found.")

# Plot ground track
def plot_ground_track(satellite, duration_minutes=90):
    start_time = datetime.now(timezone.utc)
    datetimes = [start_time + timedelta(minutes=i) for i in range(duration_minutes)]
    times = ts.from_datetimes(datetimes)

    lats, lons = [], []
    for t in times:
        geo = satellite.at(t).subpoint()
        lats.append(geo.latitude.degrees)
        lons.append(geo.longitude.degrees)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(lons, lats, label='ISS Path')
    ax.scatter(lons[0], lats[0], color='red', label='Current Position')
    ax.set_title("ISS Ground Track (Next {} Minutes)".format(duration_minutes))
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.grid(True)
    ax.legend()
    return fig

# Main App
st.title("🛰 Real-Time ISS Tracker")
st.markdown("Track the International Space Station in real-time and predict its passes over major Indian cities.")

# Fetch satellite object
name, line1, line2 = fetch_iss_tle()
satellite = EarthSatellite(line1, line2, name, ts)

# City & duration selection
city = st.selectbox("Choose a city:", list(cities.keys()))
duration = st.slider("Ground track duration (minutes):", min_value=30, max_value=180, value=90, step=10)

lat, lon = cities[city]
location = Topos(latitude_degrees=lat, longitude_degrees=lon)

# Predict next pass
st.subheader(f"Next ISS pass over {city}")
t0 = ts.from_datetime(datetime.now(timezone.utc))
t1 = ts.from_datetime(datetime.now(timezone.utc) + timedelta(days=1))

try:
    times, events = satellite.find_events(location, t0, t1, altitude_degrees=30.0)
    event_names = ['Rise 🌅', 'Culminate 🌕', 'Set 🌇']
    for t, e in zip(times, events):
        st.write(f"{event_names[e]}: {t.utc_datetime():%Y-%m-%d %H:%M:%S UTC}")
except Exception as e:
    st.warning("Could not calculate pass times.")

# Plot ground track
st.subheader("ISS Ground Track")
fig = plot_ground_track(satellite, duration)
st.pyplot(fig)
