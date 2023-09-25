import os

import openai
import streamlit as st


# Initialize OpenAI API key
def initialize_openai_api(api_key):
    openai.api_key = api_key

# Create a conversation message
def create_message(role, content):
    return {'role': role, 'content': content}

# Generate a response from OpenAI
def generate_response(messages, temperature=0.7):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

# Main Streamlit app
def main():
    st.title("💬 Food Order Chatbot")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            create_message("assistant", "Welcome to My Dear Frankfurt! How can I assist you today?")
        ]


    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if "context" not in st.session_state:
        SCRIPT_WD = os.path.dirname(__file__)
        prompts_directory = os.path.join(SCRIPT_WD, "prompts")
        order_prompt_path = os.path.join(prompts_directory, "order.prompt")

        with open(order_prompt_path, "r") as file:
            context_content = file.read()

        st.session_state.context = [{'role':'system', 'content': context_content}]


    user_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
    if st.sidebar.button("Set API Key"):
        initialize_openai_api(user_api_key)

    if user_input := st.chat_input("You:", key="user_input"):
        try:
            if not openai.api_key:
                st.info("Please add your OpenAI API key to continue.")
            else:
                user_prompt = user_input.strip()
                # Add user prompt to the conversation
                st.session_state.context.append(create_message("user", user_prompt))
                st.session_state.messages.append(create_message("user", user_prompt))

                # Generate the assistant's response
                assistant_response = generate_response(st.session_state.context)
                st.session_state.context.append(create_message("assistant", assistant_response))
                st.session_state.messages.append(create_message("assistant", assistant_response))
                st.rerun()
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    if st.button("Clear Conversation"):
        st.session_state.messages = []


if __name__ == "__main__":
    main()
