from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 设置响应状态码为200（OK）
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        
        # 获取 x-forwarded-for 的值，如果不存在则返回空字符串
        ip = self.client_address[0]
        # x_forwarded_for = self.headers.get('x-forwarded-for', '无效IP')
        
        # 将获取到的值写入响应体
        self.wfile.write(ip.encode())
        return

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8888):
    # 绑定到所有可用的 IP 地址
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
