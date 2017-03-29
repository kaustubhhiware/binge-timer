import subprocess


def getLength(filename):
    result = subprocess.Popen(["ffprobe", filename],
                              stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return [x for x in result.stdout.readlines() if "Duration" in x]


def get_time(filename):
    # print getLength(loc)
    # ['  Duration: 00:46:21.06, start: 0.000000, bitrate: 1054 kb/s\n']
    details = getLength(loc)[0].split(',')
    # print details[0]#   Duration: 00:46:21.06
    d = details[0].split(': ')
    return d[1]


loc = raw_input("enter location : ")
print "length"
timer = get_time(loc)
print timer
t = timer.split(':')
print t[0]  # hours
print t[1]  # minutes
print t[2]  # seconds

#file_size = os.path.getsize(loc) //(1024*1024)
# print file_size
