from register_class_discipline import discipline

def data_filter(verification_existing):
    code_discipline_filter = input('Digite o código da disciplina: ')

    if verification_existing(code_discipline_filter, ''):
        return True, code_discipline_filter
    else:
        return False, None

def filter_teachers_by_discipline(verification_existing):
    sucess, code_discipline_filter = data_filter(verification_existing)
    if sucess and 'teacher' in discipline[code_discipline_filter]:
        print(discipline[code_discipline_filter]['teacher'])
    else:
        print('Disciplina não encontrada.')
        