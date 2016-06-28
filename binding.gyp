{
  'variables': {
    'use_system_libnanomsg%': 'false',
  },
  'targets': [
    {
      'target_name': 'node_nanomsg',
      'sources': [ 'src/node_nanomsg.cc' ],
      'include_dirs': [
        "<!(node -e \"require('nan')\")",
      ],
      'conditions': [
        ['use_system_libnanomsg=="false"', {
          'dependencies': [ 'deps/nanomsg.gyp:nanomsg', ],
        }],
        ['OS=="linux" and use_system_libnanomsg=="true"', {
          'include_dirs+': [
            '<!@(pkg-config nanomsg --cflags-only-I | sed s/-I//g)/nanomsg',
          ],
          'libraries': [
            '<!@(pkg-config nanomsg --libs)',
          ],
        }],
        ['OS=="mac" and use_system_libnanomsg=="true"', {
          'include_dirs+': [
            '<!@(pkg-config libnanomsg --cflags | sed s/-I//g)',
          ],
          'libraries': [
            '<!@(pkg-config libnanomsg --libs)',
          ],
        }],
        ['OS=="win"', {
          'cflags': [ '-Wall -Werror -Wno-unused' ],
          'cflags_cc': ['-fexceptions'],
        }],
      ],
    },
  ],
}
