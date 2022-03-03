import keyboard, time

while True:
    
    print("Key to Spam :")
    KeySpam = input()
    print("Key to Stop :")
    KeyStop = input()
    if KeySpam == KeyStop :
        print("Same key")
        continue
    else:
        break

Spam = False

print("Start, press ",KeySpam,' to begin the spam and ', KeyStop ,'to stop')
while True:
    try:

        if keyboard.is_pressed(KeySpam):
            Spam = True

        if keyboard.is_pressed(KeyStop):
            Spam = False
            time.sleep(1) # Prevent keyboard.press_and_release(KeySpam) to activate keyboard.is_pressed(KeySpam)

        if Spam == True:
            keyboard.press_and_release(KeySpam)
                
        time.sleep(0.01)  # time.sleep -> prevent the cpu to explode
    except:
        break
