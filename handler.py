import sys
import subprocess
import time

def main():
    args = sys.argv

    if(len(args) != 2):
        return
    if(args[1].find("customfile:") != 0): 
        return
    pathStart = args[1].find(":")
    path = args[1][pathStart+1:]
    # print(path)
    while path.startswith("/"):
        path = path[1:]
    path = path.replace("%20", " ")
    path = path.replace("/", "\\")
    
    launchString = 'explorer "' + path + '"'
    print(launchString)
    subprocess.Popen(launchString)
    time.sleep(3)
    a = input("A:")



if __name__ == "__main__":
    main()