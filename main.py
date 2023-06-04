import datetime
notes_list = {}
next_key = 1




def add(list_notes, key_next):
    title = input("введи заголовок заметки: ")
    text = input("введи текст заметки: ")
    dt_now = datetime.datetime.now()
    assembling = []
    assembling.append(title)
    assembling.append(text)
    assembling.append(dt_now)
    list_notes[key_next] = assembling
    return list_notes
    
def show(list_notes):
    print("список заметок: ", list_notes)
    


    




while True:
    
    command = input("введи команду: ")
    if (command == "add"):
        add (notes_list, next_key)
        next_key = next_key +1
        print ("заметка успешно добавлена!")
    elif (command == "show"):
        show(notes_list)
        
