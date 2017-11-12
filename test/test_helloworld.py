import pycsharpmake
makefile = pycsharpmake.Makefile()
# test compile exe
makefile.make("test/helloworld.yaml", "test", "test")
makefile.run("test_param1", "test_param2")
makefile.run("test_param1", "test_param2", debug=True)
makefile.run("test_param1", "test_param2", debug=False)
# test compile dll
makefile.make("test/helloworld_dll.yaml", "test", "test")
