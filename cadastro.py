#constantes
STUDENTS = 'students'
TEACHERS = 'teachers'
#----------------------------------------------
#dicionario com os usuarios
users = {
    'students' : {},
    'teachers': {}
}
#----------------------------------------------

#coleta de dados
def collect_data_user():
    name_user = input('Digite seu nome: ')
    registration_user = input('Digite a sua matricula: ')
    date_user = input('Digite sua data de nascimento: ')
    gender_user = input('Digite o seu gênero: ')
    telephone_user = input('Digite o seu telefone: ')
    address_user = input('Digite o seu endereço: ')
    email_user = input('Digite o seu e-mail: ')

    if user_existing(registration_user):
        print('O usuario já está cadastrado!')
        return None
    else:
     return name_user, registration_user, date_user, gender_user, telephone_user, address_user, email_user

#----------------------------------------------

#cadastrar usuario
def register_user(option):
    user_data = collect_data_user()
    if user_data is None:
        return
    name_user, registration_user, date_user, gender_user, telephone_user, address_user, email_user = user_data
    if option == 1:
        users[STUDENTS][registration_user] = {
            'nome' : name_user,
            'matricula': registration_user,
            'data': date_user,
            'genero':gender_user,
            'telefone':telephone_user,
            'endereco': address_user,
            'email': email_user 
        }
        print(f'O aluno {name_user} foi cadastrado com sucesso!')

    elif option == 2 :
       disciplines_user = input('Digite as suas disciplinas separadas por virgulas: ').split(',')
       users[TEACHERS][registration_user]={
           'nome': name_user,
           'matricula': registration_user,
           'data': date_user,
           'disciplina': disciplines_user,
           'genero': gender_user,
           'telefone': telephone_user,
           'endereco': address_user,
           'email': email_user
       }
       print(f'O docente {name_user} foi cadastrado com sucesso!')
#----------------------------------------------

#verifica se o usuario já existe
def user_existing(registration_user):
        if registration_user in users[TEACHERS] or registration_user in users[STUDENTS]: 
            return True
        return False
