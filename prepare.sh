sudo modprobe esd_usb2
sudo ip link set can0 down
sudo ip link set can0 up type can bitrate 500000
sudo ip link set can0 txqueuelen 20


