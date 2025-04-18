# 🌦️ Weather ETL Pipeline

This project implements a robust **ETL (Extract, Transform, Load)** pipeline using **Apache Airflow**, **Docker**, and **Python**. The pipeline extracts real-time weather data from the OpenWeatherMap API, transforms it into a structured format, and loads it directly into a **MongoDB Atlas** (cloud database) for storage and future analysis.

---

## 🚀 Features

- ⛅ Extracts current weather data for multiple cities using OpenWeatherMap API
- 🔄 Transforms raw JSON into clean, structured records with ISO timestamps
- ☁️ Loads transformed data into **MongoDB Atlas (Cloud)**
- 🐳 Containerized using Docker for seamless deployment
- 📅 Scheduled and orchestrated with Apache Airflow

---

## 🛠️ Tech Stack

- Python
- Apache Airflow
- Docker
- MongoDB Atlas
- Requests
- Pandas & NumPy
- Logging

---

## 🧪 How It Works

1. **Extract:** Pulls weather data from OpenWeatherMap API for a list of cities.
2. **Transform:** Cleans and reshapes the data, converting timestamps to ISO format.
3. **Load:** Inserts the structured data into a MongoDB Atlas collection.
