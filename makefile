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
	@echo "Creating virtual environment..."
	python3 -m venv $(VENV_DIR)
	@echo "Upgrading pip..."
	$(PYTHON) -m pip install --upgrade pip
	@echo "Installing dependencies from requirements.txt..."
	$(PYTHON) -m pip install -r requirements.txt
	@echo "Virtual environment setup complete."

# 종속성 설치
.PHONY: install
install: $(VENV_DIR)/bin/activate
	@echo "Dependencies installed."

# 데이터베이스 설정
.PHONY: setup_db
setup_db: install
	@echo "Setting up the database..."
	$(PYTHON) src/frameworks_drivers/db_setup/database_setup.py
	@echo "Database setup complete."

# 테스트 실행
.PHONY: test
test: install
	@echo "Running tests..."
	PYTHONPATH=$(shell pwd)/src $(PYTHON) -m pytest
	@echo "Tests complete."

# 가상 환경 제거
.PHONY: clean
clean:
	@echo "Cleaning up..."
	rm -rf $(VENV_DIR)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	@echo "Cleanup complete."