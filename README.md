# candelapy
*candelapy* is a simple python script that lets you control your Yeelight Candela Ambient Lamp YLFW01YL over BLE.

Requirements
------------

*candelapy* is based on *pygatt*

    $ sudo pip3 install pygatt
    $ sudo pip3 install pexpect
    
If you want to use the webserver version you'll need *Flask*

    $ sudo pip3 install flask
    
Installation
------------

    $ git clone git://github.com/ollan/candelapy.git
    
Usage
-----

To control your lamps(s) you need to find out their MAC adress. Usually they are listed as *yeelight_ms*.

    $ sudo hcitool lescan

Afterwards you can use the script as follows:

    $ python3 candelapy.py [mac adress] [intensity 0-100]
    
Start of webserver:
    
    $ nohup python3 candelapy_web.py &
    
The webserver versions can be accessed via Port 5000:

    http://[IP]:5000/yeelight?intensity=[intensity 0-100]
    
Examples
--------

To turn on the lamp to full intensity:

    $ python3 candelapy.py F8:24:41:C0:71:A7 100
    
And to turn off the lamp:

    $ python3 candelapy.py F8:24:41:C0:71:A7 0
    
Simple local integration into Home Assistant:

    switch:
      platform: command_line
       switches:
        yeelight_candela:
          friendly_name: 'Yeelight Candela'
          command_on: 'python /home/pi/candelapy.py F8:24:41:C0:71:A7 100'
          command_off: 'python /home/pi/candelapy.py F8:24:41:C0:71:A7 0'
          
Simple remote integration into Home Assistant:

    switch:
      platform: command_line
      switches:
        yeelight_candela:
          friendly_name: 'Yeelight Candela'
          command_on: 'wget http://192.168.1.108:5000/yeelight?intensity=100'
          command_off: 'wget http://192.168.1.108:5000/yeelight?intensity=0'

Open Tasks
----------
- Activating the Fire-Mode and controlling several lamps (BLE mash) at once is not yet implemented in the official app, thus not reverse engineerable.
