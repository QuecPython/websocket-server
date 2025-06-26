import usocket as socket
import usr.websocket_handshake as websocket_helper
import utime
import _thread

class WebSocketServer:
    def __init__(self, port=80):
        self.port = port
        self.sock = None
        self.client_sock = None
        self.running = True
        print('websocket init')

    def _read_ws_frame(self, sock):
        hdr = sock.read(2)
        if not hdr:
            return None
        length = hdr[1] & 0x7F
        mask = sock.read(4)
        encoded = sock.read(length)
        decoded = bytes(b ^ mask[i % 4] for i, b in enumerate(encoded))
        return decoded

    def _send_ws_frame(self, sock, data):
        sock.write(b'\x81' + bytes([len(data)]) + data)

    def start(self):
        print('Starting WebSocket server...')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.TCP_CUSTOMIZE_PORT)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('0.0.0.0', self.port))
        self.sock.listen(5)  
        print("WebSocket server running on port", self.port)

        while self.running:
            try:
                cl, addr, port = self.sock.accept()
                print("Client connected:", addr)
                _thread.start_new_thread(self._handle_client, (cl,))
            except Exception as e:
                print("Accept error:", e)
                utime.sleep(0.1)

    def stop(self):
        print("Stopping WebSocket server...")
        self.running = False
        try:
            self.sock.close()  
            print("Socket closed.")
        except Exception as e:
            print("Socket close error:", e)

    def _handle_client(self, cl):
        try:
            cl.setblocking(True)
            websocket_helper.server_handshake(cl)
            print("Handshake OK")
            while True:
                msg = self._read_ws_frame(cl)
                if msg is None:
                    break
                print("Received:", msg)
                self._send_ws_frame(cl, msg)  # echo back
        except Exception as e:
            print("Client error:", e)
        finally:
            cl.close()
            print("Client disconnected.")
            