How to use?
===========

This should be setup before rendering a page. See `fanstatic`_ for more
information::

  >>> from fanstatic import init_needed
  >>> needed = init_needed(base_url='http://localhost')

You can import bootstrap from ``js.bootstrap4`` and ``.need`` it
where you want these resources to be included on a page::

  >>> from js.bootstrap4 import bootstrap, library
  >>> bootstrap.need()

Render the inclusion::

  >>> from fanstatic import Inclusion
  >>> i = Inclusion(needed)
  >>> print(i.render())
  <link rel="stylesheet" type="text/css" href="http://localhost/fanstatic/bootstrap/css/bootstrap.css" />
  <script type="text/javascript" src="http://localhost/fanstatic/jquery/jquery...js"></script>
  <script type="text/javascript" src="http://localhost/fanstatic/bootstrap/js/bootstrap.bundle.js"></script>

Bootstrap's CSS grid and the reset CSS (called Reboot) can be needed
separately as well, but they are already included when calling
``bootstrap.need()``:

  >>> import js.bootstrap4
  >>> js.bootstrap4.bootstrap_grid_css.need()
  >>> js.bootstrap4.bootstrap_reboot_css.need()

