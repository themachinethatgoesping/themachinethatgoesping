# SPDX-FileCopyrightText: 2022 - 2023 Peter Urban, Ghent University
#
# SPDX-License-Identifier: BSD-3-Clause
#
# Minimal project that compiles the nanobind "backend" module (the libnanobind
# backend used by split-mode extensions). It is packaged separately as the
# conda package "nanobind-backend" and published to the themachinethatgoesping
# channel, mirroring the PyPI package of the same name.
#
# See https://nanobind.readthedocs.io/en/latest/split_mode.html

cmake_minimum_required(VERSION 3.15...3.30)
project(nanobind_backend_pkg LANGUAGES CXX)

find_package(Python 3.9 COMPONENTS Interpreter Development.Module REQUIRED)

# nanobind ships the CMake helpers and the backend sources (nb_backend.cpp).
# Provided by the conda-forge `nanobind` host dependency; point nanobind_DIR at
# `python -c "import nanobind; print(nanobind.cmake_dir())"` when configuring.
find_package(nanobind CONFIG REQUIRED)

# Build the compiled backend module. This produces an extension named
# `nanobind_backend` exposing the `fill()` entry point that split-mode
# extensions call at import time. The backend is a normal (non-limited-API)
# module, compiled once per Python version.
nanobind_add_backend(nanobind_backend)

# Install the module straight into site-packages (CMAKE_INSTALL_PREFIX is set to
# the conda environment's site-packages by the recipe).
install(TARGETS nanobind_backend
        LIBRARY DESTINATION "."
        RUNTIME DESTINATION ".")
