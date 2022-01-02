import time
from colors import *

def stalin_sort(data, drawData, timeTick):
    size = len(data)
    try:
        for i in range(size):
            if data[i] < data[i+1]:
                drawData(data, [YELLOW if x == i else BLUE for x in range(len(data))] )
                time.sleep(timeTick)
                continue
            else:
                drawData(data, [RED if x == i else BLUE for x in range(len(data))] )
                data.pop(i)
    except IndexError:
        pass
    
    drawData(data, [BLUE for x in range(len(data))])


