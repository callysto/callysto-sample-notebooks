# Callysto Sample Notebooks

A collection of sample notebooks to demonstrate what can be done with Jupyter notebooks in a variety of subject areas.

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Callysto Sample Notebooks](#callysto-sample-notebooks)
	- [Getting Started](#getting-started)
		- [Downloading the Notebooks](#downloading-the-notebooks)
		- [Packages needed for demo notebooks](#packages-needed-for-demo-notebooks)
	- [Running from Docker](#running-from-docker)
		- [Additional Packages](#additional-packages)
	- [About Folders in this Repo](#about-folders-in-this-repo)

<!-- /TOC -->

## Getting Started
The easiest way to run these sample notebooks is to run them on the JupyterHub set up for the Callysto project. The hub is available at [hub.callysto.ca](https://hub.callysto.ca) and simply requires a Google account to log in. Alternatively, if you have Jupyter set up locally, you can also run these sample notebooks there or use the Docker setup instructions provided below.

### Downloading the Notebooks
Once logged in at [hub.callysto.ca](https://hub.callysto.ca), you can download all the notebooks in this repo by opening a new terminal (under New --> Terminal) and cloning the repository.

```
git clone https://github.com/callysto/callysto-sample-notebooks.git
```

This will bring all the folders and notebooks into your hub environment.

### Packages needed for demo notebooks
In order to run the sample notebooks, certain additional packages need to be installed. This setup will help ensure most of the notebooks run, although certain libraries may still have to be installed (see next section). Whether or not they are included here depends on the frequency that they are used and how heavy- or light-weight they are.

Current additional packages to run the demo notebooks on hub.callysto.ca can be installed via (run in a terminal as above)
```
bin/callysto-setup
```

Following installation of these packages, you need to source your .bashrc file:  
`source ~/.bashrc`

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
