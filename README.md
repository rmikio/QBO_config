# QBO_config

## Application  to configure the QBO system

Clone *QBO_config* repository into **/home/pi/Documents/** directory.

Update **QBOtalk.py** and **PiFaceFast.py** from PiFace repository.

## System deamon
Edit QBOautoStart.service:

`sudo nano /lib/systemd/system/QBOautoStart.service`

Add in the following text:

>[Unit]
>
>Description=My Sample Service
>
>After=multi-user.target
>
>
>[Service]
>
>Type=oneshot
>
>RemainAfterExit=yes
>
>ExecStart=/usr/bin/python /home/pi/Documents/deamonsScripts/autoStart.py
>
>ExecStop=/usr/bin/python /home/pi/Documents/deamonsScripts/autoStop.py
>
>
>[Install]
>
>WantedBy=multi-user.target

You should save and exit the nano editor.

Now the unit file has been defined we can tell systemd to start it during the boot sequence:

`sudo systemctl daemon-reload`

`sudo systemctl enable QBOautoStart.service`

Reboot the Pi and QBOautoStart service should run:

`sudo reboot`
