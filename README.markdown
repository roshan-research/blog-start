## Getting Started

If you want to create a [pelican](http://getpelican.com) blog, which is ready for blogging in **Farsi**, you can use here as a starting point.

### What you will get

* A pelican blog.
* A good and minimal [persian theme](https://github.com/sobhe/pelican-sobhe).
* A [jalali plugin](https://github.com/sobhe/pelican-jalali) for persian dates.

### Short Version

#### 1. Clone this repository

`TODO`

### Long Version

#### prerequisites

* [Python 2.7](http://python.org/download/)
* [pip](http://www.pip-installer.org/en/latest/installing.html)

#### 1. Install Pelican and Markdown

`pip install pelican Markdown`

#### 2. Start a pelican project

`cd path/to/blog/`

Change your directory to a place you want to create you blog, then do:

`pelican-quickstart`

You can read more about how to kickstart a pelican blog [here](http://docs.getpelican.com/en/latest/getting_started.html#kickstart-your-site).

#### 3. Create a simple content

Go inside the content directory and create a test content.

```
cd content
touch test-post.md
```

Then fill it with something like:

    Title: یک بلاگ پست فارسی و امتحانی
    Slug: persian-test
    Date: 2013-05-16 17:16
    Tags: آزمایشی
    
    این یک تست است.

#### 4. Add the sobhe theme

The theme repo is: <https://github.com/sobhe/pelican-sobhe>

Clone this repository to the root of your blog.

```
cd path/to/blog/
git clone git@github.com:sobhe/pelican-sobhe.git
```

Then edit your blog config (`pelicanconf.py`) so it uses this theme.

Add this to the end of `pelicanconf.py`:

`THEME = 'pelican-sobhe'`

#### 5. Add the pelican-jalali plugin for persian dates

The plugin repo is: <https://github.com/sobhe/pelican-jalali>

Clone this repository recursively into your `PLUGIN_PATH`. If you have not set any `PLUGIN_PATH` yet, you must create one:

    cd path/to/blog/
    mkdir plugins
    cd plugins
    git clone --recursive git@github.com:sobhe/pelican-jalali.git

Make sure that you clone the plugin with **--recursive**, because it contains a submodule.

Now you need to edit your config and activate the plugin.

Add this to the end of `pelicanconf.py`:

    import os
    script_path = os.path.realpath(__file__)
    blog_base_path = os.path.dirname(script_path)
    
    PLUGIN_PATH = os.path.join(blog_base_path, 'plugins/')
    PLUGINS = ['pelican-jalali']

#### 6. Test that everything is working

You can test the blog you have created this way:

```
cd path/to/blog/
make html
```

If you see this output, eveything must be ok:

    Done: Processed 1 articles and 0 pages in 0.16 seconds.

To see the live demo:

```
make serve
```

Then open a browser and navigate to <http://localhost:8000/>. You must see something like:

![image](https://raw.github.com/sobhe/pelican-sobhe/gh-pages/screenshot/bare.png)

#### 7. Going forward

* make sure your config is right (edit `pelicanconf.py` and `publishcond.py`)
* add more content

