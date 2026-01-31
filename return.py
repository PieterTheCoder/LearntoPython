def f_name(text):
    storage = text + text + text + text
    return storage

def l_name(text):
    storage2 = text + text + text + text
    return storage2

print(l_name(f_name("dog")))
print(l_name(f_name("cee")))

