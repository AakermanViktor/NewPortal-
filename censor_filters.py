from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

BAD_WORDS= [
    'редиска',
    'дурак',
    'идиот',
    'тупой',
    'глупый',
]
def censor_word(word):
    if len(word)<=1:
        return word
    return word[0]+'*'*(len(word)-1)

@register.filter(name='censor')
@stringfilter
def censor(value):
    if not isinstance(value,str):
        raise TypeError('Фильтр можно применять только к строке')
    result = value
    for word in BAD_WORDS:
        result = result.replace(word,censor_word(word))
        result = result.replace(word.capitalize(),censor_word(word.capitalize()))
        result = result.replace(word.upper(),censor_word(word.upper()))
    return result
