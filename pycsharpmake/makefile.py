import yaml, os, platform
from os import path

class Makefile:
	def __init__(self, runnable = None):
		self.windows = platform.system().startswith("Windows")
		self.runnable = runnable 

	def make(self, filename, out_root_path, scripts_root_path):
		with file(filename, 'r') as stream:
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

		cmd = '%s %s /out:%s /main:%s %s %s %s %s' % \
			('csc' if self.windows else 'mcs',
				'/debug' if isDebug else '',
				outfile,
				mainfile,
				'/r:' + ','.join(dlls) if dlls else '',
				'/define:' + defines if defines else '',
				' '.join(files) if files else '',
				' '.join(folders) if folders else '')

		if os.system(cmd) != 0:
			raise Exception("Compile error")
		else:
			self.runnable = outfile
			print 'Compile success'

	def run(self, *args):
		if self.runnable:
			cmd = '%s%s %s' % (\
				'' if self.windows else 'mono ',
				self.runnable,
				' '.join(args) if args else '')
			print cmd
			if os.system(cmd) != 0:
				raise Exception("error generate code")

if __name__ == '__main__':
	makefile = Makefile()
	makefile.make('', '', '')
	makefile.run()
