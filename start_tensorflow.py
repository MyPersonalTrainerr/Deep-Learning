# -*- coding: utf-8 -*-
"""Main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SX5Md8cnkZjUclrhAqBO9RReLPAdTgFX
"""

import tensorflow as tf
print("TensorFlow version:", tf.__version__)

msg = tf.constant('TensorFlow 2.0 Hello World')
tf.print(msg)

a = tf.constant(5)
b = tf.constant(6)

c = tf.add(a, b)

tf.print(c)
print(c)
