try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages

import os
import sys

# disables creation of .DS_Store files inside tarballs on Mac OS X
os.environ['COPY_EXTENDED_ATTRIBUTES_DISABLE'] = 'true'
os.environ['COPYFILE_DISABLE'] = 'true'

import tinybuddhawisdom

DESCRIPTION = 'Tinybuddha Wisdom is a tiny console fortune-like wisdom teller.'

setup(
    author=tinybuddhawisdom.__author__,
    author_email=tinybuddhawisdom.__author_email__,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.3',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
    data_files=[],
    description=DESCRIPTION,
    ext_modules=[],
    install_requires=[],
    license=tinybuddhawisdom.__license__,
    long_description=DESCRIPTION,
    name='tinybuddhawisdom',
    packages=find_packages(),
    package_data={},
    setup_requires=[],
    url=tinybuddhawisdom.__url__,
    use_2to3=(sys.version_info >= (3,)),
    version=tinybuddhawisdom.__version__,
    entry_points={'console_scripts' : [
        'tinybuddha = tinybuddhawisdom.app:main']},
)

