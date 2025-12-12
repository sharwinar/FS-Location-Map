from flask import Flask, render_template, jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)

# -------------------------------------------
# Load CSVs (change filenames if needed)
# -------------------------------------------
applications_df = pd.read_csv("landata.csv")
pilot_df = pd.read_csv("pilot.csv")

# Replace NaN with None for proper JSON
applications_df = applications_df.replace({np.nan: None})
pilot_df = pilot_df.replace({np.nan: None})


# -------------------------------------------
# Home page
# -------------------------------------------
@app.route("/")
def home():
    return render_template("map.html")   # Ensure map.html is in templates/


# -------------------------------------------
# Application Flow Data
# -------------------------------------------
@app.route("/markers")
def markers():
    records = applications_df.to_dict(orient="records")
    return jsonify(records)


# -------------------------------------------
# Pilot Flow Data
# -------------------------------------------
@app.route("/pilot_markers")
def pilot_markers():
    records = pilot_df.to_dict(orient="records")
    return jsonify(records)


# -------------------------------------------
# Start server
# -------------------------------------------
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)

