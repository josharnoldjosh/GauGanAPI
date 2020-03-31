from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
from enum import Enum
from glob import glob
import os
import base64
from PIL import Image
from io import BytesIO

class FileType(Enum):
    png = 1
    jpg = 2

class Upload:

    def __init__(self, use_display=False, headless=True, width=1920, height=1080):
        if use_display:
            self.display = Display(visible=0, size=(4000, 2500))  
            self.display.start()
        self.chrome_options = Options()
        self.chrome_options.add_argument(f"--window-size={width},{height}")
        if headless:
            self.chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path='./chromedriver', options=self.chrome_options)                        
        self.driver.get("http://34.216.122.111/gaugan/")
        self.driver.find_element_by_id("myCheck").click()

        if not os.path.exists("input/"): os.mkdir('input/')
        if not os.path.exists("output/"): os.mkdir('output/')

    def all(self, file_types=[FileType.png, FileType.jpg], sleep_interval=1):
        input_file_paths = self.get_input_file_paths(file_types)
        for input_path in input_file_paths:
            self.upload_single_file(input_path)
            sleep(sleep_interval)
            self.download_output(input_path)
            sleep(sleep_interval)
        self.close()

    def get_input_file_paths(self, file_types=[FileType.png, FileType.jpg]):
        result = []        
        input_path = os.path.join(os.getcwd(), 'input/')
        if FileType.png in file_types:
            result.extend(glob(f"{input_path}*.png"))
        if FileType.jpg in file_types:
            result.extend(glob(f"{input_path}*.jpg"))
        return result

    def upload_single_file(self, input_path):
        self.driver.find_element_by_id('segmapfile').send_keys(input_path)
        self.driver.find_element_by_id('btnSegmapLoad').click()        
        self.driver.find_element_by_id("render").click()

    def download_output(self, input_path):
        output_path = input_path.replace("/input/", "/output/")
        canvas = self.driver.find_element_by_id('output')
        canvas_base64 = self.driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)        
        self.canvas_png = base64.b64decode(canvas_base64)
        with open(output_path, 'wb') as f: f.write(self.canvas_png)

    def image_data(self):                    
        image = Image.open(BytesIO(self.canvas_png))
        buffered = BytesIO()
        image.save(buffered, format="png")                
        return 'data:image/png;base64,'+base64.b64encode(buffered.getvalue()).decode('ascii')    

    def close(self):
        self.driver.close()