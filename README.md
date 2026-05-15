# 🌍 Geospatial API for Spatial Analysis

A Python-based REST API built with FastAPI for geospatial data management and spatial analysis.  
The application provides endpoints for storing geographic points, performing distance-based computations, spatial filtering, and exporting data in GeoJSON format for GIS integration.

---

## 🚀 Features

- 📍 Add and manage geographic points (latitude, longitude)
- 📏 Calculate distance between two points (Haversine formula)
- 🏭 Compute distance from a fixed reference point (e.g. plant/infrastructure)
- 🔎 Filter points within a given distance
- 🗺️ Export data in GeoJSON format (GIS standard)

---

## 🧠 Use Case

This API simulates a simple geospatial analysis system that can be applied to:

- Renewable energy site selection  
- Territorial analysis  
- Proximity analysis to infrastructure  
- GIS data preprocessing  

---

## ⚙️ Tech Stack

- Python 3.9
- FastAPI
- Pydantic
- JSON (data storage)

---

## 📂 Project Structure


.
├── main.py
├── points.json
└── README.md


---

## ▶️ How to Run

1. Install dependencies:

pip install fastapi uvicorn


2. Run the server:

uvicorn main:app --reload


3. Open API docs:

http://127.0.0.1:8000/docs


---

## 📡 API Endpoints

| Endpoint | Description |
|--------|------------|
| GET /points | Retrieve stored points |
| POST /points | Add a new point |
| GET /distance | Distance between two coordinates |
| GET /distance-from-plant | Distance from fixed reference point |
| GET /points-within | Filter points within a distance |
| GET /geojson | Export all points as GeoJSON |
| GET /geojson-filtered | Export filtered points as GeoJSON |

---

## 🗺️ Example GeoJSON Output

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [14.25, 40.85]
      },
      "properties": {
        "distance_km": 1.2
      }
    }
  ]
}
```

🧩 Key Concepts Implemented (FIX)
RESTful API design
Geospatial data handling (latitude/longitude)
Haversine formula for distance calculation
Spatial filtering (distance-based queries)
GeoJSON standard for GIS interoperability
🎯 Future Improvements (FIX)
Integration with spatial databases (PostGIS)
Visualization with Leaflet / Mapbox
Advanced spatial queries (buffer, clustering)
Authentication system