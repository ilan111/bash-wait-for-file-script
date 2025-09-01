from SshToServer import SshToServer

# Enter the relevant details
PEM_FILE_PATH = ""
SERVER_SIDE_SCRIPT_PATH = ""
HOST_IP = ""
HOST_USERNAME = ""

def main():
    my_ssh = SshToServer(PEM_FILE_PATH, HOST_IP, HOST_USERNAME)
    file_name = input("Please enter the name of the file: ")
    
    try:
        seconds = int(input("How many seconds to wait? "))
    except:
        print("Invalid input, please enter a valid number")
    
    remote_command = f"bash {SERVER_SIDE_SCRIPT_PATH} {file_name} {seconds}"

    try:
        stdout, stderr = my_ssh.runRemoteCommand(remote_command)
        server_output = int(stdout)
        if server_output >= 0 and server_output <= seconds:
            print(f"File {file_name} has arrived to the server after {seconds} seconds")
        
        elif server_output == -1:
            print("Timeout")

    except Exception as e:
        print(f"Error: {e}")





if __name__ == "__main__":
    main()