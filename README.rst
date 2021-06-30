mwdata.science
==============

This is the repository for maintaining our website.

Local development
-----------------

This website is developed with 2 components:

* `Hugo (a static site generator) <https://gohugo.io/>`__ for the main website
* `Django (a web framework) <https://www.djangoproject.com/>`__ for registration and database backend. This part lives separately in ``django_site/``

Development guide
-----------------

This guide is quite bad currently and we know. Please reach out if you are interested in developing something for the website.

To download and install Hugo on Ubuntu/Debian, use the following commands::

  HUGO_VERSION="0.69.2"
  wget -O hugo.deb https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.deb
  sudo apt install ./hugo.deb

You can install and run Hugo on other systems, too, see their `list of releases <https://github.com/gohugoio/hugo/releases/download/>`__

After installing Hugo, you can view the site on your local laptop, by running the command ``hugo server`` directly in the root folder of this repository.
