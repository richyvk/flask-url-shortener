# Flask url shortener

A simple URL shortener like tinyurl that I'm working on. Buoilt with Python and using the [Flask](http://flask.pocoo.org/docs/0.10/) webapp microframework.

Currently uses a pickled list of (url,unique_hash) tuples to sort previously shortened URL data.

May move to database for the storage at some point, but wanted it to start as simple as possible.