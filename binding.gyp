{
  "targets": [
    {
      "target_name": "uws_<(OS)_<(node_module_version)",
      "defines": [
        "UWS_WITH_PROXY",
        "LIBUS_USE_LIBUV",
        "LIBUS_USE_OPENSSL"
      ],
      "include_dirs": [
        "uWebSockets/uSockets/src",
        "uWebSockets/src"
      ],
      "sources": [
        "<!@(node -p \"require('fs').readdirSync('./uWebSockets/uSockets/src').filter(f=>/.c$/.exec(f)).map(f=>'uWebSockets/uSockets/src/'+f).join(' ')\")",
        "<!@(node -p \"require('fs').readdirSync('./uWebSockets/uSockets/src/eventing').filter(f=>/.c$/.exec(f)).map(f=>'uWebSockets/uSockets/src/eventing/'+f).join(' ')\")",
        "<!@(node -p \"require('fs').readdirSync('./uWebSockets/uSockets/src/crypto').filter(f=>/.c$/.exec(f)).map(f=>'uWebSockets/uSockets/src/crypto/'+f).join(' ')\")",
        "src/addon.cpp",
        "uWebSockets/uSockets/src/crypto/sni_tree.cpp"
      ],
      "conditions": [
        [
          "OS=='win'",
          {
            "cflags": [
              "/W3",
              "/EHsc",
              "/Ox"
            ],
            "msbuild_settings": {
              "ClCompile": {
                "LanguageStandard": "stdcpp17"
              }
            }
          }
        ],
        [
          "OS=='linux'",
          {
            "cflags": [
              "-flto",
              "-O3",
              "-c",
              "-fPIC"
            ],
            "cflags_cc": [
              "--std=c++17"
            ],
          }
        ],
        [
          "OS=='mac'",
          {
            "xcode_settings": {
              'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
              "CLANG_CXX_LIBRARY": "libc++",
              "CLANG_CXX_LANGUAGE_STANDARD":"c++17",
              'MACOSX_DEPLOYMENT_TARGET': '10.14'
            },
            "cflags": [
              "-flto",
              "-O3",
              "-c",
              "-fPIC"
            ],
            "cflags_cc": [
              "--std=c++17"
            ],
          }
        ]
      ]
    }
  ]
}