# scikit-pk

One Paragraph of project description goes here

## Prerequisites

You will need to have a valid Python installation on your system. This has been tested with Python 3.6. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Package Installation

This is the repository is meant to be used for installing the scikit-pk package. A wheel dstribution of this package is present in the [`dist`](../master/dist) folder and may be installed within your virtual enviroonment as. 

`pip3 install https://github.com/sankhaMukherjee/scikit-pk/blob/master/dist/<package name>.whl`

This has been built upon a Unix system. If you use this for other systems, you may wish to consider building this library from source.

### Package Building

You may wish to make customize this package for your own use. For that, you need to build the system:

 - Clone this repo to your computer
 - Install a virtual enviromnent, and istall the required packages
 - Buid the system

 A `Makefile` has been provided for aiding with this process. The following commands should allow you do do the following

  - `make grantPermission`: grants execute permission to all shell scripts in the [`bin`](../master/bin) folder
  - `make clean`

## Contributing

Please send in a pull request.

## Authors

Kenneth Leung - Initial work (2020)

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details

## Acknowledgments

 - Hat tip to anyone who's code was used
 - Inspiration
 - etc.
 