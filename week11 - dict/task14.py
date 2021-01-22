users=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'}, 
{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'}, 
{'name':'Princess', 'phone':'555-3141', 'email':''}, 
{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

for u in users:
    if u['phone'][-1] == '8':
        print(u['name'])

print('-------------------')

for u in users:
    if u['email'] == '':
        print(u['name'])