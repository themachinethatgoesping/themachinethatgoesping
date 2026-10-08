# SPDX-FileCopyrightText: 2022 - 2023 Peter Urban, Ghent University
#
# SPDX-License-Identifier: CC0-1.0

# --- Project ---
# Define project meta data
project(
  'themachinethatgoesping',
  'cpp',
  license: 'MPL-2.0',

  version: '0.37.0.dev1',
  default_options: ['warning_level=0', 'buildtype=release', 'cpp_std=c++26'],
  meson_version: '>=1.8.1' #there is a problem with meson 1.8.0 so just use a higher version
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
module_widgets= subproject('widgets', default_options: ['cpp_std=' + get_option('cpp_std')])

# python only projects
module_gridding = subproject('gridding', default_options: ['cpp_std=' + get_option('cpp_std')])

# add python files
subdir('python')

# Stub generation using nanobind's native stubgen
# Runs after install since stubgen needs to import the installed module
if get_option('build_pythonmodule').enabled()
    pymod = import('python').find_installation(get_option('python_path'), required: true, pure: false)
    nanobind_dep = dependency('nanobind', version: '>=2.9.1')
    stubgen = nanobind_dep.get_variable('stubgen')
    
    # Generate stubs
    meson.add_install_script(
        pymod,
        stubgen,
        '-m', 'themachinethatgoesping',
        '-r',
        '-O', meson.current_source_dir() / 'python' / 'stubs',
        install_tag: 'python-runtime',
    )
    
    # Fix invalid syntax in generated stubs (numpy.ndarray[dtype=...] etc.)
    meson.add_install_script(
        pymod,
        meson.current_source_dir() / 'python' / 'fix_stubs.py',
        meson.current_source_dir() / 'python' / 'stubs',
        install_tag: 'python-runtime',
    )

    # --- docstring generation (pybind11_mkdoc, driven by Meson) ---
    # Regenerate the per-header .doc.hpp side-car files on demand. Each C++
    # module gets its own target, plus a 'mkdoc' alias that runs them all:
    #   meson compile -C builddir mkdoc-navigation
    #   meson compile -C builddir mkdoc
    # The driver reads the -I/-isystem/-D/-std flags from compile_commands.json
    # and pins libclang to the build's Python environment, so it works with both
    # the fork and upstream pybind11_mkdoc. For verbose output or a single header
    # use the CLI (python/make_pybind_doc.py --help).
    mkdoc_modules = ['tools', 'navigation', 'algorithms', 'echosounders', 'pingprocessing']
    mkdoc_targets = []
    foreach mod : mkdoc_modules
        mkdoc_targets += run_target(
            'mkdoc-' + mod,
            command: [
                pymod, '-m', 'pybind11_mkdoc.meson_mkdoc',
                '--module-root', meson.current_source_dir() / 'subprojects' / mod / 'src' / 'themachinethatgoesping',
                '--doc-header', meson.current_source_dir() / 'subprojects' / mod / 'src' / 'nanomodule' / 'new_doc_header.hpp',
                '--build-root', meson.global_build_root(),
            ],
        )
    endforeach

    alias_target('mkdoc', mkdoc_targets)
endif

 
