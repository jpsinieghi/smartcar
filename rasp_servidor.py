class ThreadServer(object):

    def server_thread(host, port):
        server = SocketServer.TCPServer((host, port), VideoStreamHandler)
        server.serve_forever()

    video_thread = threading.Thread(target=server_thread('192.168.1.100', 8000))
    video_thread.start()

if __name__ == '__main__':
    ThreadServer()
