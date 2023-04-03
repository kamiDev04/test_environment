def send_messages(sd_messages, st_messages):
    while sd_messages:
        current_ms = sd_messages.pop()
        print(current_ms)
        st_messages.insert(0, current_ms)




ms = ['alloha', 'Hello, there!', 'My name is Nick', 'This is my first program', "I hope, everything be it's ok"]
st =[]
send_messages(ms[:], st)
print(ms)
print(st)