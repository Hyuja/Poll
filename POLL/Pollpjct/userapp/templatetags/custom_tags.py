from django import template

register = template.Library()

@register.filter
def content_link(content):
    try:
        for i in range(0, len(content), 1):
            if content[i:i+5] == 'link:':
                to_split = content[i+6:]
                break
        link = to_split.split(" ")[0].strip()
    except:
        link = ""
    return link

@register.filter
def content_slogan(content):
    try:
        for i in range(0, len(content), 1):
            if content[i:i+7] == 'slogan:':
                to_split = content[i+8:]
                break
        slogan = to_split.strip()
    except:
        slogan = ""
    return slogan