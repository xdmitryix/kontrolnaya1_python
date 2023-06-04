import datetime
notes_list = {}




def add(list_notes):
    title = input("введи заголовок заметки: ")
    text = input("введи текст заметки: ")
    dt_now = datetime.datetime.now()
    assembling = []
    assembling.append(title)
    assembling.append(text)
    assembling.append(dt_now)
    list_notes[1] = assembling
    return list_notes
    
def show(list_notes):
    print("список заметок: ", list_notes)
    


    




while True:
    command = input("введи команду: ")
    if (command == "add"):
        add (notes_list)
        print ("заметка успешно добавлена!")
    elif (command == "show"):
        show(notes_list)
        
