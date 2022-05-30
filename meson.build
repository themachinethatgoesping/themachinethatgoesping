# SPDX-FileCopyrightText: 2022 Peter Urban, Ghent University
#
# SPDX-License-Identifier: CC0-1.0

# --- Project ---
# Define project meta data
project(
  'themachinethatgoesping',
  'cpp',
version : '0.0.1.2',
default_options : ['warning_level=3', 'buildtype=release', 'cpp_std=c++20']
)

projectnamespace = 'themachinethatgoesping'

# --- dependencies ---
# system
omp    = dependency('openmp')


# load themachinethatgoesping projects
tools_project = subproject('tools')
tools_dep = tools_project.get_variable('tools_dep')

 
