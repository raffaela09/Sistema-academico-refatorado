from registation import TEACHERS 
from register_class_discipline import discipline, classroom
#constantes 


#recebe os dados necessário para
def allocate_data(verification_existing):
    name_allocate = input('Nome: ')
    registration_allocate = input('Matricula ou código: ')
    code_allocate = input('Código: ')
    if verification_existing(code_allocate, ''):
        return True, name_allocate, registration_allocate, code_allocate
    else:
        return False, None, None, None
#----------------------------------------------  
    
#função resposável por matricular aluno em turma
def register_student_in_classroom(verification_existing, option):  
    sucess, name_allocate, registration_allocate, code_allocate = allocate_data(verification_existing)  
    if sucess and option == 6:
        if 'list_students' in classroom[code_allocate]:
            if name_allocate not in classroom[code_allocate]['list_students']:
                    classroom[code_allocate]['list_students'].append(name_allocate)
                    print(classroom, '1')
            else:
                classroom[code_allocate]['list_students'] = [name_allocate]
                print(classroom, '2')
    else:
        print(f"Não foi encontrada a sala de aula com código {code_allocate}.")
#----------------------------------------------

#função resposavel por alocar professo em disciplina
def allocate_teacher_in_discipline(verification_existing, option):
    sucess, name_allocate, registration_allocate, code_allocate = allocate_data(verification_existing)
    if sucess and option == 7:
        if 'teacher' in discipline[code_allocate]:
                discipline[code_allocate]['teacher'].append(name_allocate)
                print(discipline)
    else:
        print(f'A disciplina não foi encontrada.')
#----------------------------------------------

#função responsável por alocar disciplina na turma
def allocate_discipline_in_classroom(verification_existing, option):
    sucess, name_allocate, registration_allocate, code_allocate = allocate_data(verification_existing)

    if sucess and option == 8:
        if 'discipline' in classroom[code_allocate]:
                classroom[code_allocate]['discipline'].append(name_allocate)
                print(classroom)
    else:
        print('A turma não foi encontrada')
#----------------------------------------------
    