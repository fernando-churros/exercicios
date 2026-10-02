import re
import hashlib

class User:
    def __init__(self, name, email, passwd):
        self.name = name
        self.email = email
        self.passwd = passwd

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = self.remove_space(value, 'name')

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, value):
        email = self.remove_space(value)
        is_valid_email = re.search('.+@..+\.com', email)
        
        if is_valid_email is None:
            raise ValueError('Email inválido')
        
        self.__email = email        

    @property
    def passwd(self):
        return self.__passwd
    @passwd.setter
    def passwd(self, value):
        passwd = self.remove_space(value)
        self.__passwd = hashlib.sha256(passwd.encode()).hexdigest()

    @staticmethod
    def remove_space(value, tag='nospaces'):
        item = value.split()

        match tag:
            case 'name':
                item = ' '.join(item)
            case 'nospaces':
                item = ''.join(item)
            case _:
                return 'Não implementado'
        return item

new_user = User('fernand           o         augutos   ', 'fer@ca.com', 'coxinha123')
print(new_user.__dict__)



