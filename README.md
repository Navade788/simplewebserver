# EX01 Developing a Simple Webserver
## Date: 27/08/25

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
Developed by : S.Navadeep
Registration No : 212224230180
```
```
<!doctype html>
<html>
<head>
<title>My Web Server</title>
</head>
<body>
<h1>TCP/IP Protocol</h1>

<table border="1" align="left cellpadding="10" cellspacing="0" bgcolor="lightgreen">
  <tr>
    <th>S.no</th>
    <th>Layer</th>
    <th>Protocols</th>
  </tr>

  <tr>
    <td>1.</td>
    <td><b>Application Layer</b></td>
    <td>HTTP, HTTPS, FTP, SMTP, POP3, IMAP, DNS, Telnet, SSH</td>
  </tr>

  <tr>
    <td>2.</td>
    <td><b>Transport Layer</b></td>
    <td>TCP (Transmission Control Protocol), UDP (User Datagram Protocol)</td>
  </tr>

  <tr>
    <td>3.</td>
    <td><b>Network Layer (Internet Layer in TCP/IP)</b></td>
    <td>IP (IPv4, IPv6), ICMP, IGMP, ARP, RARP</td>
  </tr>

  <tr>
    <td>4.</td>
    <td><b>Link Layer (Network Access Layer in TCP/IP)</b></td>
    <td>Ethernet</td>
  </tr>
</table>

</body>
</html>
```


## OUTPUT:

<img width="949" height="1127" alt="image" src="https://github.com/user-attachments/assets/0d05c170-4ef6-434d-9b6d-0f67df20ac98" />

<img width="1612" height="376" alt="image" src="https://github.com/user-attachments/assets/c2b2098f-6234-4e30-9524-7ed2e9730374" />

<img width="1919" height="1127" alt="image" src="https://github.com/user-attachments/assets/e27acbc0-1a4c-4f27-bbca-e8b204944e38" />




## RESULT:
The program for implementing simple webserver is executed successfully.
