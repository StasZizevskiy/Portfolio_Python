class Verification:
    def __init__(self, login, password): #конструктор класса
        self.login = login
        self.password = password
        self.__lenpassword()

    def __lenpassword(self): #проверка на длину пароля
        if len(self.password) < 8:
            raise ValueError ('Короткий пароль')
    def save(self): #запись полученных логинов и паролей
        with open('users', 'a') as r:
            r.write(f'{self.login, self.password}' + '\n')



class V2(Verification): #класс наследующий от суперкласса
    def __init__(self, login, password, age):
        super().__init__(login, password)
        '''
        Метод супер позволяет цеплять родительские методы, при этом напрямую не называя класс родителя
        '''
        self.__save()
        self.age = age

    def __save(self): #проверка на наличие логинов в базе
        with open('users') as r:
            for i in r:
                if f'{self.login, self.password}' + '\n' == i:
                    raise ValueError('Такой есть')
        super().save()
    def show(self):
        return self.login, self.password

x = V2('vasia', '123456789', 35)


