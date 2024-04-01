import re
from flask import Flask, render_template
from app.app import app, index, home

def test_index():
    with app.test_request_context():
        # Render the template and capture the output
        rendered_html = index()

        # Normalize whitespace in the rendered HTML
        rendered_html_normalized = re.sub(r'\s+', ' ', rendered_html.strip())

        # Define the expected HTML
        expected_html = (
            "<!doctype html> <html> <head> <meta charset=\"UTF-8\"> "
            "<link rel=\"stylesheet\" href=\"/static/css/style.css\"> "
            "<title>hello</title> </head> <body> <h1>Things are going wrong!</h1> "
            "<h2>What is wrong with the leaders of today?</h2> </body> </html>"
        )

        # Normalize whitespace in the expected HTML
        expected_html_normalized = re.sub(r'\s+', ' ', expected_html.strip())
        # perform assertion
        assert rendered_html_normalized == expected_html_normalized

def test_home():
    with app.test_request_context():
        # Render the template and capture the output
        rendered_html = home()

        # Normalize whitespace in the rendered HTML
        rendered_html_normalized = re.sub(r'\s+', ' ', rendered_html.strip())

        # Define the expected HTML
        expected_html = (
            "<!doctype html> <html> <head> <meta charset=\"UTF-8\"> "
            "<link rel=\"stylesheet\" href=\"/static/css/style.css\"> "
            "<title>home</title> </head> <body> <h1>Welcome to flask</h1> "
            "</body> </html>"
        )

        # Normalize whitespace in the expected HTML
        expected_html_normalized = re.sub(r'\s+', ' ', expected_html.strip())
        # perform assertion
        assert rendered_html_normalized == expected_html_normalized
