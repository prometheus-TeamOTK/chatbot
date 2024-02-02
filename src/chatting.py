from character import Character
import streamlit as st
import os
import json

def character_page(file_path, user, relation, situation):
    st.title("Fiction Comes True")
    overall_chain = Character(file_path, user, relation, situation)
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "안녕하세요? 어떤 일로 찾아오셨어요?"}]
    
    for message in st.session_state.messages:
        st.chat_message(message["role"]).write(message["content"])
    
    if prompt := st.chat_input("캐릭터에게 할 말을 입력하세요."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            assistant_response = overall_chain.receive_chat(prompt)
            message_placeholder.markdown(assistant_response)
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    
    save_conversation_to_json(st.session_state.messages, "conversation.json")

def save_conversation_to_json(messages, filename):
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(messages, json_file, ensure_ascii=False, indent=4)        

def main():
    os.environ["OPENAI_API_KEY"] = st.secrets["openai_key"]
    
    st.sidebar.title("캐릭터 선택")
    
    selected_char = st.sidebar.selectbox(
        "대화할 캐릭터를 선택하세요.",
        ["백설공주", "겨울왕국 엘사", "파워퍼프걸 블로섬", "신의 탑 밤", "나루토", "원피스 루피"]
    )
    
    if selected_char == "백설공주":
        selected_sit = st.sidebar.selectbox(
            "대화할 상황을 선택하세요.",
            ["마녀가 사과를 주려고 백설공주에게 찾아간 상황"]
        )
        
        user = "마녀"
        relation = "백설공주의 새엄마이자, 마법을 쓸 줄 아는 마녀. 자기보다 아름다운 백설공주를 질투해 독사과를 주려고 한다."
        situation = "백설공주(Bot)와 마녀(User)가 백설공주가 지내는 난쟁이 오두막에서 마주친 상황. 마녀는 백설공주에게 사과를 줄지 말지 갈등한다."
        
        character_page("data/snow_white.json", user, relation, situation)
        

if __name__ == "__main__" : 
    main()