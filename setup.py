from setuptools import setup

try:
    with open("Readme.md", "r") as fh:
        long_description = fh.read()
except:
    # When using tox, this is no longer going
    # to work properly. For this, just add a
    # dummy description ...
    long_description = "some long description"

setup(
    name='scikit-pk',
    version='0.0.1',
    author="Kenneth Leung",
    author_email="kenneth.leung@holmusk.com",
    description='Say Hello!',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sankhaMukherjee/scikit-pk",
    py_modules=['scikit-pk'],
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

