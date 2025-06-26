# QuecPython WebSocket Server

A simple WebSocket server implementation for QuecPython modules, with optional client example and browser testing instructions.

## Features

- WebSocket server for QuecPython devices
- Echoes received messages back to the client
- Supports multiple clients using threads
- Example WebSocket client (for internal testing)
- Sample HTML for browser-based testing

## Getting Started

### Prerequisites

- QuecPython-compatible module (e.g., EC200U, EC600N, etc.): https://developer.quectel.com/en/pro-cat-page/cellular-modules
- QuecPython firmware you can find here: https://developer.quectel.com/en/resource-download?cid=5

### Installation

1. Upload all project files to your module:
    - `_main.py`
    - `ws_server.py`
    - `websocket_handshake.py`

2. Run `_main.py` script.

### Usage

1. Power on your module and ensure `_main.py` runs automatically.
2. The server will start on port `8080` by default.
3. To stop the server, type `q` in the module’s serial console and press Enter.

#### Testing with a Browser

You can test the server using a browser. Save the following HTML as `test.html` and open it in your browser:

```html
<!DOCTYPE html>
<html>
  <body>
    <h2>WebSocket Test</h2>
    <script>
      const ws = new WebSocket("ws://<MODULE_IP>:<PORT>");
      ws.onopen = () => {
        console.log("Connected");
        ws.send("Hello from browser!");
      };
      ws.onmessage = e => {
        console.log("Received:", e.data);
        alert("Received: " + e.data);
      };
      ws.onerror = e => {
        console.error("WebSocket error:", e);
      };
      ws.onclose = () => {
        console.log("WebSocket closed");
      };
    </script>
  </body>
</html>
```

Replace `<MODULE_IP>` with your module's IP address and `<PORT>` with the port number you will use.

#### Internal Client Example

You can also use the built-in WebSocket client for internal testing. Uncomment the client section in `_main.py` to enable it.
More on QuecPython websocket client here: https://developer.quectel.com/doc/quecpython/API_reference/en/networklib/uwebsocket.html

## File Overview

- [`_main.py`](./_main.py): Main entry point, starts the server and handles shutdown.
- [`ws_server.py`](./ws_server.py): WebSocket server implementation.
- [`websocket_handshake.py`](./websocket_handshake.py): Handles WebSocket handshake logic.

## License

MIT License

---

**Note:** This project is intended for educational and testing purposes on QuecPython modules.