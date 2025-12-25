import time
import sys
import os
from colorama import Fore, Style, init

print("=====================================================")
init(autoreset=True)

def stopwatch_live():
    seconds = 0
    while True:
        try:
            # Format the time as H:M:S
            mins, secs = divmod(seconds, 60)
            hours, mins = divmod(mins, 60)
            timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
            
            # Print the time on the same line using carriage return
            sys.stdout.write(Fore.RED + Style.BRIGHT + timer+ '\r')
            sys.stdout.flush()
            
            time.sleep(1) # Pause for 1 second
            seconds += 1
        except KeyboardInterrupt:
            # Stop the stopwatch when Ctrl+C is pressed
            print(Fore.RED + "\nStopwatch stopped.")
            break

if __name__ == "__main__":
    print("Press Ctrl+C to stop the stopwatch.")
    stopwatch_live()
print("=====================================================")








