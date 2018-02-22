#!/usr/bin/env bash
set -e

echo "### Performing final clean-up tasks ###"
sudo service docker stop
sudo chkconfig docker off
sudo rm -rf /var/log/docker /var/log/ecs/*