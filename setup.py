from setuptools import setup


def readme():
    with open("README.rst") as readme_file:
        return readme_file.read()


configuration = {
    "name": "pynndescentSC",
    "version": "0.0.1",
    "description": "Nearest Neighbor Descent for Sparse Clustering",
    "long_description": readme(),
    "classifiers": [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved",
        "Programming Language :: C",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    "keywords": "sparse clustering, nearest neighbor, knn, ANN",
    "url": "http://github.com/bobermayer/pynndescentSC",
    "author": "Leland McInnes / Benedikt Obermayer",
    "author_email": "leland.mcinnes@gmail.com / benedikt.obermayer@bih-charite.de",
    "maintainer": "Leland McInnes / Benedikt Obermayer",
    "maintainer_email": "leland.mcinnes@gmail.com / benedikt.obermayer@bih-charite.de",
    "license": "BSD",
    "packages": ["pynndescentSC"],
    "install_requires": [
        "scikit-learn >= 0.18",
        "scipy >= 1.0",
        "numba >= 0.51.2",
        "llvmlite >= 0.30",
        "joblib >= 0.11",
        'importlib-metadata >= 4.8.1; python_version < "3.8"',
    ],
    "ext_modules": [],
    "cmdclass": {},
    "test_suite": "nose.collector",
    "tests_require": ["nose"],
    "data_files": (),
    "zip_safe": False,
}

setup(**configuration)
