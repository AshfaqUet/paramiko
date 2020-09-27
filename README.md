# Paramiko
The basic function of this program is to connect to SSH server and run a command on server remotely

Preparing Server (Ubuntu in VirtualBox):

    1. Install Virtual Box

    2. Download and install ubuntu in virtual box / virtual machine
    
    3. Set the Manual IP address
    
        a. IP = 192.168.10.177
        
        b. Network = 255.255.255.0
        
        c. Gateway = 192.168.10.1 (route address)
        
        d. DNS = 8.8.8.8  ,  4.2.2.2
    
    4. Install SSH in server by using commands
        
        a. sudo apt update
        
        b. sudo apt install openssh-server
    
    5. Activate the SSH server in ubuntu
        
        a. Open terminal by Ctrl+Alt+T
        
        b. run command (sudo systemctl status ssh)
    
    6. Optional/Extra Commands for information
        
        a. Stop SSH services on ubuntu (sudo systemctl stop ssh)
        
        b. To start it again run (sudo systemctl start ssh)
        
        c. To disable the SSH service (sudo systemctl disable ssh)
        
        d. To enable it again type (sudo systemctl enable ssh)



Run code in pycharm:
    
    1. install requirements.txt packages in the environment
    
    2. IP of ubuntu / server = 192.168.10.177
    
    3. Username of ubuntu operating system in virtual machine = "ashfaq"
        
        A. How to know username of ubuntu
           
           a. Open terminal
           
           b. ashfaq@ashfaq-VirtualBox
           
           c. It can also be represent as ashfaq@192.168.10.177
           
           d. Here 'ashfaq' is the username
    
    4. Password of ubuntu = "ashfaq"
    
    5. Command = "ls"
        
        A. Commands may be different (ls,mkdir,date,df,free,and many more)
        
        B. Check this for more commands https://vitux.com/40-most-used-ubuntu-commands/
    
    6. Set there parameters and run program
    
    7. Program will first make connection with the server (client.connect(address, username=usr, password=pwd) )
    
    8. Run command on the server and return (_, ss_stdout, ss_stderr = client.exec_command(command) )
        
        A. error while running commands (ss_stderr)
        
        B. Output of commands (ss_stdout)
    
    9. Print Output or Error
