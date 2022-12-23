import os
import time


dirs = input("Enter the directory names to create: ")
location = input("Enter the location to create folder/(s) #(eg: C:/Users/Public/Documents/): ")
names = dirs.split(' ')

path = os.path.join(location, )
print("Checking Inputs...")
time.sleep(1)

try:
    for i in range(len(names)):
        path = os.path.join(location, names[i])
        os.mkdir(path)
        print('Folder {} is created'.format(i))
        time.sleep(1)
        print()
        print()
except OSError as error:
    print(error, 'Try Again')
else:
    print()
    print("All folder/(s) Created Successfully")



