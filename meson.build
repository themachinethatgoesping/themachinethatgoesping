# SPDX-FileCopyrightText: 2022 Peter Urban, Ghent University
#
# SPDX-License-Identifier: CC0-1.0

# --- Project ---
# Define project meta data
project(
  'themachinethatgoesping',
  'cpp',
  license: 'MPL-2.0',

  version: '0.4.1',
  default_options: ['warning_level=2', 'buildtype=release', 'cpp_std=c++17'],
  meson_version: '>=0.63' #0.63 added preserve_path for install headers option
)

projectnamespace = 'themachinethatgoesping'


# load themachinethatgoesping projects
module_meta  = subproject('meta', default_options: ['main_project_version=' + meson.project_version()])
module_tools = subproject('tools')
module_navigation = subproject('navigation')
module_echosounders = subproject('echosounders')

# python only projects
module_gridding = subproject('gridding')

# add python files
subdir('python')

 
