from fastapi import FastAPI
import json
import os
import math
from pydantic import BaseModel
app = FastAPI()

DATA_FILE = "points.json"
IMPIANTO = {
    "lat": 40.8518,
    "lon": 14.2681
}

class Point(BaseModel):
    lat: float
    lon: float


def load_points():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_points(points):
    with open(DATA_FILE, "w") as f:
        json.dump(points, f)


@app.get("/")
def read_root():
    return {"message": "Geospatial API is running"}





@app.post("/points")
def add_point(point: Point):
    points = load_points()
    new_point = {"lat": point.lat, "lon": point.lon}
    points.append(new_point)
    save_points(points)
    return {"message": "Point added", "point": new_point}
@app.get("/points")
def get_points():
    return load_points()
def haversine(lat1,lon1,lat2,lon2):
    R=6371
    phi1=math.radians(lat1)
    phi2=math.radians(lat2)
    d_phi=math.radians(lat2-lat1)
    d_lambda=math.radians(lon2-lon1)
    a=math.sin(d_phi/2)**2+math.cos(phi1)*math.cos(phi2)*math.sin(d_lambda/2)**2
    c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
    return R*c
@app.get("/distance")
def distance(lat1: float, lon1: float, lat2: float, lon2: float):
    dist = haversine(lat1, lon1, lat2, lon2)
    return {
        "distance_km": dist
    }
@app.get("/geojson")
def get_geojson():
    points = load_points()

    features = []

    for p in points:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [p["lon"], p["lat"]]
            },
            "properties": {}
        })

    return {
        "type": "FeatureCollection",
        "features": features
    }
@app.get("/distance-from-plant")
def distance_from_plant():
    points = load_points()

    results = []

    for p in points:
        dist = haversine(
            IMPIANTO["lat"],
            IMPIANTO["lon"],
            p["lat"],
            p["lon"]
        )

        results.append({
            "point": p,
            "distance_km": dist
        })

    return {
        "plant": IMPIANTO,
        "results": results
    }
@app.get("/points-within")
def points_within(max_distance: float):
    points = load_points()

    results = []

    for p in points:
        dist = haversine(
            IMPIANTO["lat"],
            IMPIANTO["lon"],
            p["lat"],
            p["lon"]
        )

        if dist <= max_distance:
            results.append({
                "point": p,
                "distance_km": dist
            })

    return {
        "max_distance": max_distance,
        "results": results
    }
@app.get("/geojson-filtered")
def geojson_filtered(max_distance: float):
    points = load_points()

    features = []

    for p in points:
        dist = haversine(
            IMPIANTO["lat"],
            IMPIANTO["lon"],
            p["lat"],
            p["lon"]
        )

        if dist <= max_distance:
            features.append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [p["lon"], p["lat"]]
                },
                "properties": {
                    "distance_km": dist
                }
            })

    return {
        "type": "FeatureCollection",
        "features": features
    }