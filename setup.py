from setuptools import find_packages, setup

# Set version_info[__version__], while avoiding importing numpy, in case numpy
# and vg are being installed concurrently.
# https://packaging.python.org/guides/single-sourcing-package-version/
version_info = {}
exec(open("vg/package_version.py").read(), version_info)

# https://github.com/lace/vg/issues/72
readme = open("README.md", "rb").read().decode("utf-8")
install_requires = ["numpy"]

setup(
    name="vg",
    version=version_info["__version__"],
    description="A vector-geometry toolbelt for dealing with 3D points and vectors",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Metabolize, Body Labs, and other contributors",
    author_email="github@paulmelnikow.com",
    url="https://github.com/lace/vg",
    project_urls={
        "Issue Tracker": "https://github.com/lace/vg/issues",
        "Documentation": "https://vgpy.readthedocs.io/en/stable/",
    },
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Manufacturing",
        "Topic :: Artistic Software",
        "Topic :: Multimedia :: Graphics :: 3D Modeling",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Visualization",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)
