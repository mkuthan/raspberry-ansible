# Raspberry PI Configuration

My private Raspberry Pi installation at home.

* Do not touch anything by hand, use Ansible.
* If something is hard to automate, document it at least.

## Ansible playbooks

Install 3rd party roles:

```
ansible-galaxy install -r requirements.yml
```

### Packages playbook

Configure APT repositories, install packages and upgrade system:

```
ansible-playbook packages.yml
```

### Pimp my Pi playbooks

Various playbooks to improve initial Raspberry Pi setup:

```
ansible-playbook pimpmypi.yml
```

Roles:

* common - missing pieces of vanilla Raspberry distribution
* grafana - monitoring with [Grafana Cloud](https://grafana.com/products/cloud/) (free tier)
* hdidle - spin-down disks, see [Github](https://github.com/adelolmo/hd-idle)
* log2ram - move logs into RAM, see [Github](https://github.com/azlux/log2ram)
* posfix - forward mails to real account (instead of Exim4)
* smartmontools - monitor hard drives

### Other playbooks

* adguard - privacy all the time
* backup - to backup or not to backup, that’s no question
* kodi - the best smart tv ever
* raspotify, shairport - make my retired HiFi great again
* samba - my family disk for files and automated backups
* transmission - the lightest BT daemon

## Manual setup

### Hardware

* Raspberry Pi 4 model B, 4GB
* HiFiBerry DAC+
* RAIDON GR3660-B3

### Install image

The repository is tested against Raspberry Pi OS Lite 32 bit.

1. Install image on SD card
1. Append `ip=«IP»` into `cmdline.txt`
1. Enable ssh `touch ssh`

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
