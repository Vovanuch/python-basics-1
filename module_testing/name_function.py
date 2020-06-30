''' Функция принимает части имени и выдаёт полное имя'''
def formatted_name(first_name, last_name):
    full_name = first_name.strip() + ' ' +last_name.strip()
    return full_name.title()
