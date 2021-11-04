import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

# Packages that MovingPandas uses explicitly:
INSTALL_REQUIRES = ['numpy', 'matplotlib', 'pandas']

setuptools.setup(
    name="zrod.io",
    version="0.0.1",
    author="Walter Phillips",
    author_email="walter@3dwellbore.com",
    description="Demo for the zrod.io API",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/wansco/zrod.io",
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
    install_requires=INSTALL_REQUIRES
)
