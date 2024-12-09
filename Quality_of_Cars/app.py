import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder 
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score

st.set_page_config(
    page_title = "Qualify of Cars",
    layout = "wide"
)

@st.cache_data # avoid page reloading when adding new data
def load_data_and_model():
    cars = pd.read_csv(r"D:\Repositories\Data-Science\Quality_of_Cars\data\car.csv", sep=",")
    encoder = OrdinalEncoder()

    for col in cars.columns.drop('class'):
        cars[col] = cars[col].astype('category') #transform all columns in categorical type except class column
    
    X_encoded = encoder.fit_transform(cars.drop('class', axis=1))
    
    y = cars['class'].astype('category').cat.codes

    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.3, random_state = 42)

    model = CategoricalNB()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return encoder, model, accuracy, cars

encoder, model, accuracy, cars = load_data_and_model()

st.title("Cars Quality Forecast")
st.write(f"Accuracy of Model: {accuracy:.2f}")

input_features = [

    st.selectbox("Price:", cars['buying'].unique()),
    st.selectbox("Maint:", cars['maint'].unique()),
    st.selectbox("Doors:", cars['doors'].unique()),
    st.selectbox("Persons:", cars['persons'].unique()),
    st.selectbox("car trunk:", cars['lug_boot'].unique()),
    st.selectbox("Safety:", cars['safety'].unique())

]

if st.button("Process"):
    input_df = pd.DataFrame([input_features], columns = cars.columns.drop('class'))
    input_encoded = encoder.transform(input_df)
    predict_encoded = model.predict(input_encoded)
    forecast = cars['class'].astype('category').cat.categories[predict_encoded][0]
    st.header(f"Forecast Results: {forecast}")