{
	"targets": [
		{
			"target_name": "addon",
			"sources": [
				"./native/lib.cc"
			],
			"include_dirs": [
				"<!@(node -p \"require('node-addon-api').include\")"
			],
			"dependencies": [
				"<!(node -p \"require('node-addon-api').gyp\")"
			],
			"cflags!": ["-fno-exceptions"],
			"cflags_cc!": ["-fno-exceptions"],
			"xcode_settings": {
				"GCC_ENABLE_CPP_EXCEPTIONS": "YES",
				"CLANG_CXX_LIBRARY": "libc++",
				"MACOSX_DEPLOYMENT_TARGET": "10.7"
			},
			"msvs_settings": {
				"VCCLCompilerTool": { "ExceptionHandling": 1 },
			},
			"defines": [
				"NAPI_CPP_EXCEPTIONS"
			],
			"conditions": [
				["OS==\"win\"", {
					"libraries": ["<(module_root_dir)/libs/Alt1Native.lib"],
					"copies": [
						{
							"destination": "<(module_root_dir)/dist/",
							"files": ["<(module_root_dir)/libs/InjectDLL64.dll"]
						}, {
							"destination": "<(PRODUCT_DIR)/",
							"files": ["<(module_root_dir)/libs/Alt1Native.dll"]
						}
					]
				}]
			]
		}
	]
}