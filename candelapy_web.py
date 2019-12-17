
from flask import Flask
app = Flask(__name__)
import pygatt
import sys
from flask import request

adapter = pygatt.GATTToolBackend()

@app.route("/yeelight")
def on():

 adapter.start()

 intensity = int(request.args.get('intensity'))

 try:
  print("Trying to connect...")
  device = adapter.connect("F8:24:41:C2:FC:3F")

  if intensity > 0:
   device.char_write_handle(0x001f, bytearray([0x43, 0x40, 0x01])) #on
   device.char_write_handle(0x001f, bytearray([0x43, 0x42, intensity])) #intensiy
  else:
   device.char_write_handle(0x001f, bytearray([0x43, 0x40, 0x02])) #off

 except:
  print("Connection Error")

 adapter.stop()

 return "OK"

if __name__ == "__main__":
 app.run(host='0.0.0.0',debug=True)