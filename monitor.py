import serial
import urllib
import sys
import time

port = serial.Serial("/dev/ttyUSB0", 9600)

while True:
  with open("/var/opt/dylos/data.txt", "a") as f:
    samples = port.readline().split(',')
    small = int(samples[0])
    large = int(samples[1])
    aqi = (small - large)/100
    print "large = %d, small = %d, aqi = %d" % (large, small, aqi)
    f.write("%s,%d,%d\n" % (time.ctime(), small, large))
    sys.stdout.flush()
    urllib.urlopen("http://data.sparkfun.com/input/roaznYON3AfrOG3wV391?private_key=jkRy0g6wn2hzE6KnGKvN&large=%d&small=%d&aqi=%d" % (large, small, aqi)).read()
