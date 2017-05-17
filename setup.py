import os
import os.path
from distutils.core import setup


here = os.path.abspath(os.path.dirname(__file__))
version_path = os.path.join(here, 'onvif/version.txt')
version = open(version_path).read().strip()

#

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Customer Service',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Telecommunications Industry',
    'Natural Language :: English',
    'Operating System :: POSIX',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Multimedia :: Sound/Audio',
    'Topic :: Utilities',
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
]

setup(
      name='onvif-py3',
      version=version,
      description='Python Client for ONVIF Camera',
      long_description=open('README.rst', 'r').read(),
      author='Cherish Chen',
      author_email='sinchb128@gmail.com',
      maintainer='rambo',
      maintainer_email='rambo@iki.fi',
      license='MIT',
      keywords=['ONVIF', 'Camera', 'IPC'],
      url='http://github.com/rambo/python-onvif',
      zip_safe=False,
      packages=['onvif', 'onvif.wsdl'],
      install_requires=['suds-py3'],
      dependency_links=['http://github.com/tgaugry/suds-passworddigest-py3/tarball/master#egg=suds-passworddigest-0.1.2a'],
      package_data={
          '': ['*.txt', '*.rst'],
          'onvif': ['*.wsdl', '*.xsd', '*xml*', 'envelope', 'include', 'addressing'],
          'onvif.wsdl': ['*.wsdl', '*.xsd', '*xml*', 'envelope', 'include', 'addressing'],
      },
      entry_points={
          'console_scripts': ['onvif-cli = onvif.cli:main']
          }
     )


