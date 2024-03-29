#!/home/jackr/anaconda/envs/QML36/bin/python
import os
import sys
import psutil
#sys.path.append('~/CasMonitorQt5/')
import subprocess
import time

def isPIDRunning(pid):
    print('Checking if PID {} is running...'.format(pid))
    try:
        if psutil.pid_exists(int(pid)):
            print ('PID {} already exists!'.format(pid))
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

def checkPIDFile(pidfile):
    if os.path.isfile(pidfile):
        pid = open(pidfile, 'r').read()
        #print(pid)
        if isPIDRunning(pid):
            return True, int(pid)
        else:
            return False, None
    else:
        return False, None


if __name__ == '__main__':
    #Check if SampleMonitor is running...
    pid = str(os.getpid())
    pidfile = '/tmp/SampleMonitor.pid'
    #Saving gui and ctrl subprocess PIDs to also kill if running
    guipidf = '/tmp/SampleMonitor_GUI.pid'
    ctrlpidf = '/tmp/SampleMonitor_Controller.pid'
#     pidfile = 'F:/Torres/CasMonitorQt5/SampleMonitor.pid'
    #If it is running, warn the user and do not start the app
    #Could also terminate the active processes and give the user an option to do that
    runRunning, runPID = checkPIDFile(pidfile)
    guiRunning, guiPID = checkPIDFile(guipidf)
    ctrlRunning, ctrlPID = checkPIDFile(ctrlpidf)
    guiOnly = False
    input_empty = True
    if ctrlRunning:
        while input_empty:
            restartGUI = input('Controller is still running. Do you wish to restart GUI and keep controller active? yes|no    ')
            if restartGUI == "yes" or restartGUI == "y":
                try:
                    guiOnly = True
                    if runPID is not None:
                        psutil.Process(runPID).terminate()
                    if guiPID is not None:
                        psutil.Process(guiPID).terminate()
                except Exception as e:
                    print(e)
                break
            elif restartGUI == "no" or restartGUI == "n":
                input_empty = False
                print('SampleMonitor with PID {} (runApp),{} (controlNQ),{} (setupGUI) is still running. Use task manager to terminate runApp.py, controlNQ.py, and setupGUI.py processes'.format(runPID, ctrlPID, guiPID))
                while True:
                    terminate = input("Do you wish to terminate all existing processes? yes|no    ")
                    if terminate == "yes" or terminate == "y":
                        try:
                            if runPID is not None:
                                psutil.Process(runPID).terminate()
                            if guiPID is not None:
                                psutil.Process(guiPID).terminate()
                            if ctrlPID is not None:
                                psutil.Process(ctrlPID).terminate()
                        except Exception as e:
                            print(e)
                        break
                    elif terminate == "no" or terminate == "n":
                        print('Goodbye!')
                        time.sleep(5)
                        sys.exit()
                    
    elif runRunning or guiRunning or ctrlRunning:
        print('SampleMonitor with PID {} (runApp),{} (controlNQ),{} (setupGUI) is still running. Use task manager to terminate runApp.py, controlNQ.py, and setupGUI.py processes'.format(runPID, ctrlPID, guiPID))
        while True:
            terminate = input("Do you wish to terminate all existing processes? yes|no    ")
            if terminate == "yes" or terminate == "y":
                try:
                    if runPID is not None:
                        psutil.Process(runPID).terminate()
                    if guiPID is not None:
                        psutil.Process(guiPID).terminate()
                    if ctrlPID is not None:
                        psutil.Process(ctrlPID).terminate()
                except Exception as e:
                    print(e)
                break
            elif terminate == "no" or terminate == "n":
                print('Goodbye!')
                time.sleep(5)
                sys.exit()
        
    open(pidfile, 'w').write(pid)
    
    try:
        processes = []
        if not guiOnly:
            ctrl = subprocess.Popen(['python3', 'prepbot/controlNQ.py'])
            # ctrl = subprocess.Popen([sys.executable, 'prepbot/controlNQ.py'])
            open(ctrlpidf,'w').write(str(ctrl.pid))
            processes.append(ctrl)
            time.sleep(1)
        gui = subprocess.Popen(['python3', 'setupGUI.py'])
        # gui = subprocess.Popen([sys.executable, 'setupGUI.py'])
        open(guipidf,'w').write(str(gui.pid))
        processes.append(gui)
        
        while True:
            if any(p.poll() == 0 for p in processes):
                break
            time.sleep(10)
            #for p in processes:
            #    print(p)
            #    print(p.poll())
            continue
            
        for p in processes:
            p.terminate()
            print('Process poll: {}'.format(p.poll()))
            
    finally:
        os.unlink(pidfile)
        os.unlink(guipidf)
        os.unlink(ctrlpidf)
