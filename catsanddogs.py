import pickle
import random
import tensorflow as tf
import pandas
import tkinter as tk
import os
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator #type: ignore

from tkinter import *
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
batch_size = 128
IMG_HEIGHT = 150
IMG_WIDTH = 150
PATH =  'cats_and_dogs\cats_and_dogs'
test_dir = os.path.join(PATH,'test')
test_image_generator = ImageDataGenerator(rescale=1./255)
test_data_gen = test_image_generator.flow_from_directory(test_dir, target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                         classes ='.',
                                                         class_mode='categorical', 
                                                         batch_size=batch_size,
                                                         shuffle = False)
model = keras.models.load_model('CatDog.h5')
def plot():
    a = random.randint(1,50)
    filename = str(a) +'.jpg'
    folderpath = 'cats_and_dogs\cats_and_dogs'
    folderpath = os.path.join(folderpath, 'test')
    photopath = os.path.join(folderpath, filename )
    photo = ImageTk.PhotoImage(Image.open(photopath))
    l = Label(window,image=photo)
    l.pack()
    



window = tk.Tk()
window.geometry('800x600')
window.title('Cat or Dog')


Randombutton = Button(window,command= plot, height=5,width=10, text = "Generate").pack()
window.mainloop()