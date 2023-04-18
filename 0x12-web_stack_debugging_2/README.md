# 0x12. Web stack debugging #2

#### Concepts

For this project, we expect you to look at this concept:

* <a href="https://intranet.alxswe.com/concepts/68">Web stack debugging</a>

## Requirements

### General
* All your files will be interpreted on Ubuntu 14.04 LTS
* All your files should end with a new line
* A README.md file at the root of the folder of the project is mandatory
* All your Bash script files must be executable
* Your Bash scripts must pass Shellcheck without any error
* Your Bash scripts must run without error
* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all your Bash scripts should be a comment explaining what is the script doing

## Tasks

#### 0. Run software as another user

The script first checks if exactly one argument was provided using
the ```$#``` variable, which stores the number of arguments passed to the script.
If the number of arguments is not ```1```, it prints a usage message and exits
with a non-zero status code.

The sudo command is then used to run the whoami command as the specified
user using the ```-u``` option. This allows us to run a command as another user,
in this case, the one passed as an argument. The output of the whoami
command will then show the current user's username.

#### 1. Run Nginx as Nginx

First, the ownership of Nginx directories (```/var/www/html```, ```/var/log/nginx```,
```/var/lib/nginx```, and ```/etc/nginx```) is changed to the nginx user using chown.
This ensures that the nginx user has the necessary permissions to read
and write to these directories.

Then, the script modifies the Nginx configuration to run as the nginx user
and listen on port 8080. This is achieved by using the sed command to
replace the user and listen directives in the nginx.conf and default
configuration files, respectively.

Finally, the script tests the modified Nginx configuration using nginx -t
and reloads the Nginx service using systemctl reload nginx.

#### 2. 7 lines or less

The ```chown``` command  uses brace expansion {} to group multiple directories and change
ownership in a single line.

The ```sed``` commands remove semicolons and use newlines instead to separate
commands, and the ```systemctl``` command is used instead of ```nginx -t &&
systemctl reload nginx```.

This script is 7 lines long (not counting the shebang and the newline
at the end) and meets all the requirements.