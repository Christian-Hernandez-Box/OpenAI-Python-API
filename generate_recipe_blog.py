from openai import OpenAI

def generate_recipe_blog(dietary_restrictions: str, cuisine_preferences: str, ingredients_available: str) -> None:
    client = OpenAI()

    user_profile = {
        'dietary_restrictions': dietary_restrictions,
        'cuisine_preferences': cuisine_preferences,
        'ingredients_available': ingredients_available
    }

    system_prompt = {
        "role": "system",
        "content": "Generate an HTML code for a recipe blog that considers dietary restrictions, cuisine type, and ingredients."
    }

    user_content1 = (
        f"I want to create a recipe blog post. Here are my dietary restrictions: {user_profile['dietary_restrictions']}. "
        f"My cuisine preferences include: {user_profile['cuisine_preferences']}. "
        f"The ingredients I have available are: {user_profile['ingredients_available']}."
    )

    user_content2 = (
        "Please provide a blog post with a title, description, ingredients, and instructions. "
        "Format the ingredients as a bulleted list and the instructions as numbered steps."
    )

    user_content3 = "The recipe must use only the listed ingredients and should result in a single blog post with instructions not exceeding six steps."

    user_prompt = {
        "role": "user",
        "content": f"{user_content1}\n{user_content2}\n{user_content3}"
    }

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[system_prompt, user_prompt]
        )
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    generate_recipe_blog(
        dietary_restrictions="vegetarian, gluten-free",
        cuisine_preferences="chinese, mexican",
        ingredients_available="tomatoes, rice, beans"
    )
