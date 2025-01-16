from register_class_discipline import classroom, discipline
from allocate import allocate_teacher_in_discipline

def show_list_students():
    for item in classroom:
        print(f'Código da turma: {item}')
        if 'list_students' in classroom[item]:
            print(classroom[item]['list_students']) 
        else:
            print('Nenhum aluno matriculado')

#função responsavel por mostrar os professores alocados em disciplina
def show_list_teachers_allocate_in_discipline():
        for item in discipline:
            print(f'Disciplina: {discipline[item]['name']}')
            if 'teacher_add' in discipline[item]:
                print(discipline[item]['teacher_add'])
            else:
                 print('Nenhuma alocação para essa disciplina.')
                 
def show_list_discipline_in_classroom():
     for item in classroom:
        print(f'Turma:{classroom[item]['name']}')
        if 'discipline_add' in classroom[item]:
             print(classroom[item]['discipline_add'])
