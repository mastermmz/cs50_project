import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import multitasking
from ransomware import Soldier
import notif

@multitasking.task
def WatchDog (input_path):
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = True
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    def on_created(event):
        if "." in event.src_path:
            file_extension=event.src_path.split(".")
            extension = file_extension[-1:]

            paths = file_paths(event.src_path)
            print(event.src_path)
            print(paths)
            print("<============>")
            safe = Safe_extension_cheker(extension[0])
            print(f"Safe : {safe}")
            Unsecured = Unsecured_extension_cheker(extension[0])
            print(f"Unsecured : {Unsecured}")
            if ( safe == 0):
                print("part1")
                if Unsecured == 1:
                    print("part1.1")
                    notif.maseg_Box(extension[0] , paths)

                elif Unsecured == 0:
                    Soldier(extension[0])


    def on_moved(event):
        if "." in event.dest_path:
            file_extension=event.dest_path.split(".")
            extension = file_extension[-1:]
            Safe_extension_cheker(extension[0])
            paths = file_paths(event.dest_path)
            print(event.dest_path)
            print("<============>")
            safe = Safe_extension_cheker(extension[0])
            print(f"Safe : {safe}")
            Unsecured = Unsecured_extension_cheker(extension[0])
            print(f"Unsecured : {Unsecured}")
            if ( safe == 0):
                print("part1")
                if Unsecured == 1:
                    print("part1.1")
                    notif.maseg_Box(extension[0] , paths)

                elif Unsecured == 0:
                    Soldier(extension[0])

    my_event_handler.on_created = on_created
    my_event_handler.on_moved = on_moved


    path = input_path
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)
    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()



def Safe_extension_cheker (extension):
    with open("SafeExtension.txt" , "r") as file:
        data_file = file.read()
    list_extension = data_file.split("\\")
    if extension in list_extension:
        return 1
    else:

        return 0



def Unsecured_extension_cheker (extension):
    with open("UnsecuredExtension.txt" , "r") as file:
        data_file = file.read()
    list_extension = data_file.split("\\")
    if extension in list_extension:
        return 1
    else:
        return 0


def add_cheker (extension):
    with open("extension.txt" , "a") as file:
        file.write(f"\\{extension}")



def add_extension (extension , file_name):
    with open(file_name , "a") as file:
        file.write(f"\\{extension}")


def file_paths (path):
    fileName = path.split("\\")

    path_file_end = ""
    number_of_items_in_fileName = len(fileName)
    for i in range(number_of_items_in_fileName - 1):
        path_file_end = path_file_end + fileName[i]
        path_file_end = path_file_end + "\\"

    return path_file_end