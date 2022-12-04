import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

start_date = "2016-01-01"
today_date = date.today().strftime("%Y-%m-%d")

st.title("Stock Price Forcasting App")

stocks = ("GS","MS","JPM","C")
selected_stocks = st.selectbox("Select the stock for prediction",stocks)
n_years = st.slider("Years of Prediction",1, 4)
period = n_years * 365

@st.cache
def load_data(ticker):
    data = yf.download(ticker,start_date,today_date)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text("Loading the data....")
data = load_data(selected_stocks)
data_load_state.text("Data is Loaded!!")

st.subheader("Raw Data")
st.write(data.tail())

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x = data['Date'],y=data['Open'], name = 'Open Price'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name = 'Close Price'))
    fig.layout.update(title_text = "Time Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()


# forecasting
df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date":"ds", "Close":"y"})

model = Prophet()


model.fit(df_train)
future = model.make_future_dataframe(periods= period)
forecast = model.predict(future)

st.subheader('Forecast Data')
st.write(forecast.tail())

st.write("Forecast Data")
fig_1 = plot_plotly(model, forecast)
st.plotly_chart(fig_1)

st.write("Forecast Components")
fig_2 = model.plot_components(forecast)
st.write(fig_2)






























