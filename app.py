import streamlit as st

from src.helper import voice_to_text,TextToAudio,Load_llm_Model

def main():
    st.title("Multilangual AI assistence")

    if st.button("Ask anything"):
        with st.spinner("Listening ....") :
            text=voice_to_text()
            st.title("Human Input:")
            st.text(text)
            if text =="I am unable to here you properly":
                TextToAudio(text)
            else:
                response=Load_llm_Model(text)
                st.text_area(label="AI-Bot Response: ",value=response,height=350)
                TextToAudio(response)
                with open("speech.mp3","rb") as audiobytes:
                    audiobytes=audiobytes.read()
                    print("loaded.....")
                st.audio(audiobytes)
                st.download_button(label="Download speech",data=audiobytes,
                                   file_name="Humaninput.mp3",mime="audio/mp3")
                
                






if __name__ =="__main__":
    main()