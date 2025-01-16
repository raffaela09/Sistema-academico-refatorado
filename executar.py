from registation import register_user
from register_class_discipline import register_class_discipline
from validation import verification_existing, get_information
from allocate import allocate_teacher_in_discipline, register_student_in_classroom, allocate_discipline_in_classroom
from filter_room import filter_teachers_by_discipline
from consulter import show_list_students, show_list_teachers_allocate_in_discipline, show_list_discipline_in_classroom

def exibir_opcoes():
    print('''Bem vindo!! Escolha uma opção:
          1 - Cadastrar aluno.
          2 - Cadastrar docente.
          3 - Cadastrar disciplina.
          4 - Cadastrar turma.
          5 - Filtrar professores por disciplina.
          6 - Matricular aluno em turma.
          7 - Alocar professor em disciplina.
          8 - Alocar disciplina em turma.
          9 - Consultar alunos cadastrados. 
          10 - Consultar professores cadastrados.
          11 - Consultar alunos matriculados em turmas.
          12 - Consultar professores alocados em disciplinas
          13 - Consultar disciplinas cadastradas em turmas.
          0 - Sair.
          ''')
#------------------------

#executar a função
def executar ():
     while True:
            exibir_opcoes()
            option = int(input('Digite a sua opção (em números): '))
            match option:
                case 1:
                    print('Cadastro de aluno:')
                    register_user(option, verification_existing, get_information)
                case 2:
                    print('Cadastro de professor:')
                    register_user(option, verification_existing, get_information)
                case 3:
                    print('Cadastro de disciplina:')
                    register_class_discipline(option, verification_existing, get_information)
                case 4:
                    print('Cadastro de turma:')
                    register_class_discipline(option, verification_existing, get_information)
                case 5:
                    print('Filtar professores por disciplina:')
                    filter_teachers_by_discipline(verification_existing)
                case 6:
                    print('Matricula de aluno em turma:')
                    register_student_in_classroom(verification_existing, option)
                case 7:
                    print('Alocação de professores em disciplina: ')
                    allocate_teacher_in_discipline(verification_existing, option)
                case 8:
                    print('Alocação de disciplina em turma:')
                    allocate_discipline_in_classroom(verification_existing, option)
                case 11:
                    print('Alunos matriculado nas turmas:')
                    show_list_students()
                case 12:
                    print('Professores alocados em disciplinas:')
                    show_list_teachers_allocate_in_discipline()
                case 13:
                    print('Disciplinas alocadas nas turmas:')
                    show_list_discipline_in_classroom()
                case _ :
                    print('Opção inválida, tente novamente: ')
        # except:
        #     print('Ocorreu um erro inesperado, tente novamente...')
    
executar()