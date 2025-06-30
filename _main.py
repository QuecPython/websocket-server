from usr.ws_server import WebSocketServer
import uwebsocket
import _thread
import utime


# Stop server when press 'q' and enter in the console.
def monitor_keyboard(server):
    while True:
        try:
            cmd = input()
            if cmd.strip().lower() == 'q':
                server.stop()
                break
        except:
            break

ws_server = WebSocketServer(port=8080)

_thread.start_new_thread(monitor_keyboard, (ws_server,))

# Start the WebSocket server in a new thread. Not necessary to use _thread.start_new_thread if you want to use html client.
#_thread.start_new_thread(ws_server.start, ())

ws_server.start()


######
# This is a WebSocket client example. Uncomment the following lines to run it.
######

'''
def recv(cli):
    while True:
        # Receive data in an infinite loop.
        recv_data = cli.recv()
        print("recv_data = {}".format(recv_data))
        if not recv_data:
            # The server or client closes the connection.
            print("cli close")
            client.close()
            break
        utime.sleep(0.1)

        
# Create a WebSocket client. "debug=True" indicates outputing logs. You need to customize the IP address, port or domain name.
client = uwebsocket.Client.connect('ws://127.0.0.1:8080', debug=False)

utime.sleep(4)
# Receive data in threads.
_thread.start_new_thread(recv, (client,))

# Send data.
client.send("this is a test msg")
'''
