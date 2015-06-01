#Rodms.com blog

Souce code for [my blog](http://blog.rodms.com) using [pelican](http://blog.getpelican.com/) static site generator.

NOTE: If you're using a mac, I recommend installing python using [Homebrew](http://brew.sh/), then add `export PYTHONPATH=/usr/local/lib/python2.7/site-packages` to your `.profile` file.

##installation
* [Instal pelican version 3.4](http://docs.getpelican.com/en/3.4.0/install.html) with `pip install pelican==3.4.0`
* Install markdown with `pip install Markdown`
* Install [pelican minify](https://github.com/rdegges/pelican-minify) with `pip install pelican-minify`
* Install [webassets](https://github.com/getpelican/pelican-plugins/tree/master/assets) with `pip install webassets`
* Install [cssmin](https://github.com/zacharyvoase/cssmin) with `pip install cssmin`
* Get submodules ([ghostly](https://github.com/rodms10/ghostly) and the published blog) by running `git submodule update --init --recursive`

##Running the blog

To build the blog run `make html`. This will generate the site in the `output` folder.

To run it locally, you can use `make serve` and connect to port 8000. Use `make devserver` and `make stopserver` to serve the site locally and update on every change.

`make publish` will generate the publishable site to `published` folder. To publish the blog commit and push the changes.

Run `make help` for all commands.