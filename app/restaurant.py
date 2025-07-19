from streamlit_folium import st_folium
import folium

def restaurant():
    # Center on France with appropriate zoom level
    m = folium.Map(location=[46.603354, 1.888334], zoom_start=6, tiles=None)

    # Ajouter différentes couches de tuiles
    folium.TileLayer('OpenStreetMap', name='OpenStreetMap').add_to(m)
    
    # Ajouter un marqueur
    folium.Marker(
        [46.603354, 1.888334], popup="France", tooltip="France"
    ).add_to(m)


    # Afficher la carte dans Streamlit
    return st_folium(m, width=725, key="my_map")