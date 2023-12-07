# 사용할 베이스 이미지 선택 (파이썬 버전 3.9을 사용하는 예시)
FROM python:3.9-slim

# 작업 디렉터리 설정
WORKDIR /usr/src/app

# 애플리케이션에 필요한 파이썬 패키지 설치
COPY requirements.txt ./
RUN pip install -r requirements.txt

# 애플리케이션 코드를 컨테이너 안에 복사
COPY . .

CMD ["python","main_route.py"]
