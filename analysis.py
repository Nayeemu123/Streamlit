import streamlit as st 
import pandas as pd 
import numpy as np



st.title(" Pokemon Analysis :moon:") 
st.header("Analysis Of Pokemon")
st.subheader("_By Nayeem_")


user_menu = st.sidebar.radio("Select an Analysis",("View All", "High Attack", "High Defence", "Fight Predictor"))
if user_menu == ("View All") :
 st.write("# The Pokemons we are using #")
 df = pd.read_csv("pokemon_data.csv", header= None)
 df.columns = ["No.","Name", "Type1", "Type 2", "HP", "Attack", "Defence","Sp Atk", "Sp. Def", "Speed", "Generation", "Legendary"]
 st.dataframe(df, width = 800, height = 400)

     
if user_menu == ("High Attack"):
    st.header("Highest Attack")
    st.image("mewtwo.jpeg")
    df = pd.read_csv("pokemon_data.csv", header= None)
    df.columns = ["No.","Name", "Type1", "Type 2", "HP", "Attack", "Defence","Sp Atk", "Sp. Def", "Speed", "Generation", "Legendary"]
    sorted_col = df.sort_values(by="Attack",ascending=False)
    st.write(sorted_col)
       

if user_menu == ("High Defence"):
    st.header("Highest Defence")
    st.image("213.png")
    df = pd.read_csv("pokemon_data.csv", header= None)
    df.columns = ["No.","Name", "Type1", "Type 2", "HP", "Attack", "Defence","Sp Atk", "Sp. Def", "Speed", "Generation", "Legendary"]
    sorted_colu = df.sort_values(by="Defence",ascending=False)
    st.write(sorted_colu)
       
if user_menu == ("Fight Predictor") :
    st.header ("Let's see who is the winner")
    col1, col2 = st.columns(2)
    with col1 :
     st.text_input("Choose Your Pokemon 1", "")

    with col2 :
     st.text_input("Choose Your Pokemon 2", "")
    if st.button("Result"):
        st.markdown("**Lol, You thought this will work ?**")

    