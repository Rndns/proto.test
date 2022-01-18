import address_pb2

person = address_pb2.Person()



person.name = 'Terry'

person.age = 42

person.email = 'terry@mycompany.com'



try:

 f = open('myaddress','wb')

 f.write(person.SerializeToString())

 f.close()

 print('file is wriiten')

except IOError:

 print('file creation error')