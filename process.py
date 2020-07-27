from app import getAllData

name = input("Введите ваше имя: ")

lastname = input("Введите вашу фамилию: ")

age = int(input("Введите ваш возраст: "))

dict_ = {
	'name': name,
	'lastname': lastname,
	'age': age
}

getAllData(dict_)