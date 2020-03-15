from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


with open("README.md", "r") as fh:
    long_description = fh.read()

with open('LICENSE') as f:
    license = f.read()

ext_modules = [
    Extension("pyland",  
               sources = ["pyland/Pyland.py"]),
]

setup(
    name="pyland",
    version="0.0.1",
    author="Shakerin Ahmed",
    author_email="shakerin.ahmed@gmail.com",
    description="Universal Text Generator and Code Executor 2 in 1",
    long_description=long_description,
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules,
    license=license,
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX :: Linux",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities',
        'Topic :: Scientific/Engineering',
    ],
)