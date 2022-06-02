# SPDX-FileCopyrightText: 2022 Peter Urban, Ghent University
#
# SPDX-License-Identifier: CC0-1.0

# --- Project ---
# Define project meta data
project(
  'themachinethatgoesping',
  'cpp',
  license : 'MPL-2.0',

  version : '0.0.1.6',
  default_options : ['warning_level=3', 'buildtype=release', 'cpp_std=c++17']
)

projectnamespace = 'themachinethatgoesping'

# --- dependencies ---
# system
if meson.get_compiler('cpp').get_id() == 'clang'
  add_project_arguments('-Xpreprocess', language : 'cpp')
endif
omp    = dependency('openmp')


# load themachinethatgoesping projects
tools_project = subproject('tools')
tools_dep = tools_project.get_variable('tools_dep')

 
