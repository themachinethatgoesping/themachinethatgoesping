# SPDX-FileCopyrightText: 2022 Peter Urban, Ghent University
#
# SPDX-License-Identifier: CC0-1.0

# --- Project ---
# Define project meta data
project(
  'themachinethatgoesping',
  'cpp',
  license: 'MPL-2.0',

  version: '0.1.0',
  default_options: ['warning_level=3', 'buildtype=release', 'cpp_std=c++17'],
  meson_version: '>=0.63' #0.63 added preserve_path for install headers option
)

projectnamespace = 'themachinethatgoesping'


# load themachinethatgoesping projects
tools_dep = subproject('tools').get_variable('tools_dep')
navigation_dep = subproject('navigation').get_variable('navigation_dep')

# python only projects
echogrids_project = subproject('gridding')

# add python files
subdir('python')

 
