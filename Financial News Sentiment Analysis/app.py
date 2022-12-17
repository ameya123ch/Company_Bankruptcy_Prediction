import streamlit as st
import tensorflow as tf
import tensorflow_hub as hub




new_model = tf.keras.models.load_model("best_model.h5",custom_objects={"KerasLayer": hub.KerasLayer})





def welcome():
    return "Welcome to my app"


def main():
    st.title("Financial News Sentiment Analysis App")
    st.write(
        "This app will tell you if mention news is Fake or Real by using Natural Language Processing")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Financial News Sentiment Analysis </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    text = st.text_input("Enter your Financial News")


    if st.button("Predict"):
        pred_prob = new_model.predict([text])
        predict = tf.squeeze(tf.round(pred_prob)).numpy()
        st.subheader("AI thinks that ...")

        if predict > 0:

            st.success(
                f"It's a Positive News.You can make your investment decision accordingly. Confidence Level is {tf.round(pred_prob, 3)*100}%",icon="✅")
        else:
            st.warning(
                f"It's a Negative News. Think twice before you take any investment decision. Confidence Level is {tf.round(100 - pred_prob, 3)*100}%", icon="⚠️")

    if st.button("About"):

        st.text("Built with Streamlit")


if __name__ == '__main__':
    main()

