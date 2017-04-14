from django import template
register = template.Library()
@register.filter(name='Lower')
def lower(text):
    return text.lower()
@register.filter
def question_choice_count(question):
    return question.choices.count()
@register.filter
def question_choice_add(question, num):
    return question.choices.count() + int(num)
