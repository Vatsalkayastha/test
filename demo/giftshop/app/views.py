from flask import render_template, request
from app import app
from .query_data import get_book_course_list
from .serpapi import get_book_course_suggestions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggestions', methods=['POST'])
def get_gifts():
    # Get the user's answers from the form
    topic = request.form.get('topic')
    learning_style = request.form.get('learning-style')
    budget = request.form.get('budget')
    experience_level = request.form.get('experience_level')
    preferred_format = request.form.get('preferred_format')
    specific_website_preference = request.form.get('specific_website_preference')
    description = request.form.get('description')

    # Execute the logic to generate gift ideas based on the keywords
    keywords = get_book_course_list(topic, learning_style, budget, experience_level, preferred_format,specific_website_preference,description)                                
    # Query SERPAPI for each keyword and compile the results
    suggestions = []
    for keyword in keywords:
        serpapi_results = get_book_course_suggestions(keyword)  # Use the get_book_course function
        for result in serpapi_results:
            suggestion = {
                "idea": keyword, 
                "title": result.get('title', 'N/A'), 
                "link": result.get('link', 'N/A'), 
                "price": result.get('price', 'N/A'), 
                "old_price": result.get('old_price', 'N/A'), 
                "second_hand_condition": result.get('second_hand_condition', 'N/A'), 
                "rating": result.get('rating', 'N/A'), 
                "reviews": result.get('reviews', 'N/A'), 
                "store_rating": result.get('store_rating', 'N/A'), 
                "store_reviews": result.get('store_reviews', 'N/A'), 
                "number_of_comparisons": result.get('number_of_comparisons', 'N/A'), 
                "snippet": result.get('snippet', 'N/A'), 
                "thumbnail": result.get('thumbnail', 'N/A')
            }
            suggestions.append(suggestion)

    # Render the template with the results
    return render_template('suggestions.html', suggestions=suggestion)