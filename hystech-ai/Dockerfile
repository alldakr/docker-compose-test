# 기본 이미지로 Python 3.9 사용
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /app

# 소스 코드 복사
COPY main.py .

# 필요한 종속성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 실행 명령
CMD ["python", "main.py"]