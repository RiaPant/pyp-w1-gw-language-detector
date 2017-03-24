# -*- coding: utf-8 -*-


def detect_language(text, languages):
    """Returns the detected language of given text."""
    # implement your solution here
    #def languages_common_words:
    lang=""
    prevcount=0
    for language in languages:
        count=0
        x=language.get('common_words')
        for word in x:
            if word in text:
                count += 1
        if count>prevcount:
            lang=language.get('name')
            prevcount=count
    return lang
                
    

