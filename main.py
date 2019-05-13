import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software Engineer'
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer'
    }
]


def create_client(client):
   global clients
   if client not in clients:
       clients.append(client)
   else:
       print('Client already is in the client\'s list')

   
def updated_client(client_name, updated_client_name):
	if client_name in clients :
		index = clients.index(client_name)
		clients[index] = updated_client_name
	else:
		print ('Client is no it client\'s list')


def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if not idx == client_id:
            continue
        else:
            del clients[idx] 
            break
    #Si no aparecen coincidencias en las listas se envia el siiguiente mensaje
    _client_not_found()


def search_client(client_name):
    global clients

    for client in clients:
        if client != client_name:
            continue
        else:
            return True

def _print_welcome():
    print('WELCOME TO CONSOLA VENTAS')
    print('*'*50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    print('[L]ist clients')


def _client_not_found():
	return print('Client is not in clients list')


def list_clients():
    global clients
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
           uid = idx,
           name = client['name'],
           company = client['company'],
           email = client['email'],
           position = client['position']))


def _exist_client(client_name):
    global clients
    return client_name in clients

def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}?'.format(field_name))
    return field

def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name?')

        if 'exit' in client_name:
            client_name = None
            break
        
    if not client_name:
            sys.exit()    

    return client_name


#punto de entrada
if __name__ == '__main__':
    _print_welcome()
    command = input()
    command = command.upper()
    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position')
        }
        
        create_client(client)
        list_clients()
    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        if _exist_client(client_name):
            update_client = input('What is the updated client name?')
            updated_client(client_name,update_client)
            list_clients()
        else:
            _client_not_found()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    elif command == 'L':
        list_clients()
    else:
        print('Invalid command')
    
    