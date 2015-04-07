import os
import sys

def step(path):
    for item in os.listdir(path):
        
        try:
            
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                print("dir found: %s" % item)
                step(item_path)

            else: 
                print(item_path)
                
        except Exception as err:
            continue

step(sys.argv[1])