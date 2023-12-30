from django import template

# Import your custom tag library (blog_extras in your case)
from . import blog_extras

register = template.Library()

# You might not need to explicitly register here if it's already done in blog_extras.py
