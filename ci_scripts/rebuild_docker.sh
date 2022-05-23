#!/bin/bash

# SPDX-FileCopyrightText: 2022 Peter Urban, Ghent University
# SPDX-FileCopyrightText: 2022 Valentin Buck, GEOMAR Helmholtz Centre for Ocean Research Kiel
#
# SPDX-License-Identifier: MPL-2.0

#Check if docker is installed, install it otherwise 
dpkg-query -l | grep -q docker || (sudo apt-get update; sudo apt-get install docker docker.io; sudo groupadd docker; sudo usermod -aG docker $USER; newgrp docker)

#Build image and push to registry
echo $PAT | docker login ghcr.io --username themachinethatgoesping --password-stdin

docker build -t ghcr.io/themachinethatgoesping/ubuntu_dependencies .
docker push ghcr.io/themachinethatgoesping/ubuntu_dependencies

#read -p "Please press enter to continue"

