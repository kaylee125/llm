import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import *
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
# .env 파일 로드
load_dotenv()

information="""
김정은(金正恩[3], 1984년 1월 8일[1] ~ )은 현재 조선민주주의인민공화국의 최고 지도자이다. 2000년대 후반부터 김정일의 후계자로 내세우는 등 영향력이 커지면서 이름이 알려지기 시작했으며, 2010년부터 당 중앙군사위 부위원장 등으로 정치에 참여했다. 2011년 김정일이 사망한 이후 3대 세습으로 조선민주주의인민공화국의 원수가 되었다.

그는 조선로동당 총비서, 조선민주주의인민공화국 국무위원회 위원장, 조선민주주의인민공화국 무력 최고사령관이다. 본관은 전주이며, 김정일과 고용희 사이의 둘째 아들이다. 스위스 유학 중 사용된 가명은 '박운'이다.[4] 김정일 사후, "당과 국가, 군대의 최고 통수자"로 칭해지고 있다. 2012년 4월 11일에 아버지 김정일을 이어서 조선로동당 제1비서가 되었으며, 4월 12일에는 국방위원회 제1위원장이 되었다. 2012년 7월 18일 원수로 진급했다.[5]

2016년 5월 9일 자신의 조선로동당 제1비서 직책을 폐지하고 조선로동당 위원장에 취임하면서 새로운 권력을 얻게 되었다. 이후 2016년 6월 29일 최고인민회의에서 국방위원회를 폐지하고 국무위원회를 신설했으며, 국방위원회 제1위원장 대신 국무위원회 위원장으로 취임하였다. 이 과정에서 김정일을 영원한 조선민주주의인민공화국 국방위원회 위원장으로 추대하였다. 김정은 위원장은 적성국이었던 대한민국과 미국과 각각 정상회담을 두 차례씩 개최하여 국가지도자로서 세계 무대에 드러냈다. 또한 2021년 1월 10일 조선로동당 제8차대회에서 조선로동당 총비서로 추대되었다.


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
    given the information {information} about a person i wnat you to create:
    1. a short summary
    2. two intersting facts about them

"""
    summary_prompt_templat=PromptTemplate(
        input_variables=["information"],template=summary_template
    )

    # llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    llm=ChatOllama(model="llama3")

    chain=summary_prompt_templat | llm | StrOutputParser()

    res=chain.invoke(input={"information":information})

    print(res)
