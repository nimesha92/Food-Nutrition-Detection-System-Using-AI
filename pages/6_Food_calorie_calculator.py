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
    st.title('Calorie Calculator')




    # Predefined calorie values for some common foods (per 100 grams)
    calorie_data = {
    "Apple": 52,
        
    'Banana': 96,
    'Orange': 47,
    'Strawberry':32,
    'Grapes':69,
    'Watermelon':30,
    'Blueberry':57,
    'Mango':60,
    'Pineapple':50,
    'Avocado':160,
    'Tomato':18,
    'Carrot':41,
    'Broccoli':34,
    'Spinach':23,
    'Potato':77,
    'Sweet Potato':86,
    'Peach':39,
    'Cherry':50,
    'Pear':57,
    'Plum':46,
    'Apricot':48,
    'Kiwi':61,
    'Pomegranate':83,
    'Papaya': 43,
    'Guava':68,
    'Lychee':66,
    'Blackberry':43,
    'Raspberry':52,
    'Cranberry':46,
    'Fig':74,
    'Date':282,
    'Grapefruit':42,
    'Lemon':29,
    'Lime':30,
    'Cucumber':16,
    'Bell Pepper':31,
    'Zucchini':17,
    'Eggplant':25,
    'Pumpkin':26,
    'Corn':96,
    'Peas':81,
    'Cauliflower': 25,
    'Celery':16,
    'Lettuce':15,
    'Beetroot':43,
    'Radish':16,
    'Turnip':28,
    'Kale':49,
    'Brussels Sprouts':43
    }

    def calculate_calories(food, quantity):
        if food in calorie_data:
            return calorie_data[food] * (quantity / 100)
        else:
            return 0


    st.header("Enter the food items and their quantities")

    food_list = []
    quantity_list = []

    # Get user input
    for i in range(1, 6):  # Limiting to 5 items for simplicity
        food = st.selectbox(f"Select food item {i}", list(calorie_data.keys()), key=f"food_{i}")
        quantity = st.number_input(f"Enter quantity in grams for {food}", min_value=0, key=f"quantity_{i}")
        if quantity > 0:
            food_list.append(food)
            quantity_list.append(quantity)

    # Calculate total calories
    total_calories = 0
    if st.button("Calculate Total Calories"):
        for food, quantity in zip(food_list, quantity_list):
            total_calories += calculate_calories(food, quantity)
        st.write(f"Total Calories: {total_calories} kcal")

    st.header("Calorie Information")
    st.table(calorie_data.items())



def calculate_calories(food, quantity):
    if food in calorie_data:
        return calorie_data[food] * (quantity / 100)
    else:
        return 0


def main():
    # Displaying image
    st.image("images/home_img.jpg")
    st.title("Food Nutrition Detection Sytem Using Artificial Intelligence")
    

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

