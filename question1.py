def aggregate_weather_data(records):
    city_data = {}
    
    # Process each record
    for record in records:
        city = record.get('city')
        if not city:
            continue
        
        # Initialize city data if not present
        if city not in city_data:
            city_data[city] = {'temp_sum': 0, 'temp_count': 0, 'humidity_sum': 0, 'humidity_count': 0}
        
        # Update temperature data if available
        if 'temperature' in record:
            city_data[city]['temp_sum'] += record['temperature']
            city_data[city]['temp_count'] += 1
        
        # Update humidity data if available
        if 'humidity' in record:
            city_data[city]['humidity_sum'] += record['humidity']
            city_data[city]['humidity_count'] += 1
    
    aggregated_data = {}
    
    # Calculate average values for each city
    for city, data in city_data.items():
        if data['temp_count'] > 0:
            avg_temp = data['temp_sum'] / data['temp_count']
        else:
            avg_temp = None
        
        if data['humidity_count'] > 0:
            avg_humidity = data['humidity_sum'] / data['humidity_count']
        else:
            avg_humidity = None
        
        aggregated_data[city] = {'average_temperature': avg_temp, 'average_humidity': avg_humidity}
    
    return aggregated_data

# Example usage
records = [
    {'city': 'New York', 'temperature': 22, 'humidity': 56},
    {'city': 'New York', 'temperature': 25},
    {'city': 'Los Angeles', 'temperature': 30, 'humidity': 65},
    {'city': 'Los Angeles', 'humidity': 70},
    {'city': 'Chicago', 'temperature': 18, 'humidity': 55},
    {'city': 'Chicago', 'temperature': 20},
]

print(aggregate_weather_data(records))
