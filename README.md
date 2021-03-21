# Raspberry PI Configuration

My private Raspberry Pi installation at home.

* Do not touch anything by hand, use Ansible.
* If something is hard to automate, document it at least.

## Ansible playbooks

Install 3rd party roles:

```
ansible-galaxy install -r requirements.yml
```

Install everything:

```
ansible-playbook pi.yml
```

Available playbooks:

* common - missing pieces of vanilla distribution
* packages - my linux toolbox
* adguard - privacy all the time
* raspotify - make my retired HiFi great again
* kodi - the best smart tv ever
* transmission - the lightest BT daemon
* samba - network attached storage

## Manual setup

### Install image

Download Raspberry Pi OS Lite image from https://www.raspberrypi.org/software/operating-systems/.

Copy the image to the SD card:

```
sudo dd bs=1m if=path_of_your_image.img of=/dev/rdiskN
```

Encrypt WiFi password:

```
wpa_passphrase «SSID»
```

Configure WiFi:

```
cat <<EOT >> wpa_supplicant.conf
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=«ISO-3166-1_two-letter_country_code»

network={
    ssid=«SSID»
    psk=«encrypted_wpa_passphrase»
}
EOT
```

Enable WiFi:

```
touch wifi
```

Boot Raspberry Pi

### Configuring SSH

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

### Install Docker

```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```
