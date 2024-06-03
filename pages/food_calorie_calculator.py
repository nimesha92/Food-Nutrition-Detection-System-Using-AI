import streamlit as st

def food_category_tab():
    st.title('Food Categories')

    st.write('Explore different categories of food here.')
    st.write('Some popular categories include:')
    st.write('- Fruits')
    st.write('- Vegetables')
    st.write('- Dairy Products')
    st.write('- Grains')
    st.write('- Meat and Poultry')
    st.image("images/vege.jpg" )


def calories_tab():
    st.title('Calories')

    st.write('Learn about calories and their significance.')
    st.write('Calories are a measure of the energy content of food.')
    st.write('Some key points about calories:')
    st.write('- They are essential for providing energy to the body.')
    st.write('- Consuming too many calories without burning them off through activity can lead to weight gain.')
    st.write('- Different foods have different calorie counts.')
    st.write(
        """
        Calories are units of energy. In nutrition, calories refer to the energy people get from the food and drink they consume, and the energy they use in physical activity. 
        Caloric intake minus caloric expenditure determines weight gain or loss. Consuming more calories than the body needs can result in weight gain, while consuming fewer calories than needed will result in weight loss. 
        The body uses calories from food and drink to fuel its functions, such as breathing, circulating blood, and physical activity. The number of calories a person needs depends on factors like age, sex, body composition, and level of physical activity. 
        To maintain weight, energy intake should equal energy expenditure. To lose weight, energy expenditure should exceed energy intake. 
        Calories come from macronutrients in food and drink. The three main macronutrients are carbohydrates, proteins, and fats. Each gram of carbohydrate and protein provides about 4 calories, while each gram of fat provides about 9 calories. 
        Some foods are higher in calories than others. For example, foods that are high in fat and sugar tend to be higher in calories, while foods that are high in fiber tend to be lower in calories. 
        It's important to consume a balanced diet that includes a variety of nutrient-dense foods to meet the body's energy needs and maintain overall health.
        """)

def quantity_tab():
    st.title('Quantity')

    st.write('Understand portion sizes and serving quantities.')
    st.write('It\'s important to be mindful of portion sizes when consuming food.')
    st.write('Some tips for controlling portion sizes:')
    st.write('- Use smaller plates and bowls.')
    st.write('- Measure serving sizes using measuring cups and spoons.')
    st.write('- Pay attention to serving sizes listed on food packaging.')

def food_calorie_calculator_tab():
    st.title('Food Calorie Calculator')

    st.write('Calculate the total calorie count of your meals.')
    st.write('Use the food calorie calculator to keep track of your calorie intake.')
    st.write('Enter the food name, quantity, and calories per unit to get started.')
    

    # Food input form
    st.subheader('Food Input')
    food_name = st.text_input('Food Name', '')
    quantity = st.number_input('Quantity', min_value=0, step=1, value=1)
    calorie_per_unit = st.number_input('Calories per Unit', min_value=0, step=1, value=0)

    if st.button('Add Food'):
        # Add the food item to the list
        add_food_item(food_name, quantity, calorie_per_unit)

    # Display the list of food items and their calorie counts
    

    # Clear food list button
    if st.button('Clear Food List'):
        clear_food_list()

    # Calculate and display the total calorie count
    total_calories = calculate_total_calories()
    st.subheader('Total Calories')
    st.write(total_calories)

    if st.button('Get Result'):
        if any(item['name'].lower() == 'apple' for item in st.session_state.food_list):
            if total_calories > 70:
                st.error(' bad for health!')
            else:
                st.success(' good for health!')
            if any(item['name'].lower() == 'banana' for item in st.session_state.food_list):
               if total_calories > 50:
                st.error(' bad for health!')
               else:
                st.success(' good for health!')
        else:
            st.success('Selected food is good for health!')

def add_food_item(food_name, quantity, calorie_per_unit):
    # Add the food item to a data structure (e.g., list, dataframe)
    # You can choose to store this data in a database if needed
    if 'food_list' not in st.session_state:
        st.session_state.food_list = []
    st.session_state.food_list.append({'name': food_name, 'quantity': quantity, 'calories': calorie_per_unit})

def show_food_list():
    # Display the list of food items and their calorie counts
    if 'food_list' in st.session_state and len(st.session_state.food_list) > 0:
        for item in st.session_state.food_list:
            st.write(f"{item['name']}: {item['quantity']} units - {item['calories']} calories")
    else:
        st.write('No food items added yet.')

def clear_food_list():
    # Clear the list of food items
    st.session_state.food_list = []

def calculate_total_calories():
    # Calculate the total calorie count based on the food items in the list
    total_calories = 0
    if 'food_list' in st.session_state:
        for item in st.session_state.food_list:
            total_calories += item['quantity'] * item['calories']
    return total_calories

def main():
    # Displaying image
    st.image("images/home_img.jpg")
    st.title('Food Detection Prediction System')
    

    # Add custom CSS for navigation bar
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-color: #f63366;
        }
        .sidebar .sidebar-content .sidebar-top {
            color: white;
        }
        .sidebar .sidebar-content .sidebar-item {
            color: white;
        }
        .sidebar .sidebar-content .sidebar-item.selected {
            background-color: #ee3e53;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


    # Create tabs for different functionalities
    tabs = ['Food Categories', 'Calories', 'Quantity', 'Calorie Calculator']  # Renamed and organized tabs
    selected_tab = st.sidebar.radio('Navigation', tabs)

    if selected_tab == 'Food Categories':
        food_category_tab()
    elif selected_tab == 'Calories':
        calories_tab()
    elif selected_tab == 'Quantity':
        quantity_tab()
    elif selected_tab == 'Calorie Calculator':
        food_calorie_calculator_tab()

if __name__ == "__main__":
    main()

