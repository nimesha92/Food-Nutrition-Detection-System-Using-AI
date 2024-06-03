import streamlit as st

# Setting page configuration
st.set_page_config(page_title="About", page_icon="🌍")

# Displaying image
st.image("/images/home_img.jpg")

# Header
st.header("About Project")

# Description of the project
st.markdown(
    "Nutrition detection systems can contribute to scientific research and the development of new dietary guidelines, interventions, and food products. "
    "They provide valuable data on dietary patterns, nutrient intake, and the relationship between diet and health outcomes, which can inform public health policies and initiatives."
)

# Subheader for dataset description
st.subheader("About Dataset")

# Description of the dataset
st.markdown(
    "This dataset contains images of the following food items:"
    "\n\n"
    "Fruits: banana, apple, pear, grapes, orange, kiwi, watermelon, pomegranate, pineapple, mango."
    "\n\n"
    "Vegetables: cucumber, carrot, capsicum, onion, potato, lemon, tomato, radish, beetroot, cabbage, lettuce, spinach, soybean, cauliflower, bell pepper, chili pepper, turnip, corn, sweetcorn, sweet potato, paprika, jalapeno, ginger, garlic, peas, eggplant."
)

# Subheader for dataset content
st.subheader("Content")

# Description of dataset folders
st.markdown(
    "This dataset contains three folders:"
    "\n\n"
    "1. train (100 images each)"
    "\n"
    "2. test (10 images each)"
    "\n"
    "3. validation (10 images each)"
)

# Subheader for technical overview
st.subheader("Technical Overview")

# Technical overview description
st.markdown(
    "The AI model is trained using TensorFlow."
)


