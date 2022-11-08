# PowerStrip 
Ongoing Project on sentiment analysis...

About:<br>
<b>POWER STRIP</b> is a tool used to analyze music, audio messages, textual content etc by harnessing NLP algorithms, providing a wide range of applications in music industry, social media, stock and crypto market and other related fields for enhancing user experience. <br>

<img src="images/Audio-Waveforms-Featued-Image.jpg">

<b>Instructions</b>:<br>

Step 1:
Clone this repo <br>


Step 2:
If you are running for the first time, Run these commands on terminal. Make sure that you are on the parent directory  <br>

-- Process 1: Downloading necessary libraries 
   
    python -m nltk.downloader all
-- Process 2: Adding scripts path to sys.path list    
    
    conda develop $(pwd)/scripts
-- Process 3: Install all the requirements
      
      pip install -r requirements.txt
Step 3:
File to be executed for running Flask App: <b>flaskapp/app.py</b> <br>

Execution Code
    
    python .\flaskapp\app.py

Files and Folders<br>
-- audio: Sample audio files should be uploaded to this file.<br>

-- audiototext: Audio to Text output present in the output folder(.txt file)<br>

-- sentimentanalysis: List of Positive words and Negative words should be uploaded/appended to the files folder(.txt files)<br>

-- stemming: Unstemmed text to Stemmed text output present in the output folder(.txt file)<br>



Tools Used:<br>
- VSCode[IDE] : Visual Studio Code is a code editor redefined and optimized for building and debugging modern web and cloud applications.<br>

Libraries & Frameworks Used:<br>
- <b>scipy</b> : SciPy (pronounced "Sigh Pie") is an open-source software for mathematics, science, and engineering. It includes modules for statistics, optimization, integration, linear algebra, Fourier transforms, signal and image processing, ODE solvers, and more.<br>
- <b>nltk</b> : The Natural Language Toolkit, or more commonly NLTK, is a suite of libraries and programs for symbolic and statistical natural language processing for English written in the Python programming language.<br>
- <b>streamlit</b> : Streamlit is an open source python based framework for developing and deploying interactive data science dashboards and machine learning models.<br>
- <b>numpy</b> : NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays<br>
- <b>matplotlib</b> : Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy<br>
- <b>SpeechRecognition</b> : Speech recognition is an interdisciplinary subfield of computer science and computational linguistics that develops methodologies and technologies that enable the recognition and translation of spoken language into text by computers with the main benefit of searchability.<br>
- <b>Flask</b> : Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.<br>
