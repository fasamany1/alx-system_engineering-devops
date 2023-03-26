# 0x0B. SSH

## Background Context

Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away. Like level 2 of the application process, you will connect using ssh. But contrary to level 2, you will not connect using a password but an RSA key. We’ve configured your server with the public key you created in the first task of a previous project shared in your intranet profile.

You can access your server information in the my servers section of the intranet, each line with contains the IP and username you should use to connect via ssh.

Note: Your server is configured with an Ubuntu 20.04 LTS environment.

## ResourcesResources
**Read or watch:**

* <a href="https://intranet.alxswe.com/rltoken/dkgW9lKiBRiUZHfq0MDJuw">What is a (physical) server - text</a>
* <a href="https://intranet.alxswe.com/rltoken/AxFcTdcXUCsrVp01X_EbFA">What is a (physical) server - video</a>
* <a href="https://intranet.alxswe.com/rltoken/ux0eM1QU9reNyG45b0erAQ">SSH essentials</a>
* <a href="https://intranet.alxswe.com/rltoken/Rc9FpSy4ZaQWPlcWLinbNw">SSH Config File</a>
* <a href="https://intranet.alxswe.com/rltoken/tOcxk5mtkedBM0WxyDZxTw">Public Key Authentication for SSH</a>
* <a href="https://intranet.alxswe.com/rltoken/j0atjRrVfZ6F810qmPfAzA">How Secure Shell Works</a>
* <a href="https://intranet.alxswe.com/rltoken/FKqd8CjxExmpWGu6xGavKw">SSH Crash Course</a> (Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)

**For reference:**

* <a href="https://intranet.alxswe.com/rltoken/JB-Vi4dR3q6nF4MBhsn8kQ">Understanding the SSH Encryption and Connection Process</a>
* <a href="https://intranet.alxswe.com/rltoken/SpiYWE79Yfr_vWDg42dzCw">Secure Shell Wiki</a>
* <a href="https://intranet.alxswe.com/rltoken/f2O0OQq9tch2MYeNAzkg5w">IETF RFC 4251 (Description of the SSH Protocol)</a>
* <a href="https://intranet.alxswe.com/rltoken/gd1W1UvB0KeJVWwM8BLvhA">Internet Engineering Task Force</a>
* <a href="https://intranet.alxswe.com/rltoken/jb-IrnQnUh-PsEDlbAU0Kw">Request for Comments</a>

**man or help:**

* ssh
* ssh-keygen
* env

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

* What is a server
* Where servers usually live
* What is SSH
* How to create an SSH RSA key pair
* How to connect to a remote host using an SSH RSA key pair
* The advantage of using #!/usr/bin/env bash instead of /bin/bash

## Requirements

### General

* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 20.04 LTS
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all your Bash scripts should be a comment explaining what is the script doing

