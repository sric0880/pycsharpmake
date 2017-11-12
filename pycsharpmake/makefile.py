import yaml, os, platform
from os import path

class Makefile:
	def __init__(self, runnable = None):
		self.windows = platform.system().startswith("Windows")
		self.runnable = runnable 

	def make(self, filename, out_root_path, scripts_root_path):
		with open(filename, 'r') as stream:
			content = yaml.load(stream)
		if not content:
			raise Exception('makefile %s not supported or not found' % filename)

		outfile = path.join(out_root_path, content['out'])

		mainfile = content['main']

		isDebug = content['debug']

		dlls = content.get('depends')
		if dlls:
			dlls = [path.join(out_root_path, x) for x in dlls]

		defines = content.get('defines')

		files = content.get('files')
		if files:
			files = [path.join(scripts_root_path, x) for x in files]

		folders = content.get('folders')
		if folders:
			folders = ['/recurse:' + path.join(scripts_root_path, x) for x in folders]

		cmd = '%s %s /out:%s %s %s %s %s %s' % \
			('csc' if self.windows else 'mcs',
				'/debug' if isDebug else '',
				outfile,
				'/main:' + mainfile if mainfile is not None else '/target:library',
				'/r:' + ','.join(dlls) if dlls else '',
				'/define:' + defines if defines else '',
				' '.join(files) if files else '',
				' '.join(folders) if folders else '')

		if os.system(cmd) != 0:
			print(cmd)
			raise Exception("Compile error")
		else:
			self.runnable = outfile
			print('Compile success')

	def run(self, *args, **kwargs):
		if self.runnable:
			executable = '' if self.windows else 'mono '
			debugable = '' if self.windows or not kwargs.get('debug') else '--debug '
			all_args = ' '.join(args) if args else ''
			cmd = executable + debugable + self.runnable + ' ' + all_args
			print(cmd)
			if os.system(cmd) != 0:
				raise Exception("error generate code")

if __name__ == '__main__':
	makefile = Makefile()
	makefile.make('', '', '')
	makefile.run()
