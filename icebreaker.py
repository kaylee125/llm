import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import *
from langchain_openai import ChatOpenAI
# from langchain_ollama import ChatOllama
from third_party.linkedin import scrape_linkedin_profile
# .env 파일 로드
load_dotenv()

def ice_break_with(name:str):
    """
    링크드인 조회 에이전트 사용하여
    해당 이름의 링크드인 Url반환
    

    """

if __name__ == "__main__":
    print("hello langchain")
    
    # 환경 변수 가져오기
    api_key = os.getenv('OPENAI_API_KEY')  # KeyError 방지
    if api_key:
        print(api_key)
    else:
        print("OPENAI_API_KEY is not set")

    summary_template="""
    given the linkedin information {information} about a person i wnat you to create:
    1. a short summary
    2. two intersting facts about them

"""
    summary_prompt_templat=PromptTemplate(
        input_variables=["information"],template=summary_template
    )

    # llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    llm=ChatOpenAI(model="llama3")

    chain=summary_prompt_templat | llm | StrOutputParser()

    linkedin_data=scrape_linkedin_profile()

    res=chain.invoke(input={"information":linkedin_data})

    print(res)
