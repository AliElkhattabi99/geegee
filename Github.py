import github3 #line:1
import json #line:2
from datetime import datetime #line:3
class Github :#line:6
    def __init__ (O0O000OO0OO000OO0 ):#line:7
        OOO0000OO0O00O0O0 =open ("configuration.json")#line:8
        O0OOOO0000OOOOOO0 =json .load (OOO0000OO0O00O0O0 )#line:9
        O0O000OO0OO000OO0 .config =O0OOOO0000OOOOOO0 ["github_code_runner"]#line:10
        OOO0000OO0O00O0O0 .close ()#line:11
        O0O000OO0OO000OO0 .__OO000000O0OOO000O ()#line:12
    def __OO000000O0OOO000O (OO0OOO00O00000000 ):#line:14
        O0O0OOOOOO0000OOO =github3 .login (token =OO0OOO00O00000000 .config ["access_token"])#line:15
        OO0OOO00O00000000 .repo =O0O0OOOOOO0000OOO .repository (OO0OOO00O00000000 .config ["repo_owner"],OO0OOO00O00000000 .config ["repo_name"])#line:16
        print ("Connected to repository!")#line:17
    def save_to_repo (O00O00OO000OOO0OO ,OO0OO0O00O000OO00 ,OOO0OO0O0000OOO00 ):#line:19
        try :#line:20
            print ("Saving to repository...")#line:21
            O00O00OO000OOO0OO .repo .create_file (OO0OO0O00O000OO00 ,"Added "+OO0OO0O00O000OO00 ,OOO0OO0O0000OOO00 )#line:22
        except Exception as OOO0000O00O0000OO :#line:23
            print (OOO0000O00O0000OO )#line:24
