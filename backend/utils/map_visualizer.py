import folium

def generate_map(data):
    wildlife_map = folium.Map(location=[-1.2921, 36.8219], zoom_start=6)

    for entry in data:
        folium.Marker(
            location=entry['location'],
            popup=f"Animal: {entry['animal_name']}"
        ).add_to(wildlife_map)

    wildlife_map.save('templates/map_view.html')
