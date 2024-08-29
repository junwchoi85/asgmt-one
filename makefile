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
	PYTHONPATH=$(shell pwd)/src $(PYTHON) src/frameworks_drivers/db/database_setup.py
	@echo "Database setup complete."

# 테스트 실행
.PHONY: test
test: install
	@echo "Running tests..."
	PYTHONPATH=$(shell pwd)/src $(PYTHON) -m pytest -s
	@echo "Tests complete."

# 테스트 실행
.PHONY: test_debug
test_debug: install
	@echo "Running tests in debug mode..."
	PYTHONPATH=$(shell pwd)/src $(PYTHON) -m pytest --pdb
	@echo "Tests complete."

# 가상 환경 제거
.PHONY: clean
clean:
	@echo "Cleaning up..."
	rm -rf $(VENV_DIR)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	find . -type f -name '*.db' -delete
	rm -rf dist build
	find . -type f -name '*.flag' -delete
	@echo "Cleanup complete."

# 가상환경을 활성화하고 main.py를 실행하는 규칙
.PHONY: run
run:
	PYTHONPATH=$(shell pwd)/src $(PYTHON) src/main.py

# 프로젝트 패키징
.PHONY: package
package: install
	@echo "Packaging project..."
	PYTHONPATH=$(shell pwd)/src $(PYTHON) -m pyinstaller --clean --onefile src/main.py
	@echo "Project packaged."

# Windows용 실행 파일 생성
.PHONY: package_win
package_win: install
	@echo "Packaging project for Windows..."
	PYTHONPATH=$(shell pwd)/src $(PYTHON) -m pyinstaller --clean --onefile --windowed --name main.exe src/main.py
	@echo "Windows executable packaged."