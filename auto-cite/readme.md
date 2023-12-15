## Build Citations Locally
Normally your citations are built automatically on GitHub if you're using one of the standard workflows. But if you want to preview changes to your citations before pushing them to your GitHub repo for all to see, or GitHub is having problems generating the citations, you can follow these steps to run the automatic citation process on your computer. Most people wont need or want to do this.

- Install Python (with PIP).
- Go to the folder where you cloned your site, e.g. cd your-lab-website.
- Install needed Python packages by running `python -m pip install --upgrade --requirement ./auto-cite/requirements.txt`.
- Add or change the desired sources/papers in `/_data/sources.yaml`.
- Generate citations by running python `./auto-cite/auto-cite.py`.
Citations should be automatically generated and output to `/_data/citations.yaml`.