from os import environ
from os.path import dirname, join
from distutils.core import setup
from distutils.extension import Extension
try:
    from Cython.Distutils import build_ext
    have_cython = True
except ImportError:
    have_cython = False

if have_cython:
    kivyparticle_files = [
        'kivyparticle/python/kivyparticle.pyx',
        ]
    cmdclass = {'build_ext': build_ext}
else:
    kivyparticle_files = ['kivyparticle/python/kivyparticle.c',]
    cmdclass = {}

ext = Extension('kivyparticle',
    kivyparticle_files, include_dirs=[],
    extra_compile_args=['-std=c99', '-ffast-math'])

if environ.get('READTHEDOCS', None) == 'True':
    ext.pyrex_directives = {'embedsignature': True}

setup(
    name='kivyparticle',
    description='Kivy Particle is a Particle Engine compatible with the Starling Particle Engine',
    author='Jacob Kovac',
    author_email='kovac1066@gmail.com',
    cmdclass=cmdclass,
    ext_modules=[ext])
