from fanstatic import Library, Resource, Group
from js.jquery import jquery

library = Library('bootstrap', 'resources')

bootstrap_grid_css = Resource(library, 'css/bootstrap-grid.css',
                              minified='css/bootstrap-grid.min.css')

bootstrap_reboot_css = Resource(library, 'css/bootstrap-reboot.css',
                                minified='css/bootstrap-reboot.min.css')

bootstrap_css = Resource(library, 'css/bootstrap.css',
                         minified='css/bootstrap.min.css')

bootstrap_bundle_js = Resource(library, 'js/bootstrap.bundle.js',
                               minified='js/bootstrap.bundle.min.js',
                               bottom=True,
                               depends=[jquery, ])

bootstrap_js = Resource(library, 'js/bootstrap.js',
                        minified='js/bootstrap.min.js',
                        bottom=True,
                        depends=[jquery, ])

bootstrap = Group([bootstrap_css, bootstrap_bundle_js])
