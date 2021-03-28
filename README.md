# Raspberry PI Configuration

My private Raspberry Pi installation at home.

* Do not touch anything by hand, use Ansible.
* If something is hard to automate, document it at least.

## Ansible playbooks

Install 3rd party roles:

```
ansible-galaxy install -r requirements.yml
```

Install playbook:

```
ansible-playbook «playbook»
```

Available playbooks:

* common - missing pieces of vanilla distribution
* packages - my linux toolbox
* adguard - privacy all the time
* raspotify, shairport - make my retired HiFi great again
* kodi - the best smart tv ever
* transmission - the lightest BT daemon
* samba - network attached storage
* backup - to backup or not to backup, that’s no question

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
