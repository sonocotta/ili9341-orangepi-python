from setuptools import setup, find_packages


classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name              = 'OrangePi.ILI9341',
      version           = '1.0.0',
      author            = 'Andriy Malyshenko',
      author_email      = 'andriy@sonocotta.com',
      description       = 'Library to control ILI9341 TFT LCD displays on the Orange Pi.',
      license           = 'MIT',
      classifiers       = classifiers,
      url               = 'https://github.com/sonocotta/ili9341-orangepi-python',
      install_requires  = [
            'OPi.GPIO',
            'spidev',
            'Pillow',
            'NumPy'
      ],
      packages          = find_packages())
