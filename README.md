# Raspberry PI Configuration

My Raspberry Pi installation at home.

* Do not touch anything by hand, use Ansible.
* If something is hard to automate, document it at least.

## Hardware

* Raspberry Pi 4 model B, 4GB
* HiFiBerry DAC+
* RAIDON GR3660-B3 (with fan turned off)

![hardware](static/hardware.jpg)

## Manual setup

### Install image

The repository is tested against Raspberry Pi OS Lite 64 bit (Debian 11 "Bullseye").

1. Install image on SD card
1. Append `ip=«IP»` into `cmdline.txt`
1. Enable ssh `touch ssh`
1. Configure default user account with `pi` password `echo "pi:vCKtyl9xwqPxU" > userconf`

### Configuring SSH

Generate key:

```shell
ssh-keygen -f pi_rsa
```

Configure client:

```shell
cat <<EOT >> ~/.ssh/config
Host pi
 HostName «IP»
 User pi
 IdentityFile ~/.ssh/pi_rsa
EOT
```

Copy key to Raspberry Pi:

```shell
ssh-copy-id -i ~/.ssh/pi_rsa.pub pi
```

## Ansible playbooks

Install 3rd party roles:

```shell
ansible-galaxy install -r requirements.yml
```

### Pimp my Pi playbooks

Various playbooks to improve vanilla Raspberry Pi setup:

```shell
ansible-playbook pimpmypi.yml
```

Roles:

* common - missing pieces of vanilla Raspberry distribution
* aria2 - the fastest utility for downloading files
* docker - Docker repository and packages
* fluentbit - send systemd logs to [GCP Logging](https://cloud.google.com/logging)
  and/or [Loki](https://grafana.com/oss/loki/), see [readme](roles/fluentbit/README.md)
* grafana - monitoring with [Grafana Cloud](https://grafana.com/products/cloud/) (free tier)
* hdidle - spin-down disks, see [Github](https://github.com/adelolmo/hd-idle)
* log2ram - move logs into RAM, see [Github](https://github.com/azlux/log2ram)
* posfix - forward mails to real account
* smartmontools - monitor hard drives

### Other playbooks

* adguard - privacy all the time, see [AdGuard Home](https://adguard.com/en/adguard-home/overview.html)
* backup - to backup or not to backup, that’s no question, see [Backup Ninja](https://0xacab.org/liberate/backupninja)
* hyperion - ambient lighting, see [Hyperion](https://hyperion-project.org/)
* kodi - the best [media center](https://kodi.wiki/view/Main_Page), see [readme](roles/kodi/README.md)
* raspotify, shairport - make my retired HiFi great again: [Raspotify](https://github.com/dtcooper/raspotify)
  , [Librespot](https://github.com/librespot-org/librespot), [Shairport](https://github.com/mikebrady/shairport-sync)
* samba - my family disk for files and automated backups, see [Samba](https://www.samba.org)
* viewtube - YouTube without ads, see [ViewTube](https://viewtube.io/)
* tailscale - VPN done right, see [Tailscale](https://tailscale.com/)
* traefik - Reverse proxy, see [Traefik](https://doc.traefik.io/traefik/)
* transmission - BitTorrent daemon, see [Transmission](https://transmissionbt.com)

### Upgrade playbook

Upgrade system to the latest Bullseye:

```shell
ansible all -m apt -a "upgrade=yes update_cache=yes"
```

The following packages have versions pinned and needs to updated explicitly:

* adguard
* grafana-agent
* kodi
* viewtube
