#!/bin/bash

# SPDX-FileCopyrightText: 2022 Peter Urban, Ghent University
# SPDX-FileCopyrightText: 2022 Valentin Buck, GEOMAR Helmholtz Centre for Ocean Research Kiel
#
# SPDX-License-Identifier: MPL-2.0

FROM continuumio/anaconda3
LABEL maintainer="Peter Urban <peter.urban@ugent.be>"

ARG DEBIAN_FRONTEND=noninteractive

# RUN apt-get update && apt-get install -y sudo git git-lfs apt-utils
# RUN apt update -y; apt upgrade -y
# RUN rm -r /usr/include
# RUN apt install -y libboost-all-dev
# RUN pip install meson ninja
#
# RUN git clone https://github.com/themachinethatgoesping/themachinethatgoesping.git
# WORKDIR "/themachinethatgoesping"
# RUN git submodule update --init --recursive --remote
# WORKDIR "/themachinethatgoesping/conda.recipe"

# # install prequisits
# RUN apt-get update && apt-get install -y sudo git git-lfs apt-utils
#
RUN apt-get update -qq

# install dependecies (c++)
RUN apt-get install -y build-essential ccache pkg-config cmake python3-pip libboost-all-dev libcurl4-openssl-dev

# install extra dependecies (instead of subprojects)
RUN apt-get install -y catch2 libeigen3-dev pybind11-dev

 # install dependcies (meson & pythone)
#RUN apt-get install -y meson ninja-build python3-pytest
RUN pip install meson ninja pytest

 # update and upgrade
RUN apt-get update; apt-get upgrade -y

# Reset terminal to interactive mode
ARG DEBIAN_FRONTEND=teletype
