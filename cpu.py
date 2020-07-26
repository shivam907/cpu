import psutil
def cpu():
    usage = str(psutil.cpu_percent())
    print('CPU is at '+ usage)
    battery = psutil.sensors_battery()
    print("Battery is at")
    print(battery.percent )
cpu()