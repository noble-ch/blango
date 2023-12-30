from django.contrib.auth import get_user_model
from django import template
from django.utils.html import format_html
from blog.models import Post

register = template.Library()
User = get_user_model()

@register.filter
def author_details(author, current_user):
    if not isinstance(author, User):
        # return empty string as safe default
        return ""

    if author == current_user:
        return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html('{}{}{}', prefix, name, suffix)

@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
    posts = Post.objects.exclude(pk=post.pk)[:5]
    return {"title": "Recent Posts", "posts": posts}

@register.simple_tag
def row(css_class=None):
    if css_class:
        return format_html('<div class="row {}">', css_class)
    else:
        return format_html('<div class="row">')

@register.simple_tag
def endrow():
    return format_html("</div>")

@register.simple_tag
def col(css_class=""):
    if css_class:
        return format_html('<div class="col {}">', css_class)
    else:
        return format_html('<div class="col">')

@register.simple_tag
def endcol():
    return format_html("</div>")

