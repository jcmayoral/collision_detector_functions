try:
    # Try using ez_setup to install setuptools if not already installed.
    from ez_setup import use_setuptools
    use_setuptools()
except ImportError:
    # Ignore import error and assume Python 3 which already has setuptools.
    pass

from setuptools import setup, find_packages

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: None',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name              = 'Thesis_packages',
      version           = '1.0.0',
      author            = 'Jose C Mayoral Banos',
      author_email      = 'jocamaba1989@gmail.com',
      description       = 'Python packages used for the master thesis of Jose Mayoral Banos',
      license           = 'none',
      classifiers       = classifiers,
      url               = 'https://github.com/adafruit/Adafruit_Python_ADXL345/',
      dependency_links  = ['https://github.com/jcmayoral/myRaspberryPI.git'],
      install_requires  = [''],
      packages          = find_packages())
