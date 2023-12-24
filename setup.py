from setuptools import setup, find_packages

setup(
    name="py-jelastic",
    version="0.0.2",
    description="Jelastic API client library",
    url="https://github.com/Onemind-Services-LLC/py-jelastic",
    author="Abhimanyu Saharan",
    author_email="asaharan@onemindservices.com",
    license="Apache2",
    include_package_data=True,
    use_scm_version=True,
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        "requests",
        "httpx",
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
