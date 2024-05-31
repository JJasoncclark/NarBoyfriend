import streamlit as st
import random

activity = ["Mini-Golf", "Laser Tag", "Arcade", "Movie", "Smoke Sesh",
            "Self-Care", "Game Night", "Hike", "Bike Ride", "Arts & Crafts", 
            "Museum", "Trampoline Park", "Sunset Drive", "Aquarium", "Bowling", 
            "Karaoke", "Picnic", "Mall", "Urban Exploring", "Thrifting", "Roller Skating", 
            "Carnival", "Color Me Mine", "Stargazing", "Drive in Movie"]
food = ["Ramen", "Pizza", "Mexican", "Thai", "American", "Pasta", 
        "Dumplings", "Chacutterie", "BYO Sandwich", "Ralphs Mukbang", "Sushi", 
        "Acai Bowls", "BBQ", "K-BBQ", "Middle Eastern"]
treat = ["Boba", "Matcha", "Cream Puffs", "Mochi", "Somi Somi", "Saffron & Rose",
         "Ice Cream", "Cinnamon Rolls", "Pie", "Wetzel Pretzel", "Mango Sticky Rice",
         "Candy", "Donuts"]

st.title("NarDateGenerator")
st.write("Press the button to generate a date!")
if st.button("Generate Date"):
    st.divider()
    col1, col2, col3 = st.columns(3)
    col1.header("Activity")
    col1.subheader(random.choice(activity))
    col2.header("Food")
    col2.subheader(random.choice(food))
    col3.header("Treat")
    col3.subheader(random.choice(treat))