#Python program to train the data-sets for classification into 'coding' and 'non-coding' region.

#TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from load import load_data

train_x, train_y, test_x, test_y = load_data()
class_names = ['coding', 'non_coding']

print("Training set: {}".format(np.array(train_y).shape))  
print("Testing set:  {}".format(np.array(test_y).shape))

column_names = ['P_val', 'Hs_val', 'F3_val']
df = pd.DataFrame(train_x, columns=column_names)
print (df.head())

#Function to build my neural network model
def build_model():
	model = keras.models.Sequential([keras.layers.Dense(5, kernel_regularizer=keras.regularizers.l2(0.001),\
		activation=tf.nn.relu,input_dim=3),\
		keras.layers.Dense(5,kernel_regularizer=keras.regularizers.l2(0.001),activation=tf.nn.relu),\
		keras.layers.Dense(5,kernel_regularizer=keras.regularizers.l2(0.001),activation=tf.nn.relu),\
		keras.layers.Dense(1, activation=tf.nn.relu)])
	optimizer = tf.train.RMSPropOptimizer(0.001)
	model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])
	return model

# Display training progress by printing a single dot for each completed epoch
class PrintDot(keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs):
    if epoch % 100 == 0: print('')
    print('.', end='')

EPOCHS = 500

#Build network
model = build_model()
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=20)
history = model.fit(train_x, train_y, epochs=EPOCHS, verbose=0, \
	validation_data=(test_x, test_y), callbacks=[early_stop, PrintDot()])


#Visualize the model's training progress using the stats stored in the history object.
def plot_history(history):
  plt.figure()
  plt.xlabel('Epoch')
  plt.ylabel('Mean Abs Error')
  plt.plot(history.epoch, np.array(history.history['loss']),
           label='Train Loss')
  plt.plot(history.epoch, np.array(history.history['val_loss']),
           label = 'Test loss')
  plt.legend()
  plt.show()

plot_history(history)

#Model Evaluation
train_loss, train_acc = model.evaluate(train_x, train_y)

print('Train accuracy:', train_acc)
print('Train loss:', train_loss)

print('\n')
test_loss, test_acc = model.evaluate(test_x, test_y)

print('Test accuracy:', test_acc)
print('Test loss:', test_loss)

"""
#Measure accuracy
pred = model.predict(test_x)
prediction = [1 if x>=0.5 else 0 for x in pred]
y_compare = [i[0] for i in test_y]
c = [1 if prediction[i]==y_compare[i] else 0 for i in range(len(prediction))]
accuracy = c.count(1)/len(c)
print(accuracy)
"""