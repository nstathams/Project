def to_jaden_case(string):
    # ВАШЕ РЕШЕНИЕ ТУТ
    words = string.split()
    capitalized_words = [word.capitalize() for word in words]
    result = ' '.join(capitalized_words)

    return result
