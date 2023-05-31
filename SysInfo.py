import platform, socket, re, uuid, psutil, json, subprocess
from Github import Github


class System:
    def to_github():
        gcr = Github()
        gcr.save_to_repo(
            "SysInfo/"+System.get_machine_id() + ".data", System.sys_info().encode("utf-8")
        )

    def get_machine_id():
        return (
            subprocess.check_output("wmic csproduct get uuid")
            .decode()
            .split("\n")[1]
            .strip()
        )

    def sys_info():
        try:
            info = {}
            info["platform"] = platform.system()
            info["platform-release"] = platform.release()
            info["platform-version"] = platform.version()
            info["architecture"] = platform.machine()
            info["hostname"] = socket.gethostname()
            info["ip-address"] = socket.gethostbyname(socket.gethostname())
            info["mac-address"] = ":".join(re.findall("..", "%012x" % uuid.getnode()))
            info["processor"] = platform.processor()
            info["ram"] = (
                str(round(psutil.virtual_memory().total / (1024.0**3))) + " GB"
            )
            return json.dumps(info)
        except Exception as e:
            print(e)
System.to_github()
