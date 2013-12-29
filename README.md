#Rodms.com blog

Souce code for [my blog](http://blog.rodms.com) using [pelican](http://blog.getpelican.com/) static site generator.

#installation
* [Instal pelican](http://docs.getpelican.com/en/3.3.0/getting_started.html#installing-pelican)
* Install markdown with `pip install Markdown`
* Install [pelican minify](https://github.com/rdegges/pelican-minify) with `pip install pelican-minify`
* Install [webassets](https://github.com/getpelican/pelican-plugins/tree/master/assets) with `pip install webassets`
* Install [cssmin](https://github.com/zacharyvoase/cssmin) with `pip install cssmin`
* Get submodules ([ghostly](https://github.com/rodms10/ghostly) and the published blog) by running `git submodule update --init --recursive`

If you're using a mac you may need to add `export PYTHONPATH=/usr/local/lib/python2.7/site-packages` to your `.profile` file.
