classroom = {}
discipline = {}

#Função responsavel por coletar os dados em comum
def collect_data_dc(verification_existing):
    name_discipline_class = input('Nome: ')
    code_discipline_class = input('Código: ')
    teacher_discipline_class = input('Professor: ')

    if verification_existing(code_discipline_class, ''):
        print(f'{name_discipline_class} já foi cadastrado anteriormente.')
        return None
    else:
        return code_discipline_class, name_discipline_class, teacher_discipline_class
#----------------------------------------------

#Função responsavel por registrar  
def register_class_discipline (option, verification_existing, get_information):
    date_discipline_class = collect_data_dc(verification_existing)
    
    if date_discipline_class is None:
        return
    
    code_discipline_class, name_discipline_class, teacher_discipline_class = date_discipline_class 
    get_information_data = get_information(option)

    if option == 3:
        discipline[code_discipline_class] =  {
            'name': name_discipline_class,
            'code': code_discipline_class,
            'teacher': [teacher_discipline_class],
            'workload': get_information_data, 
        }
        print(discipline)
        return discipline
    elif option == 4:
        classroom[code_discipline_class]={
            'name': name_discipline_class,
            'code': code_discipline_class,
            'teacher': [teacher_discipline_class],
            'discipline': [get_information_data],
        }
        print(classroom)
        return classroom
#----------------------------------------------




