#!/bin/sh

rdate -s time.fu-berlin.de
ln -s /npc/Europe/Athens /etc/localtime

cd /npc/
# TODO add your $password-hash here
sed -i -e 's/root::10933:0:99999:7:::/root:$password-hash:10933:0:99999:7:::/g' /etc/shadow
sed -i -e 's/root:x:0:0:root:\/root:\/bin\/sh/root:x:0:0:root:\/npc\/root-home:\/bin\/sh/g' /etc/passwd
mkdir -p /etc/dropbear
cp /npc/dropbear_ecdsa_host_key /etc/dropbear/

./dropbearmulti dropbear

#Bring wlan0 down
/sbin/ifconfig wlan0 down

# shittiest NTP client in history
now=$(wget http://192.168.2.1:8888 -O - -q -T 3)
if [ "test$now" != "test" ]; then
        date -s "$now"
fi
