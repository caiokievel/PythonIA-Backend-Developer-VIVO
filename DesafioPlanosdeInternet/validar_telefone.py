import re

def validate_numero_telefone(phone_number):
    pattern = re.compile(r'\([0-9][0-9]\)\s9[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]')
   
    if re.match(pattern, phone_number):
        return 'Número de telefone válido.'
    else:
        return 'Número de telefone inválido.'
    
phone_number = input()  

result = validate_numero_telefone(phone_number)

print(result)