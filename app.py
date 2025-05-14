import streamlit as st
import google.generativeai as genai

GEMINI_API_KEY = st.secrets["gemini_api_key"]

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

st.set_page_config(page_title="AI Recipe Generator")
st.title("AI Recipe Generator")

user_input = st.text_input("What would you like a recipe for?")

def extract_food_item(user_message):
    """
    Extract the food item from the user input using simple string processing.
    Assumes the food item is the main noun or phrase after 'recipe for' or similar.
    """
    user_message = user_message.lower().strip()
    
    prefixes = ["recipe for", "i want a recipe for", "give me a recipe for", "can you give me a recipe for"]
    
    for prefix in prefixes:
        if prefix in user_message:
            food = user_message.split(prefix)[-1].strip()
            return food
    
    return user_message

def generate_recipe_with_gemini(food):
    try:
        prompt = f"Give me a simple and easy-to-follow recipe for preparing {food}. If {food} is not a typical dish (e.g., a beverage like tea), provide a recipe for a related preparation, such as a specific type of {food} (e.g., chai tea) or a complementary dish."
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Gemini error: {e}"

if st.button("Generate Recipe"):
    if user_input:
        with st.spinner("Processing your request..."):
            # Extract the food item directly from the input
            food = extract_food_item(user_input)
            if not food:
                st.warning("Please enter a valid food item, e.g., 'Pasta' or 'Chicken Biryani'.")
            else:
                with st.spinner(f"Generating recipe for {food}..."):
                    recipe = generate_recipe_with_gemini(food)
                    st.success(recipe)
    else:
        st.warning("Please enter a food item.")