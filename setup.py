from setuptools import setup, find_packages
import os

version = '4.0.0'


def read(*rnames):
    """Read a file."""
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


long_description = "\n\n".join([
    read('README.rst'),
    read('js', 'bootstrap4', 'test_bootstrap.rst'),
    read('CHANGES.rst'),
])


setup(
    name='js.bootstrap4',
    version=version,
    description="fanstatic twitter bootstrap.",
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: JavaScript',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Zope',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: Widget Sets',
    ],
    keywords='fanstatic twitter bootstrap',
    author='RedTurtle Developers',
    author_email='sviluppoplone@redturtle.it',
    maintainer='gocept developers',
    maintainer_email='mail@gocept.com',
    url='https://github.com/gocept/js.bootstrap4',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic >= 1.0a3',
        'js.jquery >= 1.9.1',
        'setuptools',
    ],
    entry_points={
        'fanstatic.libraries': [
            'bootstrap4 = js.bootstrap4:library',
        ],
    },
)
