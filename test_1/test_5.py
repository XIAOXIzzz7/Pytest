from airtest.core.android.adb import ADB
adb = ADB()

def devices():
    return adb.devices()

print(devices())


