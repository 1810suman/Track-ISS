<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>
  <h1>🛰️ ISS Tracker </h1>
  <h2>📌 Project Description</h2>
  <p>
    This project tracks the International Space Station (ISS) in real time using live TLE data from <a href="https://celestrak.org/">CelesTrak</a>. It computes upcoming visible passes over user-defined locations, plots the ISS ground track over Earth, and analyzes orbital drift using historical TLE data. The project includes both a Jupyter Notebook and a Streamlit-based web application.
  </p>

  <h2>🚀 Features</h2>
  <ul>
    <li>Fetch live TLE data for the ISS</li>
    <li>Predict upcoming passes over major cities</li>
    <li>Plot real-time ground track (90+ minutes)</li>
    <li>Analyze long-term orbital drift (inclination, eccentricity)</li>
    <li>Batch predictions via CSV input</li>
    <li>Interactive widgets for city selection (Jupyter)</li>
    <li>Streamlit web app for real-time tracking</li>
  </ul>

  <h2>🧰 Technologies Used</h2>
  <ul>
    <li>Python 3.8+</li>
    <li>Skyfield</li>
    <li>Geopy</li>
    <li>Matplotlib</li>
    <li>ipywidgets</li>
    <li>Streamlit</li>
  </ul>

  <h2>📁 Folder Structure</h2>
  <pre>
ISS-Tracker/
├── iss_tracker.ipynb
├── streamlit_app.py
├── locations.csv
├── requirements.txt
├── tle_archive/
│   ├── 2025-07-01.txt
│   └── ...
  </pre>

  <h2>📈 Sample Results</h2>
  <ul>
    <li>Inclination: ~51.64°</li>
    <li>Eccentricity: ~0.00042</li>
    <li>Orbital Period: ~92.5 minutes</li>
    <li>30-day orbital drift plotted</li>
    <li>Ground track updated every 1 minute</li>
  </ul>

  <h2>📝 How to Run</h2>
  <h3>🔬 Jupyter Notebook</h3>
  <ol>
    <li>Install dependencies with <code>pip install -r requirements.txt</code></li>
    <li>Open <code>iss_tracker.ipynb</code> and run cells</li>
  </ol>

  <h3>🌐 Streamlit App</h3>
  <ol>
    <li>Run with <code>streamlit run streamlit_app.py</code></li>
    <li>Select city and track the ISS live</li>
  </ol>

  <h2>📌 Acknowledgements</h2>
  <ul>
    <li><a href="https://celestrak.org/">CelesTrak</a> – TLE Data</li>
    <li><a href="https://rhodesmill.org/skyfield/">Skyfield</a> – Satellite Propagation</li>
    <li><a href="https://streamlit.io/">Streamlit</a> – Web App Framework</li>
  </ul>

</body>
</html>
