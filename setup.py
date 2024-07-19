from setuptools import setup, find_packages
try:
    from setuptools import convert_path
except ImportError:
    print("convert_path is not available in your setuptools version. Please update setuptools or use an alternative function.")
    convert_path = lambda x: x  # Fallback function

# Use convert_path in your setup script
here = convert_path(__file__)
long_description = open(convert_path('README.md')).read()

setup(
    name="setuptools",
    version="71.0.3",
    description="A sample Python package",
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
