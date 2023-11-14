memory = []
frame_size = 5
page_order = []

def allocate_memory(data):
    if len(memory) < frame_size:
        page_index = len(memory)
        new_page = {'data': data, 'index': page_index}
        memory.append(new_page)
        page_order.append(page_index)
    else:
        oldest = page_order.pop(0)
        new_page = {'data': data, 'index': oldest}
        page_order.append(oldest)

def access_memory(index):
    if 0 <= index < len(memory):
        print(f"Page successfully found: Page Data: {memory[index]['data']} Page index: {memory[index]['index']}")
    else:
        print("Invalid index. No such page.")

def display_curr_status():
    for counter, page in enumerate(memory, start=1):
        print(f"{counter}. Data: {page['data']} Index: {page['index']}")
    print("Memory is full") if len(memory) == frame_size else print("There is empty space in memory")

while True:
    try:
        print("\n\tMemory simulator")
        print("Choose action:")
        print("1. Allocate Memory")
        print("2. Access Memory")
        print("3. Display current status")
        print("4. Break")
        choose = int(input("Choose >>"))
        if choose == 4:
            break
        if choose > 4 or choose < 1:
            print("Invalid command")
            continue
        if choose == 1:
            usr_data = input("Enter data for saving in memory >>>")
            allocate_memory(usr_data)
        if choose == 2:
            usr_ref = int(input("Enter index for accessing data: "))
            access_memory(usr_ref)
        if choose == 3:
            display_curr_status()
    except Exception as e:
        print(f"Error: {e}")

