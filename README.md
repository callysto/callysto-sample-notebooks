# Callysto Sample Notebooks

A collection of sample notebooks to demonstrate what can be done with Jupyter notebooks in a variety of subject areas.

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Callysto Sample Notebooks](#callysto-sample-notebooks)
	- [Folders](#folders)
	- [Running from Docker](#running-from-docker)
		- [Additional Packages](#additional-packages)
	- [Running on hub.callysto.ca](#running-on-hubcallystoca)
		- [Installing packages on hub.callysto.ca](#installing-packages-on-hubcallystoca)
		- [Packages needed for demo notebooks](#packages-needed-for-demo-notebooks)
		- [Using git on hub.callysto.ca](#using-git-on-hubcallystoca)
			- [Adding a developer key](#adding-a-developer-key)
			- [Setting up notebook specific git tools](#setting-up-notebook-specific-git-tools)

<!-- /TOC -->

## Folders

**lib**: Common code useful for all notebooks  
**notebooks**: Individual notebooks

## Running from Docker

This repository provides a completely encapsulated development environment via [Docker](https://www.docker.com). You can download Docker for your operating system [here](https://www.docker.com/community-edition).

To build the image you'll be running (based off of Continuum Analytics' Anaconda image), simply run:

```bash
bin/build
```

Once this has finished, running:

```bash
bin/notebook
```

will start up the Docker container and run `jupyter notebook` within it. Any files in your project folder will be accessible under `/opt/callysto` within the Docker container.

If you need to troubleshoot issues with package installations or other setup, sometimes it's easiest to just start up in a shell, which you can do via:

```bash
bin/bash
```

From this entry point, you can run your notebook via:

```bash
/opt/conda/bin/jupyter notebook --notebook-dir=/opt/callysto \
  --ip='*' --port=8888 --no-browser --allow-root \
  --NotebookApp.token=''
```

This is the same command that `bin/notebook` runs by default.

### Additional Packages

Once you have figured out what packages you need, you can add them to the appropriate line in the `Dockerfile`, or you can add a new `RUN` line if you just want to use cached versions of the previous steps.

## Running on hub.callysto.ca

[hub.callysto.ca](https://hub.callysto.ca) is the environment teachers and students use to develop and use notebooks created as part of the Callysto project. As such, it should be ensured that any notebooks that are created work on hub.callysto.ca. One step to help do so is to develop directly on the hub. Here are some tips for working directly on the hub.

### Installing packages on hub.callysto.ca
Python packages can be installed in userspace via either  
```
pip install PACKAGE_NAME --user
```  
in a terminal session or  
```
!pip install PACKAGE_NAME --user
```
in a notebook code block.

When installing packages in the userspace, it should be noted which are added in order to subsequently have the package installed system-wide (if it is a commonly used package). Alternatively, the notebook or a setup file should be configured to automatically install the packages on a user by user basis.

### Packages needed for demo notebooks
Current additional packages to run the demo notebooks on hub.callysto.ca can be installed via `bin/callysto-setup`.

Following installation of these packages, be sure to source your .bashrc file:  
`source ~/.bashrc`

### Using git on hub.callysto.ca
#### Adding a developer key
You can avoid having to type your main github account password or store your main private SSH key on the server by generating a new private key and having someone with admin access to the *callysto-sample-notebooks* project add the public part of it to the deploy keys for the project. You can create the new key with the following command and using your Github email address (accepting all defaults by hitting enter):

  ```bash
  ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
  ```

[Here's more documentation](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/) on that. And [here's where an admin can add a deploy key](https://github.com/cybera/callysto-sample-notebooks/settings/keys). Note that by default, the new key will overwrite any key stored in *.ssh/id_rsa*, so don't accept the default path unless you either have no key stored here or no longer need the original private key file.

#### Setting up notebook specific git tools
Any github project, including this one, can be initialized with a filter to remove output blocks from checkins and give more readable git diffs by running  
`bin/git-nb-tools`  
in the root of the project (adjusting the path to the setup script if running from outside of this project).

To use the notebook specific git tools, you will also need to make sure there is a .gitattributes file in your project root with at least the following lines:

```
*.ipynb filter=nbstripout  
*.ipynb diff=jupyternotebook  
*.ipynb merge=jupyternotebook```

Note that this file should have been pulled automatically from this repository.
