General description:
It is a multi-purpose security software whose main task is to help the user against ransomware, in such a way that the software is activated and monitors the system at any time to look for traces of ransomware activity and if Detects suspicious cases and reports it to the user so that the user can protect their files in the event of a ransomware attack.

Requirements:
Software users are all people who want to protect their information from the risk of ransomware attacks or people who want to use file encryption to secure their files.

User requirements are divided into several categories:

Ability to add secure extensions to the list of secure extensions:
Due to the sensitivity of the software on the extension of system files and the possibility of special extensions in different systems, this section allows the user to install the software to secure and specific formats of his system.
Ability to add suspicious extensions to the list of suspicious extensions for software sensitivity to extensions:
This section allows the user to manually add suspicious extensions to the list of dangerous extensions

Technical requirements:
Interface:
In this section, to create a more attractive user interface, kivy .kivymd libraries are used so that the user can work more easily with the software environment. The plyer, easygui library is used to send notifications and alerts.
Other used libraries:
The watchdog library is used to monitor the system to provide us with accurate and instant monitoring.
The os library is used to execute system commands
The pydrive library is used to upload files to Google Drive
The time library is used to create break times inside the functions
The cryptography library is used for the process of encrypting and decrypting user-selected files
The multitasking library is used for simultaneous operation of several functions and no slowness of execution when executing commands.

User scenarios:
file upload:
1. Go to the upload file menu
2. Create a Google Drive account
3. Build id (if you do not know how to build, it is displayed by pressing the training key)
4. Add an idea
5. File selection
Encrypt file:
1. Go to the folder key menu and the ENCRYPT section
2. File selection
3. By pressing the button and after the end of the encryption process, two files including the encryption file and the text file containing the encryption key will be placed.
Decrypt file:
1. Go to the folder key menu and the DECRYPT section
2. File selection
3. Write the cryptographic key
Enable system monitor:
1. Go to the security menu
2. Click on the power button
Task of each file:
Task of each file:
mian file:
Run the program
Cheker file:
Search the system and check file extensions to find suspicious extensions
Helper and interface file:
Making  UI and UX 
Notif file:
Notify the user if a suspicious item is found
Ransomware file:
Protects user files if ransomware files are found
Upload file:
Help the user to upload their files to cloud storage


