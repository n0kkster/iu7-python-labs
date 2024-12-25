import addressbook_pb2

person = addressbook_pb2.Person()
person.id = 1337
person.name = "John Doe1337"
person.email = "jjdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.PHONE_TYPE_HOME

with open('test.bin', 'wb') as f:
    f.write(person.SerializeToString())

with open('test.bin', "rb") as f:
    person.ParseFromString(f.read())
print(person)