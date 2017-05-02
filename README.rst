=============================
pyoasis
=============================

{{cookiecutter.description}}

.. image:: https://readthedocs.org/projects/pyoasis/badge/?version=latest
  :target: https://readthedocs.org/projects/pyoasis/?badge=latest
.. image:: https://travis-ci.org/ScottWales/pyoasis.svg?branch=master
  :target: https://travis-ci.org/ScottWales/pyoasis
.. image:: https://circleci.com/gh/ScottWales/pyoasis.svg?style=shield
  :target: https://circleci.com/gh/ScottWales/pyoasis
.. image:: http://codecov.io/github/ScottWales/pyoasis/coverage.svg?branch=master
  :target: http://codecov.io/github/ScottWales/pyoasis?branch=master
.. image:: https://landscape.io/github/ScottWales/pyoasis/master/landscape.svg?style=flat
  :target: https://landscape.io/github/ScottWales/pyoasis/master
.. image:: https://codeclimate.com/github/ScottWales/pyoasis/badges/gpa.svg
  :target: https://codeclimate.com/github/ScottWales/pyoasis
.. image:: https://badge.fury.io/py/pyoasis.svg
  :target: https://pypi.python.org/pypi/pyoasis

.. content-marker-for-sphinx

-------
Install
-------

---
Use
---

-------
Develop
-------

Development install::

    git checkout https://github.com/ScottWales/pyoasis
    cd pyoasis
    source raijin.env
    pip install -e '.[dev]'

Run tests::

    cd test
    mpirun -n 1 test_oasis.py

Build documentation::

    sphinx-apidoc -o doc/api oasis
    make -C doc html

Upload documentation::

    git subtree push --prefix docs/_build/html/ origin gh-pages
