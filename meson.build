# SPDX-FileCopyrightText: 2022 - 2023 Peter Urban, Ghent University
#
# SPDX-License-Identifier: CC0-1.0

# --- Project ---
# Define project meta data
project(
  'themachinethatgoesping',
  'cpp',
  license: 'MPL-2.0',

  version: '0.18.1',
  default_options: ['warning_level=2', 'buildtype=release', 'cpp_std=c++20'],
  meson_version: '>=1.3.2' #first version with  clang-cl openmp support
)
# Set-Item -Path Env:\CXX -Value 'sccache clang-cl'
projectnamespace = 'themachinethatgoesping'

# load themachinethatgoesping projects
module_meta  = subproject('meta', default_options: ['main_project_version=' + meson.project_version(), 'cpp_std=' + get_option('cpp_std')])
module_tools = subproject('tools', default_options: ['cpp_std=' + get_option('cpp_std')])
module_algorithms = subproject('algorithms', default_options: ['cpp_std=' + get_option('cpp_std')])
module_navigation = subproject('navigation', default_options: ['cpp_std=' + get_option('cpp_std')])
module_echosounders = subproject('echosounders', default_options: ['cpp_std=' + get_option('cpp_std')])
module_pingprocessing= subproject('pingprocessing', default_options: ['cpp_std=' + get_option('cpp_std')])

# python only projects
module_gridding = subproject('gridding', default_options: ['cpp_std=' + get_option('cpp_std')])

# add python files
subdir('python')

 
