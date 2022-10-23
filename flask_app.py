# importing the required modules and packages from flask
from datetime import datetime
import random
from flask import render_template
from flask import request
from flask import Flask
from flask import send_file

app = Flask(__name__)

# Encryption function
def encrypt(file):

    # opening the file int binary format
    fo = open(file, "rb")

    # reading the binary data from image (returns bytes)
    image=fo.read()

    # closing the file
    fo.close()

    # converting the bytes into bytearray to perform the Slightest Algorithm
    image=bytearray(image)

    key=random.randint(0,256)

    # Applying the Slightest Algorithm(simple XOR Operation)
    for index , value in enumerate(image):
        image[index] = value^key

    # opening an image
    fo=open("Encrypted_Image.jpg","wb")
    imageRes="Encrypted_Image.jpg"

    # writing the bytearray to the created file
    fo.write(image)
    fo.close()
    return (key,imageRes)

# Decryption function
def decrypt(key,file):
    # from decryption tab
    # reading the file in binary format
    fo = open(file, "rb")

    # read() method returns bytes from the binary file
    image=fo.read()

    # closing the file
    fo.close()

    # bytearray() class returns mutable copy of bytes
    image=bytearray(image)

    # performing the xor operation on that mutable byte array
    for index , value in enumerate(image):
        image[index] = value^key

    # creating a jpg file in binary format
    fo=open("Decrypted_Image.jpg","wb")
    imageRes="Decrypted_Image.jpg"

    # writing that bytes into above jpg file
    fo.write(image)
    fo.close()

    # returing the filename
    return imageRes

# home route
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title="Home Page",
        college="TRR Collge of Technology",
        year=datetime.now().year,
    )

# Decryption tab code
@app.route('/Decryption')
def Decryption():
    """Renders the Decryption page."""
    return render_template(
        'Decryption.html',
        title='Decryption',
        college="TRR Collge of Technology",
        message='Upload your encrypted image along with the key'
    )

# Encryption tab code
@app.route('/Encryption')
def Encryption():
    """Renders the Encryption page."""
    return render_template(
        'Encryption.html',
        title='Encryption',
        college="TRR Collge of Technology",
        message='Upload the image here'
    )
@app.route('/Encrypted', methods = ['POST'])
def Encrypted():
    if request.method == 'POST':
        global f
        f = request.files['file']
        f.save(f.filename)
        key,image=encrypt(f.filename)

        return render_template('Encrypted.html',
        title='Encrypted',
        college="TRR Collge of Technology",
        message='This is your encrypted image',
        name = f.filename,
        keys=key,
        images=image)

@app.route('/Decrypted', methods = ['POST'])
def Decrypted():
    if request.method == 'POST':
        global f
        f = request.files['file']
        f.save(f.filename)
        text = request.form['key']
        key=int(text)
        image=decrypt(key,f.filename)

        return render_template('Decrypted.html',
        title='Decrypted',
        college="TRR Collge of Technology",
        message='This is your Decrypted image', name = f.filename)


@app.route('/return-file')
def return_file():
    return send_file("../Encrypted_Image.jpg",attachment_filename="Encrypted_Image.jpg")

@app.route('/return-file1')
def return_file1():
    return send_file("../Decrypted_Image.jpg",attachment_filename="Decrypted_Image.jpg")


if __name__ == "__main__":
    app.run(debug=False)