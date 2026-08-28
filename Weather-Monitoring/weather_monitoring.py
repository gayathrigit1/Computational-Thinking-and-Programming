import random
import time

# -----------------------------------
# Weather Monitoring System
# -----------------------------------

# Threshold values
TEMP_LIMIT = 40          # °C
HUMIDITY_LIMIT = 90      # %
WIND_LIMIT = 60          # km/h
RAIN_LIMIT = 50          # mm
PRESSURE_LIMIT = 990     # hPa


# -----------------------------------
# Collect Sensor Data
# -----------------------------------

def collect_sensor_data():
    """
    Simulates collecting data from weather sensors.
    """

    data = {
        "temperature": random.randint(20, 45),
        "humidity": random.randint(40, 100),
        "wind_speed": random.randint(10, 80),
        "rainfall": random.randint(0, 100),
        "pressure": random.randint(980, 1020)
    }

    return data


# -----------------------------------
# Validate Sensor Data
# -----------------------------------

def validate_data(data):

    if not (0 <= data["humidity"] <= 100):
        return False

    if data["wind_speed"] < 0:
        return False

    if data["rainfall"] < 0:
        return False

    if data["pressure"] <= 0:
        return False

    return True


# -----------------------------------
# Detect Abnormal Conditions
# -----------------------------------

def detect_abnormal_conditions(data):

    alerts = []

    temperature = data["temperature"]
    humidity = data["humidity"]
    wind_speed = data["wind_speed"]
    rainfall = data["rainfall"]
    pressure = data["pressure"]

    # Temperature check
    if temperature > TEMP_LIMIT:
        alerts.append(
            f"Extreme temperature detected: {temperature}°C"
        )

    # Humidity check
    if humidity > HUMIDITY_LIMIT:
        alerts.append(
            f"Very high humidity detected: {humidity}%"
        )

    # Wind check
    if wind_speed > WIND_LIMIT:
        alerts.append(
            f"High wind speed detected: {wind_speed} km/h"
        )

    # Rainfall check
    if rainfall > RAIN_LIMIT:
        alerts.append(
            f"Heavy rainfall detected: {rainfall} mm"
        )

    # Atmospheric pressure check
    if pressure < PRESSURE_LIMIT:
        alerts.append(
            f"Low atmospheric pressure detected: {pressure} hPa"
        )

    # Combined condition
    if rainfall > RAIN_LIMIT and wind_speed > WIND_LIMIT:
        alerts.append(
            "SEVERE WEATHER: Heavy rainfall + high wind"
        )

    return alerts


# -----------------------------------
# Generate Alerts
# -----------------------------------

def generate_alerts(alerts):

    if alerts:

        print("\n" + "=" * 50)
        print("🚨 WEATHER ALERT")
        print("=" * 50)

        for alert in alerts:
            print("⚠️", alert)

        print("=" * 50)

    else:
        print("\n✅ Weather conditions are normal.")


# -----------------------------------
# Main Monitoring System
# -----------------------------------

def weather_monitor():

    print("🌦️ Weather Monitoring System Started")
    print("Monitoring sensor data...\n")

    for cycle in range(10):

        print(f"\n--- Monitoring Cycle {cycle + 1} ---")

        # Collect data
        data = collect_sensor_data()

        # Display sensor readings
        print(f"Temperature : {data['temperature']} °C")
        print(f"Humidity    : {data['humidity']} %")
        print(f"Wind Speed  : {data['wind_speed']} km/h")
        print(f"Rainfall    : {data['rainfall']} mm")
        print(f"Pressure    : {data['pressure']} hPa")

        # Validate data
        if not validate_data(data):

            print("❌ Invalid sensor data!")
            continue

        # Detect abnormal conditions
        alerts = detect_abnormal_conditions(data)

        # Generate alerts immediately
        generate_alerts(alerts)

        # Wait before next reading
        time.sleep(2)

    print("\n🛑 Weather monitoring stopped.")


# Run the system
weather_monitor()