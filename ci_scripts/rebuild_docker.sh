#!/bin/bash

# SPDX-FileCopyrightText: 2022 Peter Urban, Ghent University
# SPDX-FileCopyrightText: 2022 Valentin Buck, GEOMAR Helmholtz Centre for Ocean Research Kiel
#
# SPDX-License-Identifier: MPL-2.0

#Check if docker is installed, install it otherwise 
dpkg-query -l | grep -q docker || (sudo apt-get update; sudo apt-get install docker docker.io; sudo groupadd docker; sudo usermod -aG docker $USER; newgrp docker)

#Build image and push to registry
echo $PAT | docker login ghcr.io --username themachinethatgoesping --password-stdin

docker build docker-ubuntu -t ghcr.io/themachinethatgoesping/ubuntu-dep --no-cache
docker push ghcr.io/themachinethatgoesping/ubuntu-dep

docker build docker-manylinux_x86_64 -t ghcr.io/themachinethatgoesping/manylinux_x86_64-dep #--no-cache
docker push ghcr.io/themachinethatgoesping/manylinux_x86_64-dep

#docker build docker-manylinux_aarch64 -t ghcr.io/themachinethatgoesping/manylinux_aarch64-dep #--no-cache
#docker push ghcr.io/themachinethatgoesping/manylinux_aarch64-dep

#docker build docker-manylinux_ppc64le -t ghcr.io/themachinethatgoesping/manylinux_ppc64le-dep #--no-cache
#docker push ghcr.io/themachinethatgoesping/manylinux_ppc64le-dep

#read -p "Please press enter to continue"

