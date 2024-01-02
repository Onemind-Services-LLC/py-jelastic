from setuptools import setup, find_packages

# Get the long description from the README file
with open("README.md") as f:
    long_description = f.read()

setup(
    name="py-jelastic",
    version="0.1.2-dev",
    description="Jelastic API client library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Onemind-Services-LLC/py-jelastic",
    author="Abhimanyu Saharan",
    author_email="asaharan@onemindservices.com",
    license="Apache2",
    include_package_data=True,
    use_scm_version=True,
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        "requests",
    ],
    zip_safe=False,
    keywords=["jelastic", "api", "client"],
    classifiers=[
        "Intended Audience :: Developers",
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
