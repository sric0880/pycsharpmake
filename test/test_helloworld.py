import pycsharpmake
makefile = pycsharpmake.Makefile()
makefile.make("test/helloworld.yaml", "test", "test")
makefile.run()