"""
Hozd létre a következő streamlit appot: A mintán látható KPI-ok/key metric-ek és a chart-ok mindenképp legyenek jelen az app-odban, az elrendezés és a design (színkombinációk, tabok, oszlopok stb) a te döntésed.
A következőkre lesz szükséged:
● OpenWeatherMap API key: https://home.openweathermap.org/users/sign_in regisztrálj, és hozz létre egy saját API key-t (https://home.openweathermap.org/api_keys) amit a .streamlit mappában a secrets.toml-ben tárolsz, ahogy az órán tanultuk.
● Egy cache-elt function-re a jelenlegi időjárás lekéréséhez. Dokumentáció: https://openweathermap.org/current
● Egy másik cache-elt function-re az előrejelzésekhez (extra feladat része, nem kötelező). Dokumentáció: https://openweathermap.org/forecast5

Tipp: mind a két endpoint-hoz használhatsz egy “q” paramétert, nem kell a lat és lon paramétereket megadnod. Példák:
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
Így az url-be bekerülhet a felhasználó által megadott város. Az alábbi screenshotok alapján reprodukáld a teljes streamlit appot:

Működési elv: A felhasználónak képesnek kell lennie megadni egy létező város nevét. Az, hogy hol kéred be az inputot, rád van bízva (pl egy sidebaron, vagy ahogy a screenshoton látod). 
Ha az API hívás hibát dob, tudasd egy warning használatával a hibát. Minden városnévvel kapcsolatos text az oldalon dinamikusan változzon. 
A https://openweathermap.org/current endpoint-ról húzd le az órán tanult módon a megadott település jelenlegi hőmérsékletét, páratartalmát és a szél sebességét. Jelenítsd meg KPI-okként/key metric-enként ezeket az adatokat.
A /current response tartalmazni fogja a lat és lon paramétereket, ezeket felhasználva jeleníts meg egy térképet az st.map() segítségével (ennek önállóan utána kell járnod).
Deployold az app-ot a Community Cloud–ra, és a PR-odnak legyen része a link. A deployment-hez létre kell hoznod egy saját public repository-t, mivel csak admin joggal rendelkező felhasználó deployolhat. Ettől függetlenül a robot_dreams repo-ba PR-ként be kell adni a házi kódját a megszokott módon.
"""

import streamlit as st
import requests
import pandas as pd

# Cache-elt funkció a jelenlegi időjárás lekéréséhez
@st.cache_data
def fetch_weather_data(city, api_key):
    """Lekéri az aktuális időjárási adatokat a megadott városra."""
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    if data.get('cod') != 200:
        st.warning("Hiba történt az adatok lekérésekor. Kérlek, ellenőrizd a város nevét!")
        return None
    
    return data

def display_weather_data(weather_data, city):
    """Megjeleníti az időjárási adatokat és KPI-okat."""
    st.subheader(f"Jelenlegi időjárás {city} városában")
    
    # KPI-ok (hőmérséklet, páratartalom, szél sebesség)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="Hőmérséklet (°C)", value=f"{weather_data['main']['temp']}°C")
    
    with col2:
        st.metric(label="Páratartalom (%)", value=f"{weather_data['main']['humidity']}%")
    
    with col3:
        st.metric(label="Szél sebesség (m/s)", value=f"{weather_data['wind']['speed']} m/s")

    # Város koordinátái
    lat = weather_data['coord']['lat']
    lon = weather_data['coord']['lon']

    # Térkép megjelenítése
    st.subheader(f"{city} helye a térképen")
    st.map(pd.DataFrame({'lat': [lat], 'lon': [lon]}))

def main():
    """Fő alkalmazás funkció."""
    st.title("Időjárás és Térkép - OpenWeatherMap")

    # API kulcs betöltése a Streamlit titkos kulcsból
    api_key = st.secrets["weather"]["api_key"]

    # Város neve - text input a sidebar-on
    city = st.sidebar.text_input("Add meg a város nevét:", "Budapest")
    
    if city:
        # Időjárás adatainak lekérése
        weather_data = fetch_weather_data(city, api_key)
        
        if weather_data:
            display_weather_data(weather_data, city)

if __name__ == "__main__":
    main()
