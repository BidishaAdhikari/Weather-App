import streamlit as st
from weather_scraper import get_weather

def main():
    st.title("Weather Information App")

    city = st.text_input("Enter city name:", placeholder = 'Enter the city name here')

    if st.button("Get Weather Information"):
        try:
            temp, time, sky = get_weather(city)
            st.write("City:", city)
            st.write("Temperature:", temp)
            st.write("Time:", time)
            
            # Sky description
            if sky.lower() in ['partly cloudy', 'haze','cloudy']:    
                st.write(f"Sky Description: {sky} ☁️")
            elif "sunny" in sky.lower():
                st.write(f"Sky Description: {sky} ☀️")
            elif "rain" in sky.lower():
                st.write(f"Sky Description: {sky} 🌧️")
            else:
                st.write(f"Sky Description: {sky}")                

            
        except ValueError as e:
            st.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
