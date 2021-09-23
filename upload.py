from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def upload(file):
    with open("id.txt", "r") as file:
        data = file.read()

    if data != "0" and data != None:
        id_name = f"id : {data}"
    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)
    upload_file = file
    gfile = drive.CreateFile({'parents': [{'id': id_name}]})
    gfile.SetContentFile(upload_file)
    gfile.Upload()


