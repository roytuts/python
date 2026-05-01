build env:

1. py -m venv buildenv
2. buildenv\Scripts\activate
3. python.exe -m pip install --upgrade pip
4. pip install -r requirements.txt

Run code:

Single image -
python image_to_text.py sample.png

Creates outputs/sample.txt

Multiple images from a folder -
python image_to_text.py images/

Creates outputs/img1.txt, outputs/img2.txt, etc.

Multilingual -
python image_to_text.py sample.png --lang hin+eng
