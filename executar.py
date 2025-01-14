from cadastro import register_user
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
        if option == 1:
            register_user(option)
        elif option == 2:
            register_user(option)
    
executar()