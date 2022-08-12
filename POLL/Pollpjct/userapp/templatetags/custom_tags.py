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

@register.filter
def brTag(slogan):
    splitted = slogan.split('<br>')
    for i in range(0, len(splitted), 1):
        splitted[i] = splitted[i].strip()
        if splitted[i] == "": splitted.remove(splitted[i])

    return splitted

@register.simple_tag(name="DoubleIndex")
def DoubleIndex(to_index, p, q):
    return to_index[p][q]
