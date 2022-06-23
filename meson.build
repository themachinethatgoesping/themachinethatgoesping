# SPDX-FileCopyrightText: 2022 Peter Urban, Ghent University
#
# SPDX-License-Identifier: CC0-1.0

# --- Project ---
# Define project meta data
project(
  'themachinethatgoesping',
  'cpp',
  license: 'MPL-2.0',

  version: '0.0.3.10',
  default_options: ['warning_level=3', 'buildtype=release', 'cpp_std=c++17'],
  meson_version: '>=0.62' #force new meson version to limit necessary testing
)

projectnamespace = 'themachinethatgoesping'


# load themachinethatgoesping projects
tools_project = subproject('tools')
tools_dep = tools_project.get_variable('tools_dep')

# python only projects
echogrids_project = subproject('gridding')

# add python files
subdir('python')

 
