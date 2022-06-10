# SPDX-FileCopyrightText: 2022 Peter Urban, Ghent University
#
# SPDX-License-Identifier: CC0-1.0

# -- python sources --
sources = [
    'themachinethatgoesping/__init__.py'
]

pymod = import('python').find_installation(get_option('python_path'), required : get_option('build_pythonmodule'))
if get_option('build_pythonmodule').enabled()
    
    foreach source : sources
        #create install path for file
        fields = [pymod.get_install_dir()]
        foreach field : source.split('/')
            if not field.endswith('.py')
                fields += [field]
            endif
        endforeach
        pth = '/'.join(fields)

        install_data(source, install_dir : pth, install_tag : 'python-runtime')
        #pymod.install_sources(source, subdir : subdir, )
    endforeach

endif
