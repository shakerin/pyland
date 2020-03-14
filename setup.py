import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyland",
    version="0.0.1",
    author="Shakerin Ahmed",
    packages='ucg'.split(),
    author_email="shakerin.ahmed@gmail.com",
    description="Universal Text Generator and Code Executor 2 in 1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="",
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
    python_requires='>=3.6',
)