# 0x09. Web infrastructure design

**Concepts**

For this project, we expect you to look at these concepts:

* <a href="https://intranet.alxswe.com/concepts/12">DNS</a>
* <a href="https://intranet.alxswe.com/concepts/13">Monitoring</a>
* <a href="https://intranet.alxswe.com/concepts/13">Web Server</a>
* <a href="https://intranet.alxswe.com/concepts/33">Network basics</a>
* <a href="https://intranet.alxswe.com/concepts/46">Load balancer</a>
* <a href="https://intranet.alxswe.com/concepts/67">Server</a>

# Resources

Read or watch:

* Network basics concept page
* Server concept page
* Web server concept page
* DNS concept page
* Load balancer concept page
* Monitoring concept page
* <a href="https://intranet.alxswe.com/rltoken/n3CdS3EA5l5psDDKbEhApA">What is a database</a>
* <a href="https://intranet.alxswe.com/rltoken/0as4wDlFqyhLhf0f_gedcw">What’s the difference between a web server and an app server?</a>
* <a href="https://intranet.alxswe.com/rltoken/Pl3UoEfAO7K_jUKRLMmnAQ">DNS record types</a>
* <a href="https://intranet.alxswe.com/rltoken/uxpx2YhXs10TFLIDg78chA">Single point of failure</a>
* <a href="https://intranet.alxswe.com/rltoken/4ansLu2gtHnoFrNThqyObA">How to avoid downtime when deploying new code</a>
* <a href="https://intranet.alxswe.com/rltoken/TAJeVYy9U9iLaEDd6XkbRA">High availability cluster (active-active/active-passive)</a>
* <a href="https://intranet.alxswe.com/rltoken/c0zs2MxrmxFLsCPOizxq6g">What is HTTPS</a>
* <a href="https://intranet.alxswe.com/rltoken/j6idMcUTyNEDj1oYDQFmUw">What is a firewall</a>

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

* You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects
* You must be able to explain what each component is doing
* You must be able to explain system redundancy
* Know all the mentioned acronyms: LAMP, SPOF, QPS

## Requirements

### General

* A README.md file, at the root of the folder of the project, is mandatory
* For each task, once you are done whiteboarding (on a whiteboard, piece of paper or software or your choice), take a picture/screenshot of your diagram
* This project will be manually reviewed:
* As each task is completed, the name of that task will turn green
* Upload a screenshot, showing that you completed the required levels, to any image hosting service (I personally use imgur but feel free to use anything you want).
* For the following tasks, insert the link from of your screenshot into the answer file
* After pushing your answer file to GitHub, insert the GitHub file link into the URL box
* You will also have to whiteboard each task in front of a mentor, staff or student - no computer or notes will be allowed during the whiteboarding session
* Focus on what you are being asked:
* Cover what the requirements mention, we will explore details in a later project
* Keep in mind that you will have 30 minutes to perform the exercise, you will get points for what is asked in requirements
* Similarly in a job interview, you should answer what the interviewer asked for, be careful about being too verbose - always ask the interviewer if going into details is necessary - speaking too much can play against you
* In this project, again, avoid going in details if not asked

### 0. Simple web stack

A server is a computer or software program that provides a service or functionality to other computers or devices on a network. In the context of the internet, a server typically refers to a computer or software program that provides services such as serving web pages, email, file sharing, or database access to other computers or devices.

A domain name is a unique name that identifies a website on the internet. The role of a domain name is to provide a memorable and easy-to-use address for a website so that users can access it without having to remember its IP address (which is a numerical address that identifies a specific computer or device on a network).

The "www" in "www.foobar.com" is not a DNS record but rather a subdomain. A subdomain is a subset of a larger domain that is used to organize and distinguish different services or sections of a website. The DNS record associated with the subdomain "www" is typically an "A" record, which maps the subdomain to an IP address.

The role of a web server is to serve web pages to clients (such as web browsers) that request them over the internet. A web server receives requests from clients, retrieves the appropriate web page files, and sends them back to the client over the internet. The web server is responsible for processing HTTP requests and responses, and for handling the communication between the client and the web application.

An application server is a software program that provides additional functionality beyond what a web server can provide. An application server typically provides services such as transaction management, security, database access, and other functions required by web applications. Application servers can be used to host web applications that require more advanced functionality than what a simple web server can provide.

A database is a software program that stores and manages structured data. The role of a database is to provide an efficient and reliable way to store and retrieve data, and to support the functionality of web applications that require data storage and retrieval. Web applications typically interact with databases through an application programming interface (API) that provides a way for the application to communicate with the database and perform operations such as querying, inserting, updating, and deleting data.


To design a one server web infrastructure that hosts the website reachable via www.foobar.com, let's start by understanding the user's request.

* When a user types in www.foobar.com into their web browser and hits enter, the request is sent to the DNS (Domain Name System) server to resolve the IP address associated with www.foobar.com.
* Once the IP address is resolved, the user's computer sends a request to the IP address to access the website.

**Specifics about this infrastructure**

* In our infrastructure, we will have one server that will host the web server (Nginx), application server, and the MySQL database.
* We will install the LAMP stack (Linux, Apache, MySQL, PHP) on the server.
* The domain name foobar.com will be configured with a www record that points to our server's IP address 8.8.8.8.
* This will allow users to access the website using the URL www.foobar.com.
* The web server (Nginx) will receive the user's request and serve static files such as HTML, CSS, and images.
* It will also route dynamic requests to the application server. The application server will handle dynamic requests and generate responses based on the user's request. It will communicate with the MySQL database to fetch and store data.
* The MySQL database will store the website's data such as user information, blog posts, and other content.
* The server will use HTTP (Hypertext Transfer Protocol) to communicate with the user's computer requesting the website.
* The web server and application server will generate HTTP responses that will be sent back to the user's computer.

**Issues about this infrastructure**

However, this infrastructure has some issues.

* It is a single point of failure (SPOF), which means that if the server goes down, the website will not be accessible.

* There will be downtime when maintenance is needed, such as deploying new code, as the web server needs to be restarted.
* The infrastructure cannot scale if there is too much incoming traffic, as the single server will not be able to handle the load.

**How to address the issues**

* To address these issues, we can implement load balancing by adding more servers to the infrastructure.
* We can also implement a CDN (Content Delivery Network) to distribute content globally and reduce the load on the server.
* Additionally, we can use containerization technology like Docker to simplify deployment and management of the infrastructure.

### 1. Distributed web infrastructure

Here is a design for a three-server web infrastructure that hosts the website www.foobar.com:

Load Balancer Server:

* This server will act as a load balancer, distributing incoming traffic between the two application servers.
* It will run HAproxy, a software load balancer that provides high availability, load balancing, and proxying for TCP and HTTP-based applications.

Application Server 1:

* This server will host the first instance of the application.
* It will run Nginx as the web server, serving static files and passing dynamic requests to the application server.
* The server will run the application code base and connect to the MySQL database to retrieve and store data.

Application Server 2:

* This server will host the second instance of the application.
* It will run Nginx as the web server, serving static files and passing dynamic requests to the application server.
* The server will run the application code base and connect to the MySQL database to retrieve and store data.

Database Server:

* This server will host the MySQL database, where the application data will be stored.
* It will be configured as a Primary-Replica cluster, where the primary node will handle all the writes, and the replica node will handle the reads.
* The application servers will connect to the primary node to write data and connect to the replica node to read data.

**Some specifics about this infrastructure:**

* We are adding two application servers and a load balancer to handle more incoming traffic and provide high availability for the application.
* The load balancer will be configured with a round-robin distribution algorithm, where it will evenly distribute incoming requests to both application servers.
* The load balancer will be set up to enable an Active-Active setup, where both application servers are actively serving requests simultaneously.
* The database primary node will handle all the writes, and the replica node will handle the reads, providing a fault-tolerant setup and reducing the read traffic on the primary node.
* The primary node and the replica node will have different roles in the application. The primary node will handle all the writes, ensuring data consistency, while the replica node will handle the reads, providing faster access to data.

**The issues with this infrastructure:**

* The load balancer server can be a single point of failure (SPOF). If it fails, the application servers will not be able to handle incoming traffic.
* The infrastructure does not have any firewall or HTTPS configured, leaving it vulnerable to security issues.
* There is no monitoring set up to track the health of the servers and services, making it difficult to identify and troubleshoot issues.

### 2. Secured and monitored web infrastructure

Design for a three-server web infrastructure that hosts the website www.foobar.com:

Load Balancer Server:

* This server will act as a load balancer, distributing incoming traffic between the two application servers.
* It will run HAproxy, a software load balancer that provides high availability, load balancing, and proxying for TCP and HTTP-based applications.

Application Server 1:

* This server will host the first instance of the application.
* It will run Nginx as the web server, serving static files and passing dynamic requests to the application server.
* The server will run the application code base and connect to the MySQL database to retrieve and store data.

Application Server 2:

* This server will host the second instance of the application.
* It will run Nginx as the web server, serving static files and passing dynamic requests to the application server.
* The server will run the application code base and connect to the MySQL database to retrieve and store data.

Database Server:

* This server will host the MySQL database, where the application data will be stored.
* It will be configured as a Primary-Replica cluster, where the primary node will handle all the writes, and the replica node will handle the reads.
* The application servers will connect to the primary node to write data and connect to the replica node to read data.

**Some specifics about this infrastructure:**

* We are adding two application servers and a load balancer to handle more incoming traffic and provide high availability for the application.
* The load balancer will be configured with a round-robin distribution algorithm, where it will evenly distribute incoming requests to both application servers.
* The load balancer will be set up to enable an Active-Active setup, where both application servers are actively serving requests simultaneously.
* The database primary node will handle all the writes, and the replica node will handle the reads, providing a fault-tolerant setup and reducing the read traffic on the primary node.
* The primary node and the replica node will have different roles in the application. The primary node will handle all the writes, ensuring data consistency, while the replica node will handle the reads, providing faster access to data.

**The issues with this infrastructure:**

* The load balancer server can be a single point of failure (SPOF). If it fails, the application servers will not be able to handle incoming traffic.
* The infrastructure does not have any firewall or HTTPS configured, leaving it vulnerable to security issues.
* There is no monitoring set up to track the health of the servers and services, making it difficult to identify and troubleshoot issues.

### 3. Scale up

Specifics of the infrastructure we're describing.

* Firstly, let's distinguish between an application server and a web server. A web server is responsible for serving static content such as HTML, CSS, and images.
* It's the first point of contact for a user's request, and it returns the content that matches the user's request. In contrast, an application server handles dynamic content and business logic.
* It interacts with a database and processes data to create dynamic content that is then served by the web server.

Now let's move on to the requirements listed.

Adding a server:

* You're adding a server to distribute the workload and ensure high availability.
* When you have multiple servers, you can distribute the load across them to avoid overburdening any one server.
* Additionally, if one server goes down, the others can continue to handle traffic, ensuring the availability of your service.

Adding a load balancer:

* A load balancer distributes incoming requests across multiple servers to ensure that no one server is overwhelmed.
* It can also provide redundancy by automatically redirecting traffic to healthy servers if one server goes down.
* Using HAProxy to configure a cluster provides even greater fault tolerance, as multiple load balancers can work together to ensure that traffic is always directed to healthy servers.

Splitting components onto separate servers:

* This is a best practice in infrastructure design as it allows you to scale each component independently. For example, if your web server is overloaded but your application server is not, you can simply add more web servers to handle the increased load.
* Similarly, if your database is struggling, you can scale it up or out to improve its performance.
* Separating the components also reduces the risk of interference between them and can improve security by ensuring that each component only has access to the resources it needs.

Overall, this infrastructure design improves performance, scalability, and fault tolerance. It also allows you to isolate and scale each component independently, making it easier to manage your infrastructure as your service grows.

