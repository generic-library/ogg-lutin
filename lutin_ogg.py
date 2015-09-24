#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import lutin.debug as debug

def get_desc():
	return "Ogg-tremor library for ogg audio decoding"


def create(target):
	my_module = module.Module(__file__, 'ogg', 'LIBRARY')
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
	my_module.compile_version_CC(1989, gnu=True)
	my_module.compile_flags('c', "-Wno-duplicate-decl-specifier")
	if target.name=="Android":
		my_module.compile_flags('c', "-DBYTE_ORDER=1")
		my_module.compile_flags('c', "-DBIG_ENDIAN=0")
		my_module.compile_flags('c', "-DLITTLE_ENDIAN=1")
	my_module.add_export_path(tools.get_current_path(__file__) + "/ogg")
	my_module.add_path(tools.get_current_path(__file__)+"/ogg/ogg/")
	my_module.add_path(tools.get_current_path(__file__)+"/ogg/tremor/")
	return my_module









