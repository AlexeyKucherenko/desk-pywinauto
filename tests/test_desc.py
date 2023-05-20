import time
import unittest  
from pywinauto import Application, Desktop

video_path = "C:\\Users\\Alexey\\Downloads\\2023-05-11_10-43-36.mp4"

def click_menuitem():
        menu = Desktop(backend='uia').window(top_level_only = True, control_type='Menu')
        menu.children()[0].click_input()

class TestDesc(unittest.TestCase):
    def test1(self):
        app = Application(backend='uia')
        orig = app.start("C:\\Program Files\\VideoLAN\VLC\\vlc.exe")
        vlc = orig['Медиапроигрыватель VLC']
        media = vlc.Menu2.items()[0]
        media.click_input()
        time.sleep(1)

        click_menuitem()

        file_explorer_window = vlc.Dialog;
        file_explorer_window.child_window(control_id=1148, control_type='Edit').type_keys(video_path)
        file_explorer_window.child_window(auto_id="1", control_type="Button").click_input()

        


def __main__():
    unittest.main()