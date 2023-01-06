import streamlit as st
import requests as rq
import json

# clique droit sur image: copy image adress
image_laser = "https://cdn.pixabay.com/photo/2017/11/01/14/26/star-wars-2908144__480.png"
st.markdown(f'<img src="{image_laser}" alt="Image" height="200">', unsafe_allow_html=True)


st.write("""
# **STARWARS API**

Search ***People***, ***Species***, ***Planets***, ***Starship***, ***Vehicles***, and ***Films***

""")

select = st.selectbox("Select a category:", ("people","species", "planets", "starships", "vehicles", "films"))
st.write(f"You selected: ***{select}***")

choice = ""
if select is "people" :
    choice = st.text_input("Please, type your **character**:")
elif select is "planets" :
    choice = st.text_input("Please, type your **planet**:")
elif select is "starships" :
    choice = st.text_input("please, type your **starship**:")
elif select is "species" :
    choice = st.text_input("please, type your **specie**:")
elif select is "vehicles" :
    choice = st.text_input("please, type your **vehicle**:")
elif select is "films" :
    choice = st.text_input("please, type your **film**:")
url = rq.get(f"https://swapi.dev/api/{select}/?search={choice}")


json_data = json.loads(url.text)

st.json(json_data)
