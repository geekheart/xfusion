import xf_build

srcs = [
    "xf_log/src/*.c",
    "xf_log/src/xf_printf/*.c",
    "xf_log/src/xf_printf/mpaland_printf/*.c",
]

incs = [
    ".",
]

xf_build.collect(srcs=srcs, inc_dirs=incs)
