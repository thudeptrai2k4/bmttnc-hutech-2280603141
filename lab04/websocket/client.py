import tornado.ioloop
import tornado.websocket
import asyncio

class WebsocketClient:
    def __init__(self, io_loop):
        self.connection = None
        self.io_loop = io_loop

    async def connect_and_read(self):
        while True:
            try:
                print("Trying to connect...")
                self.connection = await tornado.websocket.websocket_connect("ws://localhost:8888/websocket/")
                print("Connected!")
                while True:
                    msg = await self.connection.read_message()
                    if msg is None:
                        print("Connection closed by server, reconnecting...")
                        break
                    print(f"Received word from server: {msg}")
            except Exception as e:
                print(f"Connection error: {e}")

            print("Retrying in 3 seconds...")
            await asyncio.sleep(3)

    def start(self):
        self.io_loop.add_callback(self.connect_and_read)

def main():
    io_loop = tornado.ioloop.IOLoop.current()
    client = WebsocketClient(io_loop)
    client.start()
    io_loop.start()

if __name__ == "__main__":
    main()
