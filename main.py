import streamlit as st
import pickle
import pandas as pd
from PIL import Image


image = Image.open('Fish-Weight.jpg')

st.image(image, width=700)


st.header("Fish Weight Prediction App")
st.text_input("Enter your Name: ", key="name")

# # load model


model = pickle.load(open('best_model.pkl', "rb"))

def predict(inp_species, input_Length1, input_Length2, input_Length3, input_Height, input_Width):

    if inp_species == 'Bream':
        inp_species = 1
    elif inp_species == 'Roach':
        inp_species = 2
    elif inp_species == 'Whitefish':
        inp_species = 3
    elif inp_species == 'Parkki':
        inp_species = 4
    elif inp_species == 'Perch':
        inp_species = 5
    elif inp_species == "Pike":
        inp_species = 6
    elif inp_species == "Smelt":
        inp_species = 7

    prediction = model.predict(pd.DataFrame([[inp_species, input_Length1, input_Length2, input_Length3, input_Height, input_Width]],
                                            columns=['Species', 'Length1', 'Length2', 'Length3', 'Height','Width']))
    return prediction

st.subheader("Please select relevant features of your fish!")
left_column, right_column = st.columns(2)
with left_column:
    inp_species = st.radio(
        'Name of the fish:',
        ['Bream', 'Roach', 'Whitefish', 'Parkki', 'Perch', 'Pike', 'Smelt'])

input_Length1 = st.slider('Vertical length(cm)', 0.0, 59.0, 1.0)
input_Length2 = st.slider('Diagonal length(cm)', 0.0, 63.4, 1.0)
input_Length3 = st.slider('Cross length(cm)', 0.0, 68.0, 1.0)
input_Height = st.slider('Height(cm)', 0.0, 19.0, 1.0)
input_Width = st.slider('Diagonal width(cm)', 0.0, 9.0, 1.0)

if st.button('Make Prediction'):

    weight = predict(inp_species, input_Length1, input_Length2, input_Length3, input_Height, input_Width)

    st.write(f"Your fish weight is {weight} g")

    st.write(f"Thank you {st.session_state.name}! I hope you liked it.")
    st.write(
        f" [My Github Profile](https://github.com/Sagarkeshave)")
