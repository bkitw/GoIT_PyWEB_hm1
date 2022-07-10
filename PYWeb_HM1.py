import pickle
import json

print("--- Part 1 ---")


class SerializationInterface():

    def serialize(self, file):
        raise NotImplementedError('Не переназначен метод.')  # Создаётся метод-инструкция для наследующих классов


class SerializeToJSON(SerializationInterface):  # Создан класс для сериализации JSON

    def serialize(self, file):  # Наследуем и переопределяем метод родителя-интерфейса
        with open('json_data.json', 'w') as f:
            json.dump(file, f)


class SerializeToBin(SerializationInterface):  # Создан класс для сериализации .bin

    def serialize(self, file):  # Наследуем и переопределяем метод родителя-интерфейса
        with open('bin_data.bin', 'wb') as f:
            pickle.dump(file, f)


# class SerializeToFalse(SerializationInterface): # Созданный для выявления исключения класс.
#     pass
#
# falsing = SerializeToFalse()
#
# falsing.serialize('some')


json_save = SerializeToJSON()  # Создаём проверочные экземпляры классов-сериализаторов.
pickle_save = SerializeToBin()

person_1 = {'Serhii': 'Sytnik'}  # Создаём проверочные данные для сериализации.
person_2 = {'Alexander': 'Tsema'}

json_save.serialize(file=person_1)  # Вызов метода класса-сериализатора для проверки с указанием данных для
# сохранения, как ключевого аргумента.
pickle_save.serialize(person_2)  # Вызов метода класса-сериализатора для проверки
print(f'{person_1} -- данные сохранены, как json-файл.')
print(f'{person_2} -- данные сохранены, как bin-файл.')
print("||")
with open('bin_data.bin', 'rb') as fr:  # Проверка сохранения и загрузки данных через классы-сериализаторы.
    print(f'{pickle.load(fr)} -- данные загружены из bin-файла.')
with open('json_data.json', 'r') as fr:
    print(f'{json.load(fr)} -- данные загружены из json-файла.')

print("\n--- Part 2 ---")


class Meta(type):
    # Тут находится моё решение (как минимум, никаких ошибок):
    def __new__(mcs, name, bases, namespace,
                **kwargs):  # Создание метода, определяющего параметры новых экземпляров класса
        result = super().__new__(mcs, name, bases, namespace)  # Возвращение значения создаваемого экземпляра.
        result.class_number = mcs.children_number  # Создание условия присвоения порядкового номера экземпляра.
        mcs.children_number += 1  # Создание условия изменения порядкового номера экземпляра.
        return result


Meta.children_number = 1 # Здесь я лично для себя, чтобы правильно понимать, прописываю:
# ПЕРВЫЙ СОЗДАННЫЙ ЭКЗЕМПЛЯР ПОЛУЧАЕТ 1 ПОРЯДКОВЫМ НОМЕРОМ!


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


if Cls1.class_number == 1 and Cls2.class_number == 2:  # Всевозможные проверки правильности работы класса
    # и метода присвоения порядкового номера
    print('True')
else:
    print('Not True')

assert (Cls1.class_number, Cls2.class_number) == (1, 2)
print(f'Порядковый номер класса Cls1 и Cls2 соответственно -- {Cls1.class_number}, {Cls2.class_number} ')
a, b = Cls1(''), Cls2('')
assert (a.class_number, b.class_number) == (1, 2)
print(f'Порядковый номер экземпляра класса Cls1 и Cls2 соответственно -- {a.class_number}, {b.class_number} ')