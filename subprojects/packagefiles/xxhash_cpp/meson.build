# SPDX-FileCopyrightText: 2022 - 2023 Peter Urban, Ghent University
# SPDX-FileCopyrightText: 2019 - 2022 Daniil Goncharov
#
# SPDX-License-Identifier: MIT

project(
    'xxhash_cpp', ['cpp'],
    default_options: ['cpp_std=c++20'],
    version: '0.9.dev0',
)

sse2neon_dep = dependency('sse2neon')

xxhash_cpp_include = include_directories('include')

xxhash_cpp_dep = declare_dependency(
    include_directories: xxhash_cpp_include,
    dependencies: [sse2neon_dep],
)

# list and install headers
headers = [
    ]

#install_headers(headers, preserve_path: false)
