---
layout: portfolio_entry
title: Why Jekyll Rocks
og_image: images/jekyll.png
category: Projects
---


<hr>


Some of you out there probably know a little bit about web development and the various frameworks that are available out there. Some of you may be clever enough to realise that this *very* site is designed with a static site generator developed with Ruby called “Jekyll”. I just thought I might take a moment to go over why I chose to use this fancy little tool as opposed to blowing you all away with my mad server-side coding skills.

---

**1. It’s simple**
There is no need for super complex bells and whistles when it comes to an online blog or what have you. If I were starting my own Amazon, maybe I might require some database and dynamic server-side scripting, but if I’m honest with myself, I’m not going to be that successful. At least not straight away.

No, we start out small and easy. Jekyll is great for that. You give it your content and it renders it into pages for you based on templates you specify.

**2. It’s fast**
This is pretty much a no-brainer. No server-side scripting means no server-side work. No work means much faster load times. That’s not to say there is no logic implemented here though. Jekyll comes out of the box with the ability to read a language called [Liquid](https://shopify.github.io/liquid/). Not super flexible but gets the small jobs done nicely. I especially like how you can specify parameters at the beginning of your markdown sheets and use them in your templates as variables essentially.

It's cool.

**3. Blog integration**
So you don’t need to mess about trying to get your blog to work, Jekyll does all the heavy lifting. As I touched on before, it can read markdown files and render them into readable blog posts. Pretty neat, so much so that I had to use that lame expression. 

So you can just hop onto an md editor like [Dilinger](https://dillinger.io/) like I am right now or design your own md editor and get stuck into it. I made my own but found Dillinger to be pretty effective. Look up a markdown cheat sheet like [this one](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) to make the whole process easier, but diving in blind worked fine for me to start with.

**4. GitHub integration**
GitHub is compatible with Jekyll which is awesome. You just tweak a few settings and you can update your site with some simple pushing and pulling as you would any other repo. This is great for me because it meant simply buying a domain name off some cheap company and directing it to my repo. So all I do now when I want to tweak the site is load up Ubuntu as a Virtual Machine (running windows, I like overwatch) and run the `jekyll serve` command in the terminal and I'm away to the races. Push my work and within seconds, the site is up to date and behaving exactly as it should.

If you're just wanting to post a blog post, you can simply login to your GitHub account, navigate to the `_posts/` directory and drag your md files that you produced with an online tool into the folder. It will automatically appear shortly. Particularly useful when inspiration comes out on the farm or on your jet ski or whatever.

**4. It’s delightful**
Jekyll is a gem (pun intended). It takes something that should be simple and *keeps* it that way. There are themes available and its pretty easy to tweak them provided you know some simple concepts of web development. This has been greatly useful to me for learning these concepts.

---

So do yourselves a favour and use Jekyll for something. Or don't, I don't really mind.
