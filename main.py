import paramiko

def func_do_ssh_Stuff(address, usr, pwd, command):
    try:
        print("ssh " + usr + "@" + address + ", running : " +
              command)
        client = paramiko.SSHClient()           # paramiko client object
        client.load_system_host_keys()  # this loads any local ssh keys
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        client.connect(address, username=usr, password=pwd)         # connecting to server
        _, ss_stdout, ss_stderr = client.exec_command(command)      # executing command on server and return result
        r_out, r_err = ss_stdout.readlines(), ss_stderr.read()  # ss_stderr for error and ss_stdout for result of command
        if len(r_err) > 5:
            print(r_err)
        else:
            print(r_out)
        client.close()          # closing connection
    except IOError:             # if host/server is not up or for any other issue
        print(".. host " + address + " is not up")
        return "host not up", "host not up"

ip_address = "192.168.10.177"
user = "ashfaq"
pwd = "ashfaq"
command = "date"

func_do_ssh_Stuff(ip_address,user,pwd,command)

