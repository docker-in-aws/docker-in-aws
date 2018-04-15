#!/usr/bin/env bash
set -e

echo "### Configuring Docker Volume Storage ###"
sudo service docker stop
sudo rm -rf /var/lib/docker/volumes
sudo mkdir -p /var/lib/docker/volumes
sudo mkfs.ext4 -L docker /dev/xvdcy
echo -e "LABEL=docker\t/var/lib/docker/volumes\t\text4\tdefaults,noatime\t0\t0" | sudo tee -a /etc/fstab
sudo mount -a