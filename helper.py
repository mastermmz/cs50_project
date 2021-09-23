screen_helper = """
Screen:

    ScreenManager:
        MenuScreen:
        ransomwareScreen:
        keyScreen:
        upload_file_Screen:


<MenuScreen>:
    name:'menu'
    MDBoxLayout:
        orientation: "vertical"

        MDNavigationRail:
            use_hover_behavior: True
            hover_bg: 0, 0, 0, .2
            color_active: 211/255, 224/255, 234/255, 0.5
            
            MDNavigationRailItem:
                icon: "comment-account"
                text: "profile"
                on_press : root.manager.current = 'menu'
                
            MDNavigationRailItem:
                icon: "security"
                text: "security"
                on_press : 
                    root.manager.current = 'ransomware'
                    root.manager.transition.direction : 'down'

            MDNavigationRailItem:
                icon: "folder-key"
                text: "folder key"
                on_press : 
                    root.manager.current = 'key_file'
                    root.manager.transition.direction : 'down'   

            MDNavigationRailItem:
                icon: "cloud-upload"
                text: "upload file"
                on_press : root.manager.current = 'upload_file'
                
    MDLabel:
        text: "Contact us: "
        theme_text_color: "Custom"
        text_color: 1, 0, 1, 1
        pos_hint: {"x":0.1, "center_y":0.95}
        font_style : "H5"
        id : file_name_decrypt_file             
    MDLabel:
        text: "email :  caracal.anti.ransomware@gmail.com"
        pos_hint: {"x":0.1, "center_y":0.89}
        font_style : "Body1"
        id : file_name_decrypt_file
    MDLabel:
        text: "github :  github.com/mastermmz"
        pos_hint: {"x":0.1, "center_y":0.85}
        font_style : "Body1"
        id : file_name_decrypt_file    
    MDLabel:
        text: "Software description: "
        theme_text_color: "Custom"
        text_color: 0, 0, 1, 1
        pos_hint: {"x":0.1, "center_y":0.77}
        font_style : "H5"
        id : file_name_decrypt_file    
    MDLabel:
        text: "In this program, we are looking for ransomware traces in the system by checking system file extensions\\nBut know that no anti-ransomware software can completely secure your system\\nThe best way to be safe from ransomware is to have a backup of essential information\\nFor text files, it is even better to email it to yourself to make sure your information is secure\\nIt is better to use cloud storage for your videos and photos\\nLike using Google Drive\\nAnd finally\\nWe hope our software can help you deal with ransomware"
        pos_hint: {"x":0.1, "center_y":0.58}
        font_style : "Body1"
        id : file_name_decrypt_file    
    
        
        
                          
<ransomwareScreen>:
    name: 'ransomware'

    MDBoxLayout:
        orientation: "vertical"   

        MDNavigationRail:
            use_hover_behavior: True
            hover_bg: 0, 0, 0, .2
            color_active: 211/255, 224/255, 234/255, 0.5

            MDNavigationRailItem:
                icon: "comment-account"
                text: "profile"
                on_press : 
                    root.manager.current = 'menu'
                    root.manager.transition.direction : 'up'   

            MDNavigationRailItem:
                icon: "security"
                text: "security"
                on_press : 
                    root.manager.current = 'ransomware'
                     

            MDNavigationRailItem:
                icon: "folder-key"
                text: "folder key"
                on_press : 
                    root.manager.current = 'key_file'
                    root.manager.transition.direction : 'down'     
    
            MDNavigationRailItem:
                icon: "cloud-upload"
                text: "upload file"
                on_press :
                    root.manager.current = 'upload_file'

                
                
    MDFloatingActionButton:
        icon: "plus-thick"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": 0.8, "center_y": 0.7}
        user_font_size: "40sp"
        on_release : root.add_Safe_extension()
        
    MDTextField:
        hint_text : "enter extension: " 
        pos_hint :{"center_x":0.4 , "center_y":0.7}
        size_hint_x : None
        width: 300
        id : extension
        helper_text:"Enter the Safe extension"
        helper_text_mode: "on_focus"

    MDFloatingActionButton:
        icon: "shield-plus"
        md_bg_color: 1, 0, 0, 1
        pos_hint: {"center_x": 0.8, "center_y": 0.5}
        user_font_size: "40sp"
        on_release : root.add_Unsecured_extension()
        
    MDTextField:
        hint_text : "enter extension: " 
        pos_hint :{"center_x":0.4 , "center_y":0.5}
        size_hint_x : None
        width: 300
        id : extension
        helper_text:"Enter the Unsecured extension"
        helper_text_mode: "on_focus"    
    
    MDFloatingActionButton:
        icon: "power"
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {"center_x": 0.9, "center_y": 0.1}
        user_font_size: "48sp"
        on_release : root.run_WatchDog()    


<keyScreen>:
    name: 'key_file'

    MDBoxLayout:
        orientation: "vertical"


        MDBoxLayout:
                    
            MDNavigationRail:
                use_hover_behavior: True
                hover_bg: 0, 0, 0, .2
                color_active: 211/255, 224/255, 234/255, 0.5
                MDNavigationRailItem:
                    icon: "comment-account"
                    text: "profile"
                    on_press : 
                        root.manager.current = 'menu'
                        root.manager.transition.direction : 'up' 
    
                MDNavigationRailItem:
                    icon: "security"
                    text: "security"
                    on_press : 
                        root.manager.current = 'ransomware'
                        root.manager.transition.direction : 'up' 
    
                MDNavigationRailItem:
                    icon: "folder-key"
                    text: "folder key"
                    on_press : root.manager.current = 'key_file'
        
                MDNavigationRailItem:
                    icon: "cloud-upload"
                    text: "upload file"
                    on_press :
                        root.manager.current = 'upload_file'

    
            MDBottomNavigation:
               
                            
                MDBottomNavigationItem:
                    name: 'screen 1'
                    text: 'Encrypt'
                    icon: 'file-lock'
        
                    MDIconButton:
                        icon : "lock"
                        pos_hint: {"center_x": .7, "center_y": .43}
                        user_font_size: "55sp"
                        on_release : root.Encrypt_file()
                    MDIconButton:
                        icon : "file"
                        pos_hint: {"center_x": .7, "center_y": .57}
                        user_font_size: "40sp"
                        on_release : root.file_manager_Encrypt_file()
                        
                    MDLabel:
                        text: "Press the icon to select the file: "
                        pos_hint: {"x":0.2, "center_y":0.58}
                        id : file_name_Encrypt_file

                MDBottomNavigationItem:
                    name: 'screen 2'
                    text: 'decrypt'
                    icon: 'key-remove'

                    MDIconButton:
                        icon : "key"
                        pos_hint: {"center_x": .7, "center_y": .43}
                        user_font_size: "55sp"
                        on_release : root.decrypt_file()
                    MDIconButton:
                        icon : "file"
                        pos_hint: {"center_x": .7, "center_y": .57}
                        user_font_size: "40sp"
                        on_release : root.file_manager_decrypt_file()
                    MDLabel:
                        text: "Press the icon to select the file: "
                        pos_hint: {"x":0.2, "center_y":0.58}
                        id : file_name_decrypt_file
                    MDTextField:
                        hint_text : "enter key: " 
                        pos_hint :{"center_x":0.4 , "center_y":0.4}
                        size_hint_x : None
                        width: 300
                        id : key
                        helper_text:"Enter the key"
                        helper_text_mode: "on_focus"


<upload_file_Screen>:
    name: 'upload_file'

    MDBoxLayout:
        orientation: "vertical"


        MDBoxLayout:
                    
            MDNavigationRail:
                use_hover_behavior: True
                hover_bg: 0, 0, 0, .2
                color_active: 211/255, 224/255, 234/255, 0.5

                MDNavigationRailItem:
                    icon: "comment-account"
                    text: "profile"
                    on_press : 
                        root.manager.current = 'menu'
                        root.manager.transition.direction : 'up' 
    
                MDNavigationRailItem:
                    icon: "security"
                    text: "security"
                    on_press : 
                        root.manager.current = 'ransomware'
                        root.manager.transition.direction : 'up' 
    
                MDNavigationRailItem:
                    icon: "folder-key"
                    text: "folder key"
                    on_press : root.manager.current = 'key_file'
                    
                MDNavigationRailItem:
                    icon: "cloud-upload"
                    text: "upload file"
                    on_press :
                        root.manager.current = 'upload_file'

    MDIconButton:
        icon : "refresh"
        pos_hint: {"x":0.64, "center_y":0.65}
        user_font_size: "55sp"
        on_release : root.refresh()         
    MDIconButton:
        icon : "account-plus"
        pos_hint: {"x":0.74, "center_y":0.65}
        user_font_size: "50sp"
        on_release : root.account_plus()
    MDLabel:
        text: "id: "
        pos_hint: {"x":0.28, "center_y":0.65}
        id : id_name
        
        
    MDLabel:
        text: "Press the icon to select the file: "
        pos_hint: {"x":0.28, "center_y":0.52}
        id : file_name_decrypt_file 
    MDIconButton:
        icon : "file"
        pos_hint: {"center_x": 0.7, "center_y": .52}
        user_font_size: "40sp"
        on_release : root.file_manager()
        
        
    MDIconButton:
        icon : "file-upload"
        pos_hint: {"center_x": .5, "center_y": .35}
        user_font_size: "55sp"
        on_release : root.upload_file()
        
        
    MDFlatButton:
        text: "How to make ID"
        on_release : root.education()
        pos_hint: {"center_x": .9, "center_y": .05}




<Content>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"

    MDTextField:
        hint_text: "id:"
        id : key
        
        
    MDBoxLayout:
        orientation: "vertical"

        MDIconButton:
            icon : "book-education"
            pos_hint: {"center_x": .03, "center_y": .1}
            user_font_size: "20sp"
            on_release : root.education()            
        MDFlatButton:
            text : "OK"
            pos_hint: {"center_x": 0.9, "center_y": 0.1}
            on_release : root.chkec()
                        
            
            
"""


