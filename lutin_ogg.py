#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import lutin.debug as debug
import os


def get_type():
	return "LIBRARY"

def get_desc():
	return "Ogg-tremor library for ogg audio decoding"

def get_licence():
	return "BSD-3"

def get_compagny_type():
	return "org"

def get_compagny_name():
	return "xiph"

def get_version():
	return [1,3,0]

def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	my_module.add_src_file([
		'ogg/ogg/framing.c',
		'ogg/ogg/bitwise.c',
		'ogg/tremor/floor0.c',
		'ogg/tremor/vorbisfile.c',
		'ogg/tremor/synthesis.c',
		'ogg/tremor/res012.c',
		'ogg/tremor/block.c',
		'ogg/tremor/mdct.c',
		'ogg/tremor/sharedbook.c',
		'ogg/tremor/codebook.c',
		'ogg/tremor/floor1.c',
		'ogg/tremor/window.c',
		'ogg/tremor/registry.c',
		'ogg/tremor/info.c',
		'ogg/tremor/mapping0.c'
		])
	my_module.compile_version("c", 1989, gnu=True)
	my_module.compile_flags('c', "-Wno-duplicate-decl-specifier")
	if target.name=="Android":
		my_module.compile_flags('c', "-DBYTE_ORDER=1")
		my_module.compile_flags('c', "-DBIG_ENDIAN=0")
		my_module.compile_flags('c', "-DLITTLE_ENDIAN=1")
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "ogg"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "ogg/ogg"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "ogg/tremor"))
	my_module.add_header_file([
		'ogg/tremor/window_lookup.h',
		'ogg/tremor/mdct.h',
		'ogg/tremor/misc.h',
		'ogg/tremor/mdct_lookup.h',
		'ogg/tremor/registry.h',
		'ogg/tremor/codebook.h',
		'ogg/tremor/config_types.h',
		'ogg/tremor/lsp_lookup.h',
		'ogg/tremor/block.h',
		'ogg/tremor/asm_arm.h',
		'ogg/tremor/codec_internal.h',
		'ogg/tremor/ivorbiscodec.h',
		'ogg/tremor/os.h',
		'ogg/tremor/window.h',
		'ogg/tremor/backends.h',
		'ogg/tremor/ivorbisfile.h'
		],
		destination_path="tremor")
	my_module.add_header_file([
		'ogg/ogg/ogg.h',
		'ogg/ogg/os_types.h'
		],
		destination_path="ogg")
	return my_module









