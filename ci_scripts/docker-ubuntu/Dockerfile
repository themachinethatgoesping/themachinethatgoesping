#!/bin/bash

# SPDX-FileCopyrightText: 2022 Peter Urban, Ghent University
# SPDX-FileCopyrightText: 2022 Valentin Buck, GEOMAR Helmholtz Centre for Ocean Research Kiel
#
# SPDX-License-Identifier: MPL-2.0

FROM ubuntu:latest
LABEL maintainer="Peter Urban <peter.urban@ugent.be>"

# install perquisites
RUN apt update && apt install -y sudo git git-lfs apt-utils

RUN apt update -qq

ARG DEBIAN_FRONTEND=noninteractive

# install dependencies (c++)
RUN apt install -y build-essential ccache pkg-config cmake python3-pip libboost-all-dev

# install extra dependencies (instead of subprojects)
RUN apt install -y catch2 libeigen3-dev pybind11-dev

# install dependencies (meson & python)
#RUN apt-get install -y meson ninja-build python3-pytest
RUN pip install meson ninja pytest

# update and upgrade
RUN apt update; apt upgrade -y

# Reset terminal to interactive mode
ARG DEBIAN_FRONTEND=teletype
