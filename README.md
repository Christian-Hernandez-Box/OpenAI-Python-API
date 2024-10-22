# Recipe Blog Generator

This project generates an HTML code for a recipe blog post based on dietary restrictions, cuisine preferences, and available ingredients using OpenAI's GPT-3.5-turbo model.

## Files

- `generate_recipe_blog.py`: Contains the main function to generate the recipe blog post.
- `test_generate_recipe.py`: Contains unit tests for the `generate_recipe_blog` function.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To generate a recipe blog post, run the `generate_recipe_blog.py` script:

You can customize the dietary restrictions, cuisine preferences, and available ingredients by modifying the parameters in the generate_recipe_blog function call in the __main__ block.

##Testing

To run the tests, use pytest:
```
pytest test_generate_recipe.py
```

## Functional Details

```
def generate_recipe_blog(dietary_restrictions: str, cuisine_preferences: str, ingredients_available: str) -> None:
```

Generates an HTML code for a recipe blog post.

Parameters:
* dietary_restrictions (str): Dietary restrictions (e.g., "vegetarian, gluten-free").
* cuisine_preferences (str): Preferred cuisines (e.g., "chinese, mexican").
* ingredients_available (str): Available ingredients (e.g., "tomatoes, rice, beans").

* Returns: None
* Example:
```
generate_recipe_blog(
    dietary_restrictions="vegetarian, gluten-free",
    cuisine_preferences="chinese, mexican",
    ingredients_available="tomatoes, rice, beans"
)
```

