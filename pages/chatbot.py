import streamlit as st
import random



# Define responses for the chatbot
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thank you!", "Feeling great!", "I'm doing well, thanks for asking!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Take care!"],
    "I want to know nutrition": ["Nutrition is the process of obtaining and using the food necessary for health and growth.",
                  "Nutrition involves the intake of food, digestion, absorption, and metabolism.",
                  "Good nutrition is essential for maintaining overall health and preventing diseases."],
    "I want to know calories": ["Calories are units of energy derived from food and beverages consumed.",
                 "The number of calories in food represents the amount of energy it provides to the body.",
                 "Balancing calorie intake with physical activity is key to maintaining a healthy weight."],
    "I want to know vitamins": ["Vitamins are organic compounds that are essential for normal growth and development.",
                 "There are 13 essential vitamins that the body needs to function properly.",
                 "Vitamins play key roles in various physiological processes, including metabolism, immunity, and cell repair."],
    "I want to know minerals": ["Minerals are inorganic nutrients that are essential for various bodily functions.",
                 "Examples of minerals include calcium, iron, potassium, and zinc.",
                 "Minerals play important roles in bone health, muscle function, and nerve signaling."],
}

# Function to generate response based on user input
def get_response(user_input):
    user_input = user_input.lower()
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return "Sorry, I don't understand that."

# Streamlit app
def main():
    # Displaying image
    st.image("D:\myprojects\STREAMLIT.DEMO\home_img.jpg")
    st.title("Food Nutrition Chatbot")
    st.title("Animated Hand")

    # Display animated hand emoji
    st.markdown("👋")


    # User input text box
    user_input = st.text_input("You:", "")

    if st.button("Send"):
        # Get response from the chatbot
        bot_response = get_response(user_input)
        st.text_area("Bot:", bot_response, height=100)

if __name__ == "__main__":
    main()
