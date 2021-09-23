import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import multitasking
from upload import upload

@multitasking.task
def Soldier (input_extension):
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = True
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    def on_created(event):
        if "." in event.src_path:
            file_extension=event.src_path.split(".")
            extension = file_extension[-1:]
            if extension[0] == input_extension:
                path_file_upload = return_path(event.src_path)
                if path_file_upload !=1:
                    upload(path_file_upload)

    def on_moved(event):
        if "." in event.dest_path:
            file_extension=event.dest_path.split(".")
            extension = file_extension[-1:]
            if extension[0] == input_extension:
                path_file_upload = return_path(event.dest_path)
                upload(path_file_upload)


    my_event_handler.on_created = on_created
    my_event_handler.on_moved = on_moved


    path = "\\"
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


def return_path(file ):
    path_file = file
    fileName = path_file.split(".")
    return_find_name_file = find_name_file(file)
    if return_find_name_file == 0 :
        path_file_end = ""
        number_of_items_in_fileName = len(fileName)
        for i in range(number_of_items_in_fileName - 1):
            path_file_end = path_file_end + fileName[i]
            path_file_end = path_file_end + "."
        return path_file_end
    else:
        return 1


def find_name_file(file_name):
    path_file = file_name
    fileName = path_file.split("\\")
    file_name = fileName[-1:]
    number = find_cracter("." , file_name)
    if number == 2:
        return 0
    else:
        return 1

def find_cracter(cracter , string ):
    number = 0
    cracter = cracter
    inpput_string = string
    while index < len(inpput_string):
        letter = inpput_string[index]
        if letter == cracter:
            number = number + 1
        index = index + 1
    return number