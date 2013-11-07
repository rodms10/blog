Title: Blogging on blogging
Tags: blog, pelican

The idea of starting a blog has been on the back burner for a while. Now, working on open source, I can safely write about my work publicly. With one less excuse out of the way it was time start one.

But which of the hundreds of blogging platforms to use?

I learned about [ghost](https://ghost.org/) while it still was a [kickstarter project](http://www.kickstarter.com/projects/johnonolan/ghost-just-a-blogging-platform). I loved it! It's a simple open source blogging platform written in [node.js](http://nodejs.org/). It was overfunded and it's now out. I installed it locally and started playing with it. The default generated blog is gorgeous and it's really easy to use. It even has an inline [Markdown](http://daringfireball.net/projects/markdown/) editor with live preview. We have a first contender.

I plan to add my blog to [planet mozilla](http://planet.mozilla.org/). But I'm sure subscribers will not appreciate posts about [aliens invading earth](http://www.history.com/shows/ancient-aliens) to harvest gold or the weather in Seattle (spoiler alert - it rains a lot). OK, I promise I'll not write about aliens. But anyway I need a way to create a separate feed for posts I wanted to include in planet mozilla. This is when Ghost starts to show it's infancy. It supports tags but doesn't generate feeds based on tags. It also doesn't support code highlighting yet, which is important as I plan to make this blog mostly technical. Of course being open source I could implement those features myself, but I've postponed starting the blog for long enough.

With ghost ruled out I started looking into static site generators. They have the big advantage of being easier to host. I looked into [hexo](http://zespia.tw/hexo/), [jekyll](http://jekyllrb.com/) and [octopress](http://octopress.org/). But the decision was made when I bumped into [Paul McLanahan's](http://pmac.io) blog, a fellow mozillian. His blog had the feeds per tags that I was looking for plus it lists the posts with a summary on the homepage. Pretty neat. His site uses [pelican](http://getpelican.com/) so I started looking into it. It's written in python, a plus since it's a very friendly language that I just started learning. It's extensible and already has many [plugins](https://github.com/getpelican/pelican-plugins) and [themes](https://github.com/getpelican/pelican-themes). The search for the blogging platform was over. Pelican it is.

I really liked ghost's beautiful design, so I decided to create a pelican theme based on ghost's design. This is what you're looking at. I started from ghost's CSS and did some adjustments to it. Hope you like it. The code for the theme is available [here](https://github.com/rodms10/ghostly).
