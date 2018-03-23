# Callysto Sample Notebooks

A collection of sample notebooks to demonstrate what can be done with Jupyter notebooks in a variety of subject areas.

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Callysto Sample Notebooks](#callysto-sample-notebooks)
	- [Getting Started](#getting-started)
		- [Setting up GitHub](#setting-up-github)
		- [Downloading the Notebooks](#downloading-the-notebooks)
		- [Packages needed for demo notebooks](#packages-needed-for-demo-notebooks)
	- [Developing on hub.callysto.ca](#developing-on-hubcallystoca)
		- [Installing packages on hub.callysto.ca](#installing-packages-on-hubcallystoca)
		- [Setting up notebook specific git tools](#setting-up-notebook-specific-git-tools)
		- [Adding a developer key](#adding-a-developer-key)
	- [Running from Docker](#running-from-docker)
		- [Additional Packages](#additional-packages)
	- [About Folders in this Repo](#about-folders-in-this-repo)

<!-- /TOC -->

## Getting Started
The recommended way to run the sample notebooks is to use the JupyterHub set up for this project.
[hub.callysto.ca](https://hub.callysto.ca) is the environment teachers and students use to develop and use notebooks created as part of the Callysto project. As such, it should be ensured that any notebooks that are created work on hub.callysto.ca. One step to help do so is to develop directly on the hub.

### Setting up GitHub
Once logged in at [hub.callysto.ca](https://hub.callysto.ca), it is recommended to set up SSH authentication for interacting with Github. To do so, create a new private key on hub.callysto.ca and add the corresponding public key to your Github account as per the following instructions.

1. Using your github email, create the key using the following command and hitting enter when prompted.
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
Note that by default, the new key will overwrite any key stored in *.ssh/id_rsa*, so don't accept the default path unless you either have no key stored here or no longer need the original private key file.

2. Copy the contents of your public key. This is easiest done by opening a new Jupyter notebook and copying the output of the following (the notebook will make it easier to copy and paste the key)
```
!cat .ssh/id_rsa.pub
```
3. Add the public key to your github account at [github.com/settings/keys](https://github.com/settings/keys)  

NB: there are other options for interacting with Github as well. Please see the [section below](#adding-a-developer-key) for more information.


### Downloading the Notebooks
With your key set up as per the instructions above, you can download all the notebooks in this repo by opening a new terminal (under New --> Terminal) and cloning the repository.

```
git clone git@github.com:callysto/callysto-sample-notebooks.git
```

This will bring all the folders and notebooks into your hub environment.

### Packages needed for demo notebooks
In order to run the sample notebooks, certain additional packages need to be installed. This setup will help ensure most of the notebooks run, although certain libraries may still have to be installed (see next section). Whether or not they are included here depends on the frequency that they are used and how heavy- or light-weight they are.

Current additional packages to run the demo notebooks on hub.callysto.ca can be installed via
```
bin/callysto-setup
```

Following installation of these packages, you need to source your .bashrc file:  
`source ~/.bashrc`

## Developing on hub.callysto.ca
### Installing packages on hub.callysto.ca
In the case where certain libraries are not installed when running or developing notebooks, users may install packages in their userspace via:

```
pip install PACKAGE_NAME --user
```  
in a terminal session or  
```
!pip install PACKAGE_NAME --user
```
in a notebook code block.

When installing packages in the userspace, it should be noted which are added in order to subsequently have the package installed system-wide (if it is a commonly used package). Alternatively, the notebook or a setup file should be configured to automatically install the packages on a user by user basis.

### Setting up notebook specific git tools
Any github project, including this one, can be initialized with a filter to remove output blocks from checkins and give more readable git diffs by running  
`bin/git-nb-tools`  
in the root of the project (adjusting the path to the setup script if running from outside of this project).

To use the notebook specific git tools, you will also need to make sure there is a .gitattributes file in your project root with at least the following lines:

```
*.ipynb filter=nbstripout  
*.ipynb diff=jupyternotebook  
*.ipynb merge=jupyternotebook```

Note that this file should have been pulled automatically from this repository.

### Adding a developer key
It's smart to avoid using the same private SSH key on multiple machines, especially when you don't have full control of the environment on a machine. While you could use https authentication for github, which at least shouldn't leave anything on disk, there are [still safer methods](https://developer.github.com/v3/guides/managing-deploy-keys/).

If you're only accessing one repository on the server, the simplest and safest method is to use a [deploy key](https://github.com/cybera/callysto-sample-notebooks/settings/keys). You are only allowed to use a public key once as a deploy key, so if you need access to more than one repository, you need to use the slightly more complicated method of defining a "machine user", associating that user with the projects you need access to, and adding your newly generated key to that user's keys.

You can [create the new key](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/) with the following command and using your Github email address (accepting all defaults by hitting enter):

  ```bash
  ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
  ```

Note that by default, the new key will overwrite any key stored in *.ssh/id_rsa*, so don't accept the default path unless you either have no key stored here or no longer need the original private key file.

The "machine user" method allows you to limit access from the server with that key to only the repositories that it needs access to and is recommended if you can do it. A machine user has been set up already for Cybera employees.

Note that you can still set your git config settings to commit code as yourself. As long as the ssh key has access to the repository through *some* user, GitHub trusts whatever identity you give it as the committer.

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


## About Folders in this Repo

**lib**: Common code useful for all notebooks  
**notebooks**: Individual notebooks
