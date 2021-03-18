# Raspberry PI Configuration

My private Raspberry Pi infrastructure as a code. Do not touch anything by hand, use Ansible.

## Install image

Download Raspberry Pi OS Lite image from https://www.raspberrypi.org/software/operating-systems/.

Copy the image to the SD card:

```
sudo dd bs=1m if=path_of_your_image.img of=/dev/rdiskN
```

Configure WiFi:

```
cat <<EOT >> wpa_supplicant.conf
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=«ISO-3166-1_two-letter_country_code»

network={
    ssid="«SSID»"
    psk="«PSK»"
    key_mgmt=WPA-PSK
}
EOT
```

Enable WiFi:

```
touch wifi
```

Boot Raspberry Pi

## Configuring SSH

Generate key:

```
ssh-keygen -f pi_rsa
```

Configure client:

```
cat <<EOT >> ~/.ssh/config
Host pi
	HostName «IP»
	User pi
	IdentityFile ~/.ssh/pi_rsa
EOT
```

Copy key to Raspberry Pi:

```
ssh-copy-id -i ~/.ssh/pi_rsa.pub pi
```
## Install and configure everything else

```
ansible-playbook pi.yml
```

That's all folks :)