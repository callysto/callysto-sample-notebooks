# Callysto Sample Notebooks

A collection of sample notebooks to demonstrate what can be done with Jupyter notebooks in a variety of subject areas.

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

## hub.callysto.ca

Ideally, we want to make sure these notebooks work on the main hub, [hub.callysto.ca](https://hub.callysto.ca) as soon as possible. Here are some tips for working directly on the hub.

1. Python packages can be installed in userspace via either `pip install PACKAGE_NAME --user` in a terminal session or `!pip install PACKAGE_NAME --user` in a notebook code block.

2. You can avoid having to type your main github account password or store your main private SSH key on the server by generating a new private key and having someone with admin access to the *callysto-sample-notebooks* project add the public part of it to the deploy keys for the project. You can create the new key with the following command (accepting all defaults by hitting enter):

  ```bash
  ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
  ```

  [Here's more documentation](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/) on that. And [here's where an admin can add a deploy key](https://github.com/cybera/callysto-sample-notebooks/settings/keys). Note that by default, the new key will overwrite any key stored in *.ssh/id_rsa*, so don't accept the default path unless you either have no key stored here or no longer need the original private key file.

3. Current additional packages needed on hub.callysto.ca can be installed via `bin/callysto-setup`. Any github project, including this one, can be initialized with a filter to remove output blocks from checkins and give more readable git diffs by running `bin/git-nb-tools` in the root of the project (adjusting the path to the setup script if running from outside of this project).

4. To use the notebook specific git tools, you will also need to make sure there's a `.gitattributes` file in your project root with at least the following lines:

  ```
  *.ipynb filter=nbstripout
  *.ipynb diff=jupyternotebook
  *.ipynb merge=jupyternotebook
  ```
