# Atom-shell-branding #

Builds a branded Atom-shell launcher from GIT in a simple way, including icons and other resources.


## Why? ##

In the Atom-shell [docs](https://github.com/atom/atom-shell/blob/master/docs/tutorial/application-distribution.md), it is mentioned that a full rebrand implies the compilation of atom-shell from source.

There is a [grunt task](https://github.com/paulcbetts/grunt-build-atom-shell) that allows us to handle this automatically. However, it doesn't support the branding of icons or other resources. On the other hand [atom-shell-starter](https://github.com/atom/atom-shell-starter) is a little bit more advanced, but too complex and seems to force you to use coffescript files.

Atom-shell-branding just follows the documentation to build a simple rebranded atom-shell.


## Usage ##

Open 'build.py' in a text editor and set the following parameters as you want:

    # == Parameters (edit these) == #

    configuration = 'Release'  # Release / Debug
    project_name = 'myapp'
    product_name = 'MyApp'

If you need to change resource files, such as icons, use the 'resources' folder. In most cases, you will only want to change the icon files.

Execute the python script with 'python build.py'. If everything worked fine, your rebranded atom-shell application will be in 'atom-shell/out/Release/' (or 'atom-shell/out/Debug/', depending on the configuration).

For compilation errors, refer to the [atom-shell documentation](https://github.com/atom/atom-shell/tree/master/docs). This script assumes that you have a development machine with the prerequisites for your OS as mentioned in the documents.


## Architecture ##

Atom-shell-branding is a very simple python file which does the following:

1. Downloads atom-shell from git and places it in 'atom-shell' directory.
2. Bootstraps atom-shell with the branded project and product names.
3. Replaces the atom-shell resources folder with the branded resources.
4. Builds the branded atom-shell.
5. Done!


## Support ##

Atom-shell-branding works fine in OSX Mavericks. I still have not tested it in Windows or Linux, but will eventually. Send me a pull-request if you find that something is not working, or open an Issue.
