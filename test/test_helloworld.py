import pycsharpmake
makefile = pycsharpmake.Makefile()
makefile.make("test/helloworld.yaml", "test", "test")
makefile.run("test_param1", "test_param2")
makefile.run("test_param1", "test_param2", debug=True)
makefile.run("test_param1", "test_param2", debug=False)
