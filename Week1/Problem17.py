# inputted seconds become formatted hh:mm:ss

inputSeconds = int(input())
hours = str(inputSeconds // 3600 % 24)
minutes = str((inputSeconds % 3600) // 60)
seconds = str(inputSeconds % 3600 % 60)
if len(minutes) == 1:
    minutes = "0"+minutes
if len(seconds) == 1:
    seconds = "0"+seconds
print(hours, minutes, seconds, sep=":")
