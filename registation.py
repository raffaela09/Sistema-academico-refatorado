#constantes
STUDENTS = 'students'
TEACHERS = 'teachers'
#----------------------------------------------
#dicionario com os usuarios
users_info = {
    'students' : {},
    'teachers': {}
}
#----------------------------------------------

#coleta de dados
def collect_data_user(verification_existing):
    name_user = input('Digite seu nome: ')
    registration_user = input('Digite a sua matricula: ')

    if verification_existing('', registration_user):
        print('O usuario já está cadastrado!')
        return None

    date_user = input('Digite sua data de nascimento: ')
    gender_user = input('Digite o seu gênero: ')
    telephone_user = input('Digite o seu telefone: ')
    address_user = input('Digite o seu endereço: ')
    email_user = input('Digite o seu e-mail: ')

  
    
    return name_user, registration_user, date_user, gender_user, telephone_user, address_user, email_user

#----------------------------------------------

#cadastrar usuario
def register_user(option, verification_existing, get_information):
    user_data = collect_data_user(verification_existing)
    if user_data is None:
        return
    get_information_data = get_information(option)
  
    
    name_user, registration_user, date_user, gender_user, telephone_user, address_user, email_user = user_data
    if option == 1:
        users_info[STUDENTS][registration_user] = {
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
       users_info[TEACHERS][registration_user]={
           'nome': name_user,
           'matricula': registration_user,
           'data': date_user,
           'disciplina': get_information_data,
           'genero': gender_user,
           'telefone': telephone_user,
           'endereco': address_user,
           'email': email_user
       }
       print(f'O docente {name_user} foi cadastrado com sucesso!')
#----------------------------------------------



