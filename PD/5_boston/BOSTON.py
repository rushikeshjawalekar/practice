#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import boston_housing
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


# In[3]:


(X_train, y_train), (X_test, y_test) = boston_housing.load_data()


# In[4]:


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = Sequential([
    Dense(1, input_dim=X_train_scaled.shape[1])  
])


# In[5]:


model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(X_train_scaled, y_train, epochs=100, batch_size=32, verbose=1)

mse = model.evaluate(X_test_scaled, y_test, verbose=0)
print(f"Mean Squared Error on Test Data: {mse}")


# In[6]:


weights, bias = model.layers[0].get_weights()


# In[7]:


print("Coefficients:")
for i in range(len(weights)):
    print(f"Feature {i+1}: {weights[i][0]}")
print(f"Bias: {bias[0]}")

weights, bias = model.layers[0].get_weights()
y_pred = model.predict(X_test_scaled)

plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted Prices")


# In[ ]:




