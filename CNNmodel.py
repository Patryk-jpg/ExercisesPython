from copyreg import pickle
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
import requests, zipfile, io
import os
if os.path.isdir('cats_and_dogs') == False:
    r = requests.get('https://cdn.freecodecamp.org/project-data/cats-and-dogs/cats_and_dogs.zip')
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall("cats_and_dogs")
    print('done')
else:
    print("Files Downloaded Arleady")
PATH = 'cats_and_dogs\cats_and_dogs'
train_dir = os.path.join(PATH, 'train')
validation_dir = os.path.join(PATH, 'validation')
test_dir = os.path.join(PATH, 'test')



# Variables for pre-processing and training.
batch_size = 128
epochs = 12
IMG_HEIGHT = 150
IMG_WIDTH = 150


train_image_generator = ImageDataGenerator(rescale=1./255)
validation_image_generator =ImageDataGenerator(rescale=1./255)
test_image_generator = ImageDataGenerator(rescale=1./255)

train_data_gen = train_image_generator.flow_from_directory(batch_size=batch_size,
                                                     directory=train_dir,
                                                     target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                     class_mode='binary')

val_data_gen = validation_image_generator.flow_from_directory(validation_dir, target_size=(IMG_HEIGHT, IMG_WIDTH),  class_mode='categorical',batch_size=batch_size)
test_data_gen = test_image_generator.flow_from_directory(test_dir, target_size=(IMG_HEIGHT, IMG_WIDTH), classes ='.',class_mode='categorical',  batch_size=batch_size, shuffle = False)
#I,ve found that you can use classes = ".", to get test data labels (labels when there are no subdirectories ))
from tensorflow.python.framework.func_graph import flatten

if os.path.isfile('CatDog.h5') == False:
    model = tf.keras.Sequential()   
    model.add(tf.keras.layers.Conv2D(32, (3,3) , input_shape = (150,150,3)))
    model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))
    model.add(tf.keras.layers.Conv2D(64, (3,3),activation = 'relu'))
    model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))
    model.add(tf.keras.layers.Conv2D(64, (3,3),activation = 'relu'))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(64))
    model.add(tf.keras.layers.Dense(1,activation = 'sigmoid'))
    model.compile(optimizer='adam',
                loss=tf.keras.losses.BinaryCrossentropy(),
                metrics=['accuracy'])
    model.fit(train_data_gen,
                epochs=epochs, 
                batch_size = batch_size,
                validation_data=val_data_gen,
                steps_per_epoch =1600//batch_size, 
                validation_steps=600//batch_size)



    model.save('CatDog.h5')
else:
    print('model created arleady')


