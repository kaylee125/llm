"""
링크드인에서 프로필 정보를 스크래핑하는 코드
"""

import os
import requests

from dotenv import load_dotenv

def scrape_linkedin_profile(linkedin_profile_url:str,mock:bool=False):
    """
    scrape information from linkedin profiles.
    manually scrape the information from the linkedin profile
    """

    if mock:
        linkedin_profile_url="https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
        response=requests.get(linkedin_profile_url)

    else:
        api_endpoint=""
        header_dic={"Authorization":f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response=requests.get(
            api_endpoint,
            params={"url":linkedin_profile_url},
            headers=header_dic,
            timeout=10,
        )
    
    data=response.json()


    # 토큰 수를 줄이기 위해 유효하지 않은 응답 데이터의 키 값을 결과값에서 제외하는 코드 스니펫
    data={
        k:v
        for k,v in data.items()
        if v not in ([],'',None) and k not in['certifications']

    }
    return data


if __name__=="__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/eden-marco/",
            mock=True
        )
    )