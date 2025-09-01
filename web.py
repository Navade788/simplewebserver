from http.server import HTTPServer, BaseHTTPRequestHandler
content = '''
<!doctype html>
<html>
<head>
<title>Web Server</title>
</head>
<body>
<h1>TCP/IP Protocol</h1>

<table border="1" align="left cellpadding="10" cellspacing="0" bgcolor="lightblue">
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
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET request received...")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode("utf-8"))

print("This is my webserver, running at http://localhost:5000/")
server_address = ('', 5000)
httpd = HTTPServer(server_address, MyServer)
httpd.serve_forever()