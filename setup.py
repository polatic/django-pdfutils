# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='PDFutils',
    version='1.1.4',
    description='Django PDFutils',
    long_description=(read('README.rst')),
    author='Maxime Haineault',
    author_email='haineault@gmail.com',
    license='BSD',
    url='https://github.com/h3/django-pdfutils',
    packages=find_packages(),
    include_package_data=True,
    package_data={'pdfutils': [
        'README.rst',
        'changelog',
        ]},
    install_requires = [
        'django',
        'decorator<=3.9.9',
        'reportlab>=2.1',
        'html5lib',
        'httplib2',
        'pyPdf',
        'xhtml2pdf',
    ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
