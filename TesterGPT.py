import streamlit as st
import pandas as pd
from openai import OpenAI
import data
import os
import time


client = OpenAI(
    api_key=data.Credentials.API_KEY
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)

model = "gpt-3.5-turbo"

# creating new assistant_id

# personal_assis = client.beta.assistants.create(
#     name="Testorn-ESB",
#     instructions="you are a test case generator generating minimum of 10 test cases ,you get a feature like 'login' or query parms in api testing like this-'api::member_id' and your response is- validation test cases generating 10 test cases ,your response will be in  table with 4 colmuns :ID, test name ,steps ,expected results,test type(functional/G.U.I)",
#     model=model
# )

assistant_id="asst_E2pgf75ljoNqJgCxgRDPYOMx"
print(assistant_id)

# creating new thread_id:

# thread = client.beta.threads.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "login"
#         }
#     ]
# )
thread_id = "thread_1U4jcY03Ap4KGE5w1tE3apkD"
print(thread_id)


st.title('TesterGPT')
st.title('AI is :blue[cool] :sunglasses:')
st.write("Test Case Generator")

data_df = pd.DataFrame(
    {
        "category": [
            "📊 Digital",
            "📈 E2E",
            "🤖 Integration-ESB",
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "category": st.column_config.SelectboxColumn(
            "Team Category",
            help="The category of the team",
            width="medium",
            options=[
                "📊 Digital",
                "📈 E2E",
                "🤖 Integration-ESB",

            ],
            required=True,
        )
    },
    hide_index=True,
)
requirement = st.text_input("Enter a feature", )


def generate_test_cases(requirement):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant capable of generating minimum of 10 test cases with no mistakes!,your response will be in  table with 4 colmuns of max 10 tests :ID, test name ,steps ,expected results,test type(functional/G.U.I),only if you get query parms like this-api::'the name of the params' it means API testing,you will response with sending valid/inavlid/empty/null the steps will be detailed -only in the case of api parms the expected result always will contains the HTTP status code 200 or 500 ,query parms like this-api::'the name of the parms'+yes,means the parms is mandatory so sending null/empty will get 500 HTTP status code,if api::'the name of the parms'+NO, means the parms is non mandatory and the expected result for null/empty will be 200 HTTP status code ,if the input will be the parms and (dataType) so the invlid value test will be a negative tests with examples on the steps-for example (int) will get-send characters-AAA,if gets also number like(5) it means the max length of the parms -the invalid tests will be send 6 numbers in the parms,only if the input is-CB -it means compering the response on the service to the CouchBase you will provide only 1 test of compere details of the response to the CB ,only if the input is- DB -the response will be 1 test of compere details to the DataBase,only if the input is- AppLinx -the response will same as DB/CB - 1 test of compare details from service respone to the AppLinx "},
            {"role": "user", "content": requirement}
        ]
    )
    return response.choices[0].message.content




# Button to generate test cases
if st.button('Generate Test Cases'):
    if requirement:
        with st.spinner('Generating...'):
            try:
                test_cases = generate_test_cases(requirement)
                st.success('Generated Test Cases')
                st.write(test_cases)
            except Exception as e:
                st.error('An error occurred while generating test cases.')
                st.error(e)
    else:
        st.error('Please enter a requirement to generate test cases.')

st.write("By Alon Fiban")
