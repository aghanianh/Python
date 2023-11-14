import uuid
import time
notes = []

def add_note():
    note_id = str(uuid.uuid4())
    content = input("Enter the content of note:... ")
    note = {'id':note_id, 'content':content}
    notes.append(note)


def list_nodes():
    if not notes:
        print("Notes not found")
        return
    for note in notes:
        print(f"Note-id: {note['id']}, Note-Content: {note['content']}")

def retrive_node(uniq):
    for note in nodes:
        if note['id'] == uniq:
             print(f"Note-id: {note['id']}, Note-Content: {note['content']}")
             return
    print('Note with given id: {uniq} not founded')

def delete_node(uniq):
    for note in notes:
        if note['id'] == uniq:
            notes.remove(note)

    print(f"Note with given {uniq} not found")

def searching_note(keyword):
    searching_notes = [note for note in notes if keyword.lower() in note['content'].lower()]
    if not searching_notes:
        print(f"there is no note with given {keyword}")
        return
    for note in searching_notes:
        print(f"your searcing Notes is:  ID: {note['id']}, Contest: {note['content']}")

while True:
    try:
        time.sleep(1)
        print("\n\nMENU")
        print("1.Adding Note:")
        print("2.List Note:")
        print("3.Retrive Note:")
        print("4.Delete Note:")
        print("5.Search Note:")
        print("6.Exit From Menu:")
        choose = int(input("Enter what you want to doing..."))
        if not (choose <= 6 and choose > 0):
            print("Enter valid nums from MENU")
            continue
        if choose == 6:
            break
        if choose == 1:
            add_note()
        elif choose == 2:
            list_nodes()
        elif choose == 3:
            user_id = input('Enter uuid for Retrive note: ')
            retrive_node(user_id)
        elif choose == 4:
            user_id = input("Enter uuid for delete note: ")
            delete_node(user_id)
        elif choose == 5:
            keyword = input("Enter keyword for searching in notes: ")
            searching_note(keyword)
        time.sleep(1)
    except Exception as e:
        print(f"An error occured: {e}")
    
