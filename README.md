# The_12_Zodiac_Animals
12_zodiac

카메라로 전신 사진을 촬영하고 십이지신 동물을 무작위로 배정하는 Streamlit 데모입니다. 앱을 연 날에는 50~500 크레딧을 5 단위로 한 번 지급합니다.

## 로컬 실행

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run 01_start.py
```

카메라 사용을 허용해 주세요. 카메라는 localhost 또는 HTTPS 환경에서 사용할 수 있습니다.

## Streamlit Community Cloud 배포

1. 이 프로젝트를 GitHub 저장소에 push합니다.
2. [Streamlit Community Cloud](https://share.streamlit.io/)에서 저장소를 연결합니다.
3. 앱 파일 경로로 `01_start.py`를 지정해 배포합니다.

## 데모의 저장 범위

이 버전은 크레딧, 보상 기록, 사진을 Streamlit 세션 안에서만 보관합니다. 따라서 브라우저 세션이 끝나거나 새 세션으로 접속하면 데이터가 초기화됩니다. 실제 이용자별로 매일 1회 보상을 유지하려면 로그인/사용자 식별과 영구 데이터베이스를 추가해야 합니다. 사진은 별도 서버나 파일에 저장하지 않습니다.
