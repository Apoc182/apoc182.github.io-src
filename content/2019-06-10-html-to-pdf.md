---
layout: portfolio_entry
title: Pure Python HTML to PDF
og_image: images/pdf.png
category: Career
subtitle: When anything less than purity will not do.

---

[Image credit](https://www.microsoft.com/en-us/p/excellent-pdf-reader/)

Hello again! Welcome to another Monday and another short one for you here.

So, have you ever needed to make a PDF file programmatically? I know I have. One of the main advantages of having a pdf as opposed to some other graphical format is being able to print them from the right click (context) menu.

The simplest method of programmatically styling something like this in my experience seems to be HTML. Once you have this, simply use some kind of library to convert it into a PDF. Right? Well, kind of.

You see, another nuance to this thing here is that generally speaking, you want your applications to be independent of the OS and environment. Well, you might wanna have Python and a couple of packages installed, but that’s it. Let’s not rely on the user to install anything external.

Let me introduce [xhtml2pdf](https://pypi.org/project/xhtml2pdf/)

As I was unable to find any clear cut instructions on how to do this locally, so let me save you some trouble and walk you through it.

```python
from xhtml2pdf import pisa
from jinja2 import Environment, FileSystemLoader
```

First, let's import the pisa module from the xhtml2pdf package. Optionally, you can import the Environment and FileSystemLoader modules from [jinja2]([http://jinja.pocoo.org/](http://jinja.pocoo.org/)) if you would like to populate a html template with some data. Then, provided you want to use Jinja2…

```python
environment = Environment(loader=FileSystemLoader(searchpath="./"))
template = environment.get_template('./Template.html')
```

We create an environment specifying we want to load from the filesystem and that the place to load from is the current directory.

```python
output_from_parsed_template = template.render(**kwargs)
```

Above, we are grabbing the properly formatted jinja template (with {{ variables }} and the like), and populating it with data. If you want to know more about that, google it. It's not the focus of what I'm talking about here.

```python
resultFile = open(outputFilename, "w+b")

pisaStatus = pisa.CreatePDF(output_from_parsed_template, dest="./output_pdf")

resultFile.close()

```

In the above, we open some kind of output file for writing as binary. Then, we use the CreatePDF function from pisa to do the magic. Pure, pythonic conversion. Then of course, we tidy up and close the file.



That's all there is too it folks! Hope that was helpful to someone! See ya'll next week :)
