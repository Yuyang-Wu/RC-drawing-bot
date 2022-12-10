# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
#esp.osdebug(None)

#import webrepl
def do_connect(ssid, pwd):
    import network
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.active(True)
        wlan.connect(ssid, pwd)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
 
# do_connect('CMCC511', 'dufnu2-cavpuj-hohjEp')
# webrepl.start()

##################################################################################
#examples
##################################################################################

# wlan = network.WLAN(network.STA) # create station interface
# wlan.active(True)       # activate the interface
# wlan.scan()             # scan for access points
# wlan.isconnected()      # check if the station is connected to an AP
# wlan.connect(ssid='VC-Secure', auth=(WLAN.WPA2_ENT, '2039771', '8e3nuPeaT85qLyv'), [identity='myidentity', ca_certs='/flash/cert/ca.pem'])
# wlan.config('mac')      # get the interface's MAC address
# wlan.ifconfig()         # get the interface's IP/netmask/gw/DNS addresses

# ap = network.WLAN(network.AP_IF) # create access-point interface
# ap.active(True)         # activate the interface
# ap.config(ssid='ESP-AP') # set the SSID of the access point
##################################################################################
