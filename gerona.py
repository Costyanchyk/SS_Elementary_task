treug = []  # создать пустой список
name,a,b,c = input('Введите название треугольника, сторону а, в и с через запятую ').split(',')
treug.append(name)  # в список присоединяются все введенные пользователем данные
treug.append(float(a))  
treug.append(float(b))  
treug.append(float(c))  
print('Хотите еще вводить треугольники?')
otvet = input().lower()  
while otvet == 'y' or otvet == 'yes':  # проверка ответа
    name,a,b,c = input('Введите название треугольника, сторону а, в и с через запятую ').split(',')
    treug.append(name)  
    treug.append(float(a))
    treug.append(float(b))
    treug.append(float(c))
    print('Хотите еще вводить треугольники?')
    otvet = input().lower()
plase = dict()  # создается пустой словарь
x = 4  #счетчик для движения в списке по именам треугольников
for i in range(len(treug)):
    a = treug[i * x + 1]
    b = treug[i * x + 2]
    c = treug[i * x + 3]
    p = (a + b + c ) / 2
    plase[treug[i * x]] = ((p * (p - a) * (p - b) * (p - c)) ** 0.5)
    if i == (len(treug)-4)/4:
        break
for i in range(len(plase)): 
    m = 0
    n = ''
    for key,value in plase.items():
        if float(value) >= m:
            m = float(value)
            n = key
    print('[',n,']:',m,'cm')
    plase[n] = (0)
 
        
   
   
    
        
    
    
    
                                                

