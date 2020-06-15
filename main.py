#Mr-Zero Project for Changing the MAC address
from mac import MAC_changer
if __name__ == "__main__":
    mc = MAC_changer()
    mac = mc.get_MAC("wlan0")
    print(mac)
    mc.change_mac("wlan0", "00:11:22:33:44:55")
    print(mac)


