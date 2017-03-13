# pycsharpmake
compile cs files to exe using python

## Install

```
cd pycsharpmake
sudo pip install .
```

## Unit Test

```
cd pycsharpmake
python setup.py test
```

## Usage
see example under test dir

```python
import pycsharpmake
makefile = pycsharpmake.Makefile()
makefile.make(build_config, scirpt_path, assets_path)
makefile.run()
```

__build_config__: yaml format text for compile parameters, examples:

```yaml
out: bin/out.exe
main: MainClassName
debug: Yes/No
depends:
 - bin/xxx.dll
 - bin/xxx.dll
defines: CUSTOM_DEFINES,EDITOR,ANDROID
files:
 - xxxFolder/xxx.cs
folders:
 - xxxFolder/xxxSubFolder/*.cs
 - xxxFolder/xxxSubFolder/*.cs
```

__script_path__: c# code root path

__assets_path__: root path for the export exe and dependency dlls
