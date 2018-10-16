import time
import sys, signal
def signal_handler(signal, frame):
    print("\neeee")


start_time = time.time() 
last_time = start_time
lap_num = 0

try:
  while True:
    
    lap_time = round(time.time() - last_time, 2)
    total_time = round(time.time() - start_time, 2)
    print(f"Lap {lap_num} -> {lap_time} secs since last Lap -> {total_time} secs in total")
    lap_num += 1
    last_time = time.time()

except KeyboardInterrupt:
  print('\nbye!')