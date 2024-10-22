import pytest
from unittest.mock import patch, MagicMock
from generate_recipe_blog import generate_recipe_blog

@patch('upgraded.OpenAI')
def test_generate_recipe_blog_success(MockOpenAI):
    mock_client = MockOpenAI.return_value
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "<html>Mock HTML content</html>"
    mock_client.chat.completions.create.return_value = mock_response

    with patch('builtins.print') as mocked_print:
        generate_recipe_blog(
            dietary_restrictions="vegetarian, gluten-free",
            cuisine_preferences="chinese, mexican",
            ingredients_available="tomatoes, rice, beans"
        )
        mocked_print.assert_called_once_with("<html>Mock HTML content</html>")

@patch('upgraded.OpenAI')
def test_generate_recipe_blog_failure(MockOpenAI):
    mock_client = MockOpenAI.return_value
    mock_client.chat.completions.create.side_effect = Exception("API Error")

    with patch('builtins.print') as mocked_print:
        generate_recipe_blog(
            dietary_restrictions="vegetarian, gluten-free",
            cuisine_preferences="chinese, mexican",
            ingredients_available="tomatoes, rice, beans"
        )
        mocked_print.assert_called_once_with("Error occurred: API Error")

@patch('upgraded.OpenAI')
def test_generate_recipe_blog_empty_response(MockOpenAI):
    mock_client = MockOpenAI.return_value
    mock_response = MagicMock()
    mock_response.choices[0].message.content = ""
    mock_client.chat.completions.create.return_value = mock_response

    with patch('builtins.print') as mocked_print:
        generate_recipe_blog(
            dietary_restrictions="vegetarian, gluten-free",
            cuisine_preferences="chinese, mexican",
            ingredients_available="tomatoes, rice, beans"
        )
        mocked_print.assert_called_once_with("")

@patch('upgraded.OpenAI')
def test_generate_recipe_blog_partial_response(MockOpenAI):
    mock_client = MockOpenAI.return_value
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "<html>Partial content"
    mock_client.chat.completions.create.return_value = mock_response

    with patch('builtins.print') as mocked_print:
        generate_recipe_blog(
            dietary_restrictions="vegetarian, gluten-free",
            cuisine_preferences="chinese, mexican",
            ingredients_available="tomatoes, rice, beans"
        )
        mocked_print.assert_called_once_with("<html>Partial content")

@patch('upgraded.OpenAI')
def test_generate_recipe_blog_no_dietary_restrictions(MockOpenAI):
    mock_client = MockOpenAI.return_value
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "<html>No dietary restrictions content</html>"
    mock_client.chat.completions.create.return_value = mock_response

    with patch('builtins.print') as mocked_print:
        generate_recipe_blog(
            dietary_restrictions="",
            cuisine_preferences="chinese, mexican",
            ingredients_available="tomatoes, rice, beans"
        )
        mocked_print.assert_called_once_with("<html>No dietary restrictions content</html>")

@patch('upgraded.OpenAI')
def test_generate_recipe_blog_no_cuisine_preferences(MockOpenAI):
    mock_client = MockOpenAI.return_value
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "<html>No cuisine preferences content</html>"
    mock_client.chat.completions.create.return_value = mock_response

    with patch('builtins.print') as mocked_print:
        generate_recipe_blog(
            dietary_restrictions="vegetarian, gluten-free",
            cuisine_preferences="",
            ingredients_available="tomatoes, rice, beans"
        )
        mocked_print.assert_called_once_with("<html>No cuisine preferences content</html>")

@patch('upgraded.OpenAI')
def test_generate_recipe_blog_no_ingredients_available(MockOpenAI):
    mock_client = MockOpenAI.return_value
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "<html>No ingredients available content</html>"
    mock_client.chat.completions.create.return_value = mock_response

    with patch('builtins.print') as mocked_print:
        generate_recipe_blog(
            dietary_restrictions="vegetarian, gluten-free",
            cuisine_preferences="chinese, mexican",
            ingredients_available=""
        )
        mocked_print.assert_called_once_with("<html>No ingredients available content</html>")

if __name__ == '__main__':
    pytest.main()
    mock_client = MockOpenAI.return_value
    mock_response = MagicMock()
    mock_response.choices[0].message.content = ""
    mock_client.chat.completions.create.return_value = mock_response

    with patch('builtins.print') as mocked_print:
        generate_recipe_blog(
            dietary_restrictions="vegetarian, gluten-free",
            cuisine_preferences="chinese, mexican",
            ingredients_available="tomatoes, rice, beans"
        )
        mocked_print.assert_called_once_with("")

@patch('upgraded.OpenAI')
def test_generate_recipe_blog_partial_response(MockOpenAI):
    mock_client = MockOpenAI.return_value
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "<html>Partial content"
    mock_client.chat.completions.create.return_value = mock_response

    with patch('builtins.print') as mocked_print:
        generate_recipe_blog(
            dietary_restrictions="vegetarian, gluten-free",
            cuisine_preferences="chinese, mexican",
            ingredients_available="tomatoes, rice, beans"
        )
        mocked_print.assert_called_once_with("<html>Partial content")

if __name__ == '__main__':
    pytest.main()