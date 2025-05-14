# AI Recipe Generator

## Overview

The AI Recipe Generator is a web application that allows users to input a food item (e.g., "Pizza", "Chicken Biryani") and generates a simple, easy-to-follow recipe using AI. The app extracts the food item from the user’s input using spaCy and generates recipes with the Gemini API, all presented through a Streamlit interface.

## Features

- Extracts food items from user input using lightweight NLP (spaCy).
- Generates recipes using the Gemini API.
- Simple and intuitive web interface built with Streamlit.

## Prerequisites

A Gemini API key (set up in st.secrets["gemini_api_key"])

## Setup Instructions

1. Clone the Repository (if applicable):

git clone <repository-url>
cd <repository-directory>

2. Create a Virtual Environment (recommended):

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies:

pip install -r requirements.txt

4. Download spaCy Model:

python -m spacy download en_core_web_sm

5. Set Up Gemini API Key:

Create a .streamlit/secrets.toml file in your project directory.
Add your Gemini API key:
gemini_api_key = "your-gemini-api-key"

## Usage

1. Run the App:

streamlit run app.py
This will open the app in your browser (e.g., at http://localhost:8501).

2. Enter a Food Item:
Input a food item (e.g., "Pizza", "chai tea") in the text box.
Click "Generate Recipe" to get a recipe.

## Example

Input: "Pizza"

Output:

Here's a simple and easy-to-follow recipe for preparing Homemade Margherita Pizza:

Ingredients:
- 1 pre-made pizza dough (or 1 cup flour, 1 tsp yeast, 1/2 tsp salt, 1/2 cup water for homemade dough)
- 1/2 cup tomato sauce
- 1 cup fresh mozzarella cheese, sliced
- Fresh basil leaves
- 1 tablespoon olive oil
- Salt and pepper to taste

Instructions:
1. Preheat your oven to 475°F (245°C). If using a pizza stone, place it in the oven to heat.
2. Roll out the pizza dough on a floured surface to your desired thickness.
3. Transfer the dough to a pizza tray or the heated pizza stone.
4. Spread the tomato sauce evenly over the dough, leaving a border for the crust.
5. Place the mozzarella slices on top, drizzle with olive oil, and season with salt and pepper.
6. Bake for 10-12 minutes, or until the crust is golden and the cheese is bubbly.
7. Remove from the oven, top with fresh basil leaves, and let it cool slightly before slicing.
8. Serve and enjoy!

Tip: Add your favorite toppings like olives or mushrooms for variety!
