from registation import users_info, TEACHERS, STUDENTS
from register_class_discipline import classroom, discipline
#Função para verificar se ja existe
def verification_existing(code_discipline_class, registration_user):
    if code_discipline_class in classroom or code_discipline_class in discipline:
        return True
    if registration_user in users_info[TEACHERS] or registration_user in users_info[STUDENTS]: 
            return True
    return False
#----------------------------------------------

#Função responsavel por verificar qual cadastro é e informar o campo adicional desse cadastro
def get_information(option):
#mudar para match case 
    if option == 2:
        disciplines_user = input('Digite as suas disciplinas separadas por virgulas: ').split(',')
        return disciplines_user
    
    elif option == 3:
        workload_discipline = input('Carga horária:')
        return workload_discipline
    
    elif option == 4:
        discipline_class = input('Disciplina: ')
        return discipline_class
    