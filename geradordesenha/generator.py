import random

caracteres = 'qwertyuiopçlkjhgfdsazxcvbnm1234567890!@#$%¨&*()_+='

senha = ''

for x in range(17):
    senha += random.choice(caracteres)
    
   
# if senha == '':
#     for x in range(10):
#         print(random.choice(caracteres))
    
    
    
    print(senha)