from setuptools import find_packages
from setuptools import setup
import os


def read_file(name):
    with open(os.path.join(os.path.dirname(__file__), name)) as f:
        return f.read()


version = '1.4.dev0'
shortdesc = 'Slider Widget for YAFOWIL'
longdesc = '\n\n'.join([read_file(name) for name in [
    'README.rst',
    'CHANGES.rst',
    'LICENSE.rst'
]])
tests_require = ['yafowil[test]']


setup(
    name='yafowil.widget.slider',
    version=version,
    description=shortdesc,
    long_description=longdesc,
    classifiers=[
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='',
    author='BlueDynamics Alliance',
    author_email='dev@bluedynamics.com',
    url=u'http://pypi.python.org/pypi/yafowil.widget.slider',
    license='Simplified BSD',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['yafowil', 'yafowil.widget'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'yafowil>2.1.99',
    ],
    tests_require=tests_require,
    extras_require=dict(
        test=tests_require,
    ),
    test_suite="yafowil.widget.slider.tests",
    entry_points="""
    [yafowil.plugin]
    register = yafowil.widget.slider:register
    example = yafowil.widget.slider.example:get_example
    """
)
