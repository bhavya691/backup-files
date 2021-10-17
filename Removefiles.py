import os
import shutil
import time

path = input('Enter the path: \t')
days = input('Enter number of days: \t')
days = time.time()
if os.path.exists(path):
    for root, subFols, files in os.walk(path):
        a = os.path.join(path,root)
        print(a)
        ctime = os.stat(a).st_ctime
        if ctime > days:
            if files:
                os.remove(a+'/'+files)
            elif subFols:
                shutil.rmtree(a)                
else:
    print('Not found')