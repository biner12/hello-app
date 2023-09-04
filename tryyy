import streamlit as st

def calculate_volume(length, width, height):
    return length * width * height

def calculate_cost(volume, unit_price):
    return volume * unit_price

st.title("Construction Estimation Calculator")

length = st.number_input("Length:", value=0.0, step=0.1)
width = st.number_input("Width:", value=0.0, step=0.1)
height = st.number_input("Height:", value=0.0, step=0.1)
unit_price = st.number_input("Unit Price:", value=0.0, step=0.1)

if st.button("Calculate"):
    volume = calculate_volume(length, width, height)
    total_cost = calculate_cost(volume, unit_price)
    st.write(f"Volume: {volume:.2f}")
    st.write(f"Total Cost: {total_cost:.2f}")


def sub(*args):
    result_place = Element('output')
    result_place.write(f"<p>Dear {Element('FullName').value},<p>Thank you for submitting your question. We will respond to you at <b>{Element('email').value}<b>as soon as possible.</p><p><br><b><u>Your Question</u></b>:<br>{Element('question').value}")
    target = document.getElementbyId("output")
    target.style.backgroundColor = "gainsbro"
