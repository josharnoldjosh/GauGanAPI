# GauGanAPI

## Description

A light-weight API for bulk processing images to [Nvidia GauGan](http://nvidia-research-mingyuliu.com/gaugan/).

## Installation

### Environment

You first need to install the requirements. Run:

`pip3 install -r requirements.txt`

Or, optionally, create your own virtual environment by:

```python
git clone https://github.com/josharnoldjosh/GauGanAPI.git
cd GauGanAPI
pip3 install virtualenv
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

### Chrome Driver

1. You must have Google Chrome installed.

2. You have to check your Google Chrome version by doing `Chrome > About Google Chrome`. You can see in the image below I am running Google Chrome version 80. If you're on a terminal, you'll have to google another way to figure out your chrome version.

![alt text](https://i.ibb.co/qWv2S3c/Screen-Shot-2020-03-31-at-10-58-12-AM.png)

3. The last step is you need the `chromedriver` for your version of Google Chrome. Jump to [chromedriver downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads) and download whatever version of chrome driver that corresponds to your version of Google Chrome. For me, I would download version 80. Lastly, unzip the downloaded folder and put "chromedriver" in the root of this Github folder.

![alt text](https://i.ibb.co/9yP4nyT/Screen-Shot-2020-03-31-at-11-02-37-AM.png)

## Running the code

### Where to put your files

All you have to do is place any folders or files under `input/`. The code uses `glob`, so you don't have to worry about "flattening" your input folders, as long as each image has a unique name, it doesn't matter how many folders are within your `input/` folder. So, for example, both `input/<my images>` would work and also `input/another_folder/<my images>`.

### The API

The function below initalizes the API. `use_display` is specific to Linux, if you use Linux, you want to try to set this to `True`. If you run into any issues, you could try setting it to `False` and seeing if it works. `headless` determines whether or not you want to "see" the web browser pop up when you run the code. Most of the time, you probably won't so I'd recommend setting it to `True` to hide the web browser. `width` and `height` determines the size of your webbrowser, the following values `1920` and `1080` should be fine.

```python
upload = Upload(use_display=False, headless=True, width=1920, height=1080)
```

The function below actually handles uploading all the files. `file_types` is an array that uses enums. Simply pass in `FileType.png` for `png` input files, and `FileType.jpg` for `jpg` input files, or both if you want both file types to be uploaded. `sleep_interval` is pretty important, if it is too small, the API may not have time to load and you won't get any output files. I have found `1` works fine, but if you run into any issues, try to increase it. It should take ~`2 * sleep_interval` to process one image.

```python
upload.all(file_types=[FileType.png, FileType.jpg], sleep_interval=1)
```

### Example

Check out `example.py` for an example implementation!