
Wiki-Dump Reader
================


.. image:: https://travis-ci.org/CyberZHG/wiki-dump-reader.svg
   :target: https://travis-ci.org/CyberZHG/wiki-dump-reader
   :alt: Travis


.. image:: https://coveralls.io/repos/github/CyberZHG/wiki-dump-reader/badge.svg?branch=master
   :target: https://coveralls.io/github/CyberZHG/wiki-dump-reader
   :alt: Coverage


Extract corpora from wiki-dump.

Install
-------

.. code-block:: bash

   pip install wiki-dump-reader

Usage
-----

The dump file ``*wiki-*-pages-articles.xml`` should be downloaded first. Then you can iterate and get cleaned text from the text:

.. code-block:: python

   from wiki_dump_reader import Cleaner, iterate

   cleaner = Cleaner()
   for title, text in iterate('*wiki-*-pages-articles.xml'):
       text = cleaner.clean_text(text)
       cleaned_text, links = cleaner.build_links(text)

Just ignore ``links`` if you don't need them:

.. code-block::

   cleaned_text, _ = cleaner.build_links(text)

See `examples <tests/targets>`_ for an intuitive feeling.
