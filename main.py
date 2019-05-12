import sys

clients = ['pablo','ricardo']


def create_client(client_name):
   global clients
   if not _exist_client(client_name):
       clients.append(client_name)
   else:
       print('Client already is in the client\'s list')

   
def updated_client(client_name, updated_client_name):
	global clients

	if _exist_client(client_name):
		clients = clients.replace (client_name + ',', updated_client_name + ',')
	else:
		_client_not_found()


def delete_client(client_name):
    global clients

    if _exist_client(client_name):
        clients = clients.replace(client_name+',','')
    else:
        _client_not_found()


def search_client(client_name):
    global clients
    clients_list = clients.split(',')

    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True


def _add_comma():
    global clients

    clients += ','


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
    for client in clients:
        print(client)


def _exist_client(client_name):
    global clients
    return client_name in clients


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
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
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
    
    