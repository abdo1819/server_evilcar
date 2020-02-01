from socket import gethostbyname
def write_request(content_str
                  ,host
                  ,method="GET"
                  ,path="/"
                  ,content_type="application/json"
                  ,new_line=r"\r\n"
                  ,http_version="HTTP/1.1"
                  ):
    return method+" "+path+" "+http_version+new_line \
           +"Host: "+host+new_line \
           +"Content-Type: "+content_type+new_line \
           +"Content-Length: "+str(len(content_str))+new_line*2 \
           +content_str \
           +new_line 
def do_ip_lookup(domain):
    return gethostbyname(domain)

print(do_ip_lookup("evilcar.herokuapp.com"))