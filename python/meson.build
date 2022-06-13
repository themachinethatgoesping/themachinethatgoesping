# SPDX-FileCopyrightText: 2022 Peter Urban, Ghent University
#
# SPDX-License-Identifier: CC0-1.0

fs = import('fs')

# configure source
conf_data = configuration_data()

if get_option('pydev_install').enabled()
    conf_data.set('PYDEV_SRC_PATH','pydev_install_src_path = "' + meson.source_root() +'/subprojects/"')
    conf_data.set('PYDEV_MODULES','pydev_install_modules = ["tools","gridding"]')
    conf_data.set('PYDEV_INSTALL',fs.read('themachinethatgoesping/in.pydev_install.py'))
endif



pymod = import('python').find_installation(get_option('python_path'), required : get_option('build_pythonmodule'))

if get_option('build_pythonmodule').enabled()
    configure_file(input : 'themachinethatgoesping/in.__init__.py',
                output : '__init__.py',
                configuration : conf_data,
                install_dir : pymod.get_install_dir() + 'themachinethatgoesping', 
                install_tag : 'python-runtime'
                )
endif


