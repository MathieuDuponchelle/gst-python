runtests = files('runtests.py')

tests = [
    ['Test gst', 'test_gst.py'],
    ['Test fundamentals', 'test_types.py'],
]

pluginsdirs = []
if not meson.is_subproject()
  pkgconfig = find_program('pkg-config')
  runcmd = run_command(pkgconfig, '--variable=pluginsdir',
      'gstreamer-' + api_version)
  if runcmd.returncode() == 0
      pluginsdirs = runcmd.stdout().split()
  else
    error('Could not determine GStreamer core plugins directory for unit tests.')
  endif
endif

runcmd = run_command(python, '-c', '''with open("@0@/mesonconfig.py", "w") as f:
    f.write("path='@1@'")'''.format(
  join_paths(meson.current_build_dir()), join_paths(meson.current_build_dir(), '..')))

if runcmd.returncode() != 0
    error('Could not configure testsuite config file.' + runcmd.stderr())
endif

gi_dir = join_paths(pygi_override_dir, '..', '..')

foreach i: tests
    test_name = i.get(0)
    env = environment()
    env.prepend('PYTHONPATH', [gi_dir, gi_overrides_build_dir])
    test(test_name, python, args: [runtests, i.get(1)], env: env)
endforeach
