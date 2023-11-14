def create_counter(counter = 0):
    counter_value = counter
    def increment(amount = 1):
        nonlocal counter_value
        counter_value += amount
    def decrement(amount = 1):
        nonlocal counter_value
        counter_value -= amount
    def get_counter_value():
        return counter_value

    return increment, decrement, get_counter_value

increment, decrement, get_counter = create_counter()
increment(3)
print(get_counter())
decrement(213)
print(get_counter())

