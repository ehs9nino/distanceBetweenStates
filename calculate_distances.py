import streamlit as st
import pandas as pd
from geopy.distance import geodesic
import folium
from streamlit_folium import folium_static

# Load processed data
data = pd.read_csv('/root/distanceBetweenStates/processed_uscities.csv')

def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).miles

def create_map(coord1, coord2, city1, city2):
    map_ = folium.Map(location=[(coord1[0] + coord2[0]) / 2, (coord1[1] + coord2[1]) / 2], zoom_start=5)
    folium.Marker(coord1, tooltip=city1).add_to(map_)
    folium.Marker(coord2, tooltip=city2).add_to(map_)
    folium.PolyLine([coord1, coord2], color="blue").add_to(map_)
    return map_

def main():
    st.markdown("""
        <style>
        .big-font {
            font-size:30px !important;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Distance Between U.S. Cities</p>', unsafe_allow_html=True)

    city_with_state1 = st.selectbox("Select the first city", data['city_with_state'].unique())
    city_with_state2 = st.selectbox("Select the second city", data['city_with_state'].unique())

    if st.button("Calculate Distance"):
        coord1 = data.loc[data['city_with_state'] == city_with_state1, ['lat', 'lng']].values[0]
        coord2 = data.loc[data['city_with_state'] == city_with_state2, ['lat', 'lng']].values[0]
        city1, city2 = city_with_state1.split(",")[0], city_with_state2.split(",")[0]
        distance = calculate_distance(coord1, coord2)
        st.write(f"The distance between {city1} and {city2} is {distance:.2f} miles.")
        map_ = create_map(coord1, coord2, city1, city2)
        folium_static(map_)

        # Additional Features
        population1 = data.loc[data['city_with_state'] == city_with_state1, 'population'].values[0]
        population2 = data.loc[data['city_with_state'] == city_with_state2, 'population'].values[0]
        density1 = data.loc[data['city_with_state'] == city_with_state1, 'density'].values[0]
        density2 = data.loc[data['city_with_state'] == city_with_state2, 'density'].values[0]

        st.write("### Population Comparison")
        st.write(f"- {city1}: {population1:,} people")
        st.write(f"- {city2}: {population2:,} people")

        st.write("### Density Information (People per sq km)")
        st.write(f"- {city1}: {density1} people/sq km")
        st.write(f"- {city2}: {density2} people/sq km")

if __name__ == "__main__":
    main()
