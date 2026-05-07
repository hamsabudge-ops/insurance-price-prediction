# creat environment
# python -m venv myenv
# activate environment
# venv\Scripts\activate

#install dependencies
# streamlit pandas matplotlib seaborn scikit-learn

import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler
 #load the model
model = pickle.load(open('gb_model.pkl','rb'))
 #load scalar
Scaler = MinMaxScaler()
 #give title
st.title('Insurance premium price prediction app')
# define variables
age=st.number_input('Age',min_val=1,max_val=100,value=25)
gender=st.selectbox('Gender',('male','female'))
bmi=st.number_input('BMI',min_value=20.0,max_value=100,value=30.0)
smoker=st.selectbox('Smoker',('Yes','No'))
children=st.number_input('Number of Children',min_val=0,max_val=10,value=3)
region=st.selectbox('Region',('southwest','northwest','northeast','southeast'))

#write a logic for categorical values
#gender smoker,region
Smoker = 1 if smoker == 'Yes' else 0
#region
region_dict={'southwest':0,'northwest':1,'northeast':2,'southeast':3}
Region = region_dict[region]
#gender
sex_male = 1 if gender=='male' else 0
sex_female = 1 if gender=='female' else 0

# creat dataframe
input_features = pd.DataFrame({'age':[age],
                                            'bmi':[bmi],
                                            'children':[children],
                                            'Smoker':[Smoker],
                                            'sex_male':[sex_female],
                                            'sex_female':[sex_female],
                                            'Region':[Region]})
                                            
  #min max scalar
input_features[['age','bmi']]=scaler.fit_transform(input_features[['age','bmi']])
  #predictions
if st.button('Predict'):
              predictions=model.predict(input_features)
              output = round(np.exp(predictions[0]),2)
              st.success(f'predicted Charges: ${output}')