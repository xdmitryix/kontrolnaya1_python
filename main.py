import json
import datetime

# Функции:

def add(list_notes, key_next):
    title = input("введи заголовок заметки: ")
    text = input("введи текст заметки: ")
    dt_now = datetime.datetime.now()
    iso_dt_now = dt_now.isoformat()
    assembling = []
    assembling.append(title)
    assembling.append(text)
    assembling.append(iso_dt_now)
    if (len(list_notes) == 0):
        key_next = 1
    else:
        max_key = 0
        list_notes_keys = list_notes.keys()
        for key in list_notes_keys:
            if (key > max_key):
                max_key = key
        key_next = max_key + 1
    list_notes[key_next] = assembling
    return list_notes
    
def show(list_notes):
    print("список заметок: ", list_notes)

def dell(list_notes):
    count = 0
    num = int(input("введи ID(номер) заметки: "))
    for k in list_notes.copy():
        if (k == num):
            count = count+1
            del list_notes[k]
    if (count >= 1):
        print("заметка успешно удалена!")
    else:
        print("заметка не найдена!")

def change(list_notes):
    count = 0
    num = int(input("введи ID(номер) заметки для редактирования: "))
    for k in list_notes:
        if (k == num):
            title = input("введи заголовок заметки: ")
            text = input("введи текст заметки: ")
            dt_now = datetime.datetime.now()
            iso_dt_now = dt_now.isoformat()
            assembling = []
            assembling.append(title)
            assembling.append(text)
            assembling.append(iso_dt_now)
            list_notes[k] = assembling
            count = count+1
    if (count >= 1):
        print("заметка успещно изменена!")
    else:
        print("заметка с данным ID не найдена!")

def rec(list_notes):
    count = 0
    num = int(input("введи ID(номер) заметки: "))
    for k in list_notes:
        if (k == num):
            count = count+1
            print("Искомая заметка: \n", list_notes[k])
        if (count == 0):
            print("заметка не найдена!")

def save():
    with open('notes_json.json', 'w') as outfile:
        json.dump(notes_list, outfile)
        print("изменения успешно сохранены в файл!")

def load(list_notes):
    list_notes.clear()
    with open('notes_json.json') as f:
        templates = json.load(f)
        for section, commands in templates.items():
           list_notes[int(section)] = commands
    print("файл успешно загружен!")


# Сама Программа:
notes_list = {}
next_key = 1
print("Прилождение для заметок готово к использованию!")
print("\nсписок команд:\n add - добавление заметки\n show - показать список заметок\n dell - удалить заметку\n change - изменить заметку\n rec - вывод заметки по ID\n \
save - сохранить список заметок\n load - загрузить список заметок\n help - вызвать список команд\n exit - выход\n")
while True:
    
    command = input("введите команду: ")
    if (command == "add"):
        add (notes_list, next_key)
        next_key = next_key + 1
        print ("заметка успешно добавлена!")
    elif (command == "show"):
        show(notes_list)
    elif (command == "dell"):
        dell(notes_list)
    elif (command == "change"):
        change(notes_list)
    elif (command == "rec"):
        rec(notes_list)
    elif (command == "save"):
        save()
    elif (command == "load"):
        load(notes_list)
    elif (command == "help"):
        print("\nсписок команд:\n add - добавление заметки\n show - показать список заметок\n dell - удалить заметку\n change - изменить заметку\n rec - вывод заметки по ID\n \
save - сохранить список заметок\n load - загрузить список заметок\n help - вызвать список команд\n exit - выход\n")
    elif (command == "exit"):
        break
    else:
        print("команда не найдена! введите команду  'help' для вывода списка доступных команд.")
        
