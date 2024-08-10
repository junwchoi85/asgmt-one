# Makefile for Python project

# 가상 환경 디렉토리
VENV_DIR := venv

# Python 인터프리터
PYTHON := $(VENV_DIR)/bin/python

# 기본 타겟
.PHONY: all
all: setup_db

# 가상 환경 설정
$(VENV_DIR)/bin/activate: requirements.txt
	python3 -m venv $(VENV_DIR)
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

# 종속성 설치
.PHONY: install
install: $(VENV_DIR)/bin/activate

# 데이터베이스 설정
.PHONY: setup_db
setup_db: install
	$(PYTHON) src/frameworks_drivers/db_setup/database_setup.py

# 테스트 실행
.PHONY: test
test: install
	$(PYTHON) -m unittest discover -s tests

# 가상 환경 제거
.PHONY: clean
clean:
	rm -rf $(VENV_DIR)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete