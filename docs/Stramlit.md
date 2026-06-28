# Streamlit Dashboard Learning

## Display Metric

st.metric("Total Articles", value)

## Display Heading

st.subheader("Top Sources")

## Call API

response = requests.get(url)

## Parse JSON

data = response.json()

## Display Data

st.write(data)
