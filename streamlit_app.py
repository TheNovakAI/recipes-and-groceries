import streamlit as st
import openai
import os

# Initialize OpenAI client using the API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_diet_habits():
    """Asks the user for their diet preferences."""
    st.header("Weekly Recipe Generator")
    st.write("Please answer the following questions about your diet preferences:")

    diet_type = st.selectbox(
        "What is your diet type?",
        ["Omnivore", "Vegetarian", "Vegan", "Keto", "Paleo", "Other"]
    )

    favorite_cuisines = st.text_input(
        "What are your favorite cuisines? (e.g., Italian, Mexican, Indian)"
    )

    avoid_ingredients = st.text_input(
        "Are there any ingredients you want to avoid? (e.g., nuts, dairy, gluten)"
    )

    return diet_type, favorite_cuisines, avoid_ingredients

def generate_recipes_and_grocery_list(diet_type, favorite_cuisines, avoid_ingredients):
    """Generates recipes and a grocery list using OpenAI API based on user input."""
    prompt = f"""
    You are a helpful AI assistant. Generate a week's worth of recipes and a grocery list based on the following preferences:
    
    Diet Type: {diet_type}
    Favorite Cuisines: {favorite_cuisines}
    Ingredients to Avoid: {avoid_ingredients}
    
    Provide detailed recipes for breakfast, lunch, and dinner for each day, and a consolidated grocery list.
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1500,
        n=1,
        stop=None,
        temperature=0.7,
    )

    recipes_and_grocery_list = response.choices[0].text.strip()
    return recipes_and_grocery_list

def main():
    diet_type, favorite_cuisines, avoid_ingredients = get_diet_habits()

    if st.button("Generate Weekly Recipes and Grocery List"):
        with st.spinner("Generating recipes and grocery list..."):
            recipes_and_grocery_list = generate_recipes_and_grocery_list(
                diet_type, favorite_cuisines, avoid_ingredients
            )
            st.success("Here are your recipes and grocery list for the week:")
            st.text_area("Recipes and Grocery List", value=recipes_and_grocery_list, height=400)

if __name__ == "__main__":
    main()
