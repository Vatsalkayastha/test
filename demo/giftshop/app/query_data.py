from openagent import compiler
from .config import Config
import logging

def get_book_course_list(topic, learning_style, budget, experience_level, preferred_format, specific_website_preference, description):
    llm = compiler.llms.OpenAI("text-davinci-003", token=Config.get_openai_key())
    
    # Define the prompt
    book_course_suggestions = compiler("""I'm looking for learning resources. My topic of interest is {{topic}}. I prefer {{learning_style}} for learning. My budget is {{budget}} rupees. My experience level is {{experience_level}}. I prefer {{preferred_format}} format. {{specific_website_preference}}, I have a preference for learning from a specific website and the website information or website link is given in the description. Here's my additional description: {{description}}. Please suggest some books and courses for me.
The following is a list of suggestions/keywords for finding resources on the web in JSON format.
```json
{
    "book_course_suggestions": [{{#geneach 'book_course_suggestions' num_iterations=10}} "{{gen 'this' temperature=1.0}}", {{~/geneach}}]
}```""", llm=llm)
    
    # Generate the list of book and course suggestions
    result = book_course_suggestions(
        topic=topic,
        learning_style=learning_style,
        budget=budget,
        experience_level=experience_level,
        preferred_format=preferred_format,
        specific_website_preference=specific_website_preference,
        description=description
    )
    logging.info(result)
    
    variables = result.variables().get('book_course_suggestions', [])
    logging.info(variables)

    return variables

