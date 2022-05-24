#!/bin/bash

# SPDX-FileCopyrightText: 2022 Peter Urban, Ghent University
# SPDX-FileCopyrightText: 2022 Valentin Buck, GEOMAR Helmholtz Centre for Ocean Research Kiel
#
# SPDX-License-Identifier: MPL-2.0

FROM ubuntu:latest
MAINTAINER Peter Urban <peter.urban@ugent.be>

# install prequisits
RUN apt-get update && apt-get install -y sudo git

RUN apt-get update -qq

ARG DEBIAN_FRONTEND=noninteractive

# install dependecies (c++)
RUN apt-get install -y build-essential ccache pkg-config cmake python3-pip libboost-all-dev

# install extra dependecies (instead of subprojects)
RUN apt-get install -y catch2 libeigen3-dev pybind11-dev

# install dependcies (meson & pythone)
RUN apt-get install meson ninja-build python3-pytest
#RUN pip install meson ninja pytest numpy

# update and upgrade
RUN apt-get update; apt-get upgrade -y

# Reset terminal to interactive mode
ARG DEBIAN_FRONTEND=teletype
