Title: Bugzillator: From add-on builder to cfx
Tags: bugzillator, planet

I was introduced to the [add-on builder](https://builder.addons.mozilla.org/) by a [friend](https://twitter.com/awfurtado) a while ago. It's an incredibly easy way to get started writing Firefox add-ons. The online code editor combined with the [SDK](https://addons.mozilla.org/en-US/developers/docs/sdk/latest/dev-guide/index.html) allows you to instantly get an add-on running. It relieves you from having to worry about all the boilerplate and lets you focus on the code. It inspired me to write an add-on I had thought of some time back: the Bugzillator.

Sometimes I read blogs and mailing lists that contain bug references. Most of the time I just want to know the title of the bug for some extra context. When they don't have links, I have to copy the bug number to search in bugzilla. Bugzillator scans the DOM for bug numbers and adds links directly to bugzilla. Plus it adds a hover panel with some useful information on the bug.

##Getting started

There's no need to scan every single page visited, so I created a toolbar button to activate it. It was just a matter of using the builder [search tool](https://builder.addons.mozilla.org/search/) to find [code that did what I wanted](https://builder.addons.mozilla.org/package/167058/).

The code that looks for bug patterns has to run in content to have access to the DOM tree. To load the content script on demand I used the [tabs attach API](https://addons.mozilla.org/en-US/developers/docs/sdk/latest/modules/sdk/tabs.html#attach%28options%29):

    let worker = tabs.activeTab.attach({
        contentScriptFile: data.url("bugzillator.js")
    });

###Loading bug info

To get bug information I'm using [bz.js](https://github.com/harthur/bz.js) which is a JavaScript wrapper for [bugzilla's REST API](https://wiki.mozilla.org/Bugzilla:REST_API). To keep content script to a minimum it runs in add-on script and communicates using a [port](https://addons.mozilla.org/en-US/developers/docs/sdk/latest/dev-guide/guides/content-scripts/using-port.html). A `getBug` message from content gets the bug data and returns a `onBug` message with the info. On the add-on side we have:

    #!js
    worker.port.on("getBug", function (bugNumber) {
        bzClient.getBug(bugNumber, function (response) {
            if (response.status == 200) {
                let bug = response.json;
                worker.port.emit("onBug", bug);
            }
        });
    });

On the content side it's pretty simple too:

    #!js
    // Request bug info
    self.port.emit("getBug", bugNumber);

    // Receive bug info
    self.port.on("onBug", function(bug) {
        // Do stuff
    });

###Loading the CSS

The tabs attach API does not take a `contentStyleFile` property like [page-mod](https://addons.mozilla.org/en-US/developers/docs/sdk/latest/modules/sdk/page-mod.html). The simplest solution I found to load a separate CSS file in content was passing the file content as a message. On add-on script side you send the file contents:

    #!js
    worker.port.emit("onCss", data.load("bugzillator.css"));

Now you just add the CSS to the page in content side:

    #!js
    self.port.on("onCss", function(style) {
        let headStyle = document.createElement("style");
        headStyle.innerHTML = style;

        document.head.appendChild(headStyle);
    });

Simple and effective.

##Graduating from the builder

After some time playing with the add-on builder I got a [working prototype](https://builder.addons.mozilla.org/package/207471/latest/) that I was happy with. But I missed using [my favorite JavaScript editor](http://www.jetbrains.com/webstorm/) and wanted a similar workflow using it.

It was harder than I expected. The add-on builder site gives you 2 options for downloading your work: source code and xpi package. The xpi is the fully packaged add-on and contains a lot more than I cared for. The source code options only gives you a zip file with your code and the code for all dependencies. But how can you make changes and have the add-on reinstall itself like when using the builder?

On my first attempt I unpacked the xpi (it's just a zip file), found my code and made changes to it. Then I created a script to repackage everything into an xpi. Now I have the updated xpi but for Firefox to pick it up you have to manually install it every time. No go.

Looking a bit further I found the [cfx tool](https://addons.mozilla.org/en-US/developers/docs/sdk/latest/dev-guide/cfx-tool.html). The downloaded source code from the add-on builder gives you the package.json files that the cfx tool needs. The easiest way I found to get the tool working with the downloaded source was to create a `package` folder under the main add-on folder and move all dependencies into it. This way cfx was able to find all dependencies and worked fine without any extra command line parameters. The directory structure looks like this:

    Bugzillator
     |- data
     |   +- content loaded js, css, icon...
     |- lib
     |   +- main.js
     |- packages
     |   |- bugzillaclient
     |   |  |- lib
     |   |  |   +- module code
     |   |  +- package.json
     |   |- toolbarbutton-extended
     |   |  |- lib
     |   |  |   +- module code
     |   |  +- package.json
     |   +- other dependencies...
     +- package.json

With this setup running `cfx run` will start Firefox on a temporary profile with the current version of the add-on installed. That's almost good enough, I still had to manually load my html test file.

###Testing

While I was developing using the builder I created a very simple html file with some test cases. It would be neat if I could have a command to open Firefox, load the html and run bugzillator without me having to press buttons. The `cfx test` command does the trick.

I added my html test file to the add-on data folder and created a [cfx compatible unit test](https://addons.mozilla.org/en-US/developers/docs/sdk/latest/dev-guide/tutorials/unit-testing.html). Now running `cfx test` opens up Firefox, loads the html test file and runs bugzillator. It's not automated testing yet, but definitely better.

###Building the xpi.

There's a cfx command for that: `cfx xpi`. It packages everything and you won't need to worry about things like `install.rdf` and getting the directory structure right.

##Conclusion

Add-on builder is great, but I wish there was a clear path to graduation. Converting the downloaded source to use with cfx tool was trivial but required lots of trial and error and documentation surfing.

The code is available on [github](https://github.com/rodms10/bugzillator). I'm using the [issue tracker](https://github.com/rodms10/bugzillator/issues?state=open) for bugs and new features. Hope you find it useful.