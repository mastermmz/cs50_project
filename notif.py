from plyer import notification
import easygui
from os import startfile
from ransomware import Soldier

def notif(input_extension ):
    notification.notify(
        title="You have a suspicious extension",

        message=f"{input_extension} extension A common extension was not detected",

        timeout=50
    )
    return


def add_extension (extension , file_name):
    with open(file_name , "a") as file:
        file.write(f"\\{extension}")


def maseg_Box_path(woring_extension , path_file):
    msg = """First check if this is a safe extension or not?
To do this, you can see the folder containing that file by clicking the "Path" button
You can start by trying to open the suspicious file
If the system could not execute the file properly with certain software, we may be dealing with a malicious extension
If the extension was secure, you can add it to the list of secure extensions by clicking the "Safe" button.

 """
    Answer = easygui.buttonbox(msg, "See the route", ("path" , "safe" ,"Unsecured"))

    if Answer == "path":
        startfile(path_file)


    elif Answer == "safe":
        Answer_local = easygui.ynbox("If you are sure, click the Yes button to add it to the list of safe" , "Are you sure it's safe?")
        if Answer_local:
            add_extension(woring_extension , "SafeExtension.txt")
        else:
            maseg_Box_path(woring_extension , path_file)

    elif Answer == "Unsecured" :
        Answer_local = easygui.ynbox("If you are sure, click the Yes button to add it to the list of Unsecured" , "Are you sure it's Unsecured?")
        if Answer_local:
            Soldier(woring_extension)
        else:
            maseg_Box_path(woring_extension , path_file)


def maseg_Box(woring_extension , path_file):
    "if yuo no extension"
    msg = f"""We found a suspicious extension called "{woring_extension}" Do you consider this extension secure?"""
    Answer = easygui.ynbox(msg ,"We found a suspicious extension" )
    if Answer:
        print("yes")
        pass
    else:
        maseg_Box_path(woring_extension ,path_file)


