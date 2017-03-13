from setuptools import setup

setup(name='pycsharpmake',
      version='1.0',
      description='compile cs files to exe using python',
      url='https://github.com/sric0880/pycsharpmake.git',
      author='sric0880',
      author_email='justgotpaid88@qq.com',
      license='MIT',
      packages=['pycsharpmake'],
      test_suite='test.my_test_suite',
      install_requires=[
          'pyyaml',
      ],
      zip_safe=False)