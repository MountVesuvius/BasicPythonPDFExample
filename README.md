# Basic Python PDF Example

This will generate a very simple pdf based dynamically based on the content that you provide to it. Probably won't be a drag and drop for your project, but should be enough to make some basic invoices.

Here is the link to the documentation: (user guide)[https://www.reportlab.com/docs/reportlab-userguide.pdf]

## Running the project
### Prelude Virtualenv
If you aren't using virtualenv that is fine you can skip this step, however I recommend you always use virtualenv. 
1. `pip3 install virtualenv` to install
2. `virtualenv venv` to create a new virtualenv of name `venv`

### Setup
1. `pip3 install -r requirements.txt` will install the required libraries to use the example
2. `python3 main.py` will create `invoice.pdf` automatically

The code is decently straight forward, and I've tried to put some comments in to explain what is going on. If there is something specific you need, probably smart to check the documentation as it will know more than me. You can use this library as it has an open source license that will cover you for this school project so don't worry about anything you see regarding licensing for this library.

If you need to do more templating style stuff from memory there is a way to setup Jinja2 with HTML to create templates you can convert but it's a little annoying. We can look at it if you really need it, but try this for now.
