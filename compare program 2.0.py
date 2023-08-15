import easygui  
import winsound 



while 1:

        Number = easygui.enterbox("Enter asset tag or serial number:")
        with open("List.txt") as f:
         content = f.readlines()
        for item1 in content:
            item1 = item1.strip()
            if item1 == Number:
                winsound.Beep(1000, 100)  # Beep at 1000 Hz for 100 ms
                easygui.msgbox("Found")                

                
            
            

                
                msg = "Do you want to continue?"
                title = "Please Confirm"
                if easygui.ccbox(msg, title):                
                    pass
                else:
                    sys.exit(0)
       