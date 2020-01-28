import optparse
import subprocess
def input():
    parser=optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="please add interface")
    parser.add_option("-m", "--mode", dest="mode", help="please add interface mode")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[+]enter valid interface")
    elif not options.mode:
        parser.error("[+]enter valid mode ")
    else:
     return options
def modechanger(interface, mode):
    print("[+]try to change mode of "+interface+" to "+mode+ " mode.")
    subprocess.call(["airmon-ng", "check", "kill"])
    subprocess.call(["iwconfig", interface, "mode", mode])
    subprocess.call(["airmon-ng", "start", interface])
options = input()
modechanger(options.interface, options.mode)



