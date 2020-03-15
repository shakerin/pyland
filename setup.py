import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('LICENSE') as f:
    license = f.read()

setuptools.setup(
    name="pyland",
    version="0.0.1",
    author="Shakerin Ahmed",
    author_email="shakerin.ahmed@gmail.com",
    description="Universal Text Generator and Code Executor 2 in 1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="",
    license=license,
    packages=setuptools.find_packages(exclude=('tests', 'docs')),
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