
import os
import keyboard as kb

while True:
	os.system("cls")
	print("""Выберете действие:
1. Создать файл
2. Прочитать файл
3. Перезаписать файл
4. Удалить файл
5. Запустить файл
6. Выйти
""")
	vvod = int(input("#> "))
	if vvod == 1:
		os.system("cls")
		path = input("Введите дирректорию файла: ")
		print("Построчно вводите информацию в файл. Чтобы закончить ввод в файл, введите /end")
		n = ""
		while True:
			vvod = input("> ")
			if vvod in "/end":
				break
			else:
				n += vvod
		file=open(path, "w")
		file.write(n)
		file.close()
		print("файл успешно сохранён")

	if vvod == 2:
		os.system("cls")
		path = input("Введите дирректорию файла: ")
		print("Прочитанный файл:")
		print()
		file=open(path, "r")
		print(file.read())
		print()
		file.close()
		input("Ввод для продолжения... ")
		os.system("cls")

	if vvod == 3:
		os.system("cls")
		path = input("Введите дирректорию файла: ")
		print("Построчно вводите информацию в файл. Чтобы закончить ввод в файл, введите /end")
		n = ""
		while True:
			vvod = input("> ")
			if vvod in "/end":
				break
			else:
				n += vvod
		file=open(path, "w")
		file.write(n)
		file.close()
		print("файл успешно сохранён")

	if vvod == 4:
		path = input("Введите дирректорию удаляемого файла или нажмите ввод, чтобы вернуться в главное меню: ")
		if path != "":
			os.remove(rf"{path}.txt")

	if vvod == 5:
		path = input("Введите дирректорию файла")
		os.system(path)

	if vvod == 6:
		os.system("cls")
		print("Вы уверенны, что хотите выйти? (E)xit, (C)ontinue")
		while True:
			if kb.is_pressed("E"):
				quit()
			if kb.is_pressed("C"):
				os.system("cls")
				break
	close()