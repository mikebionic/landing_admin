# Landing Admin Makefile
# Useful commands for development and deployment

# Variables
PYTHON = python3
PIP = pip3
FLASK = flask
DOCKER_COMPOSE = docker-compose
PROJECT_NAME = landing-admin
VENV = venv

# Colors for output
RED = \033[0;31m
GREEN = \033[0;32m
YELLOW = \033[1;33m
BLUE = \033[0;34m
NC = \033[0m # No Color

.PHONY: help install run test clean docker-build docker-up docker-down docker-logs docker-shell db-init db-migrate db-reset lint format

# Default target
help: ## Show this help message
	@echo "$(GREEN)Landing Admin - Available Commands$(NC)"
	@echo "$(YELLOW)================================$(NC)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "$(BLUE)%-20s$(NC) %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# Development Setup
install: ## Install dependencies and setup development environment
	@echo "$(GREEN)Setting up development environment...$(NC)"
	$(PYTHON) -m venv $(VENV)
	./$(VENV)/bin/pip install --upgrade pip
	./$(VENV)/bin/pip install -r requirements.txt
	@echo "$(GREEN)✓ Dependencies installed$(NC)"
	@echo "$(YELLOW)Don't forget to activate your virtual environment:$(NC)"
	@echo "  source $(VENV)/bin/activate"

install-dev: ## Install development dependencies
	@echo "$(GREEN)Installing development dependencies...$(NC)"
	./$(VENV)/bin/pip install pytest pytest-flask flask-debugtoolbar black flake8 pylint

setup: ## Setup project (copy env, create directories)
	@echo "$(GREEN)Setting up project structure...$(NC)"
	cp -n .env.example .env || echo ".env already exists"
	mkdir -p static/uploads
	mkdir -p logs
	@echo "$(GREEN)✓ Project setup complete$(NC)"
	@echo "$(YELLOW)Please edit .env file with your configuration$(NC)"

# Development
run: ## Run development server
	@echo "$(GREEN)Starting development server...$(NC)"
	$(PYTHON) app.py

run-debug: ## Run development server with debug
	@echo "$(GREEN)Starting development server in debug mode...$(NC)"
	FLASK_ENV=development FLASK_DEBUG=1 $(PYTHON) app.py

test: ## Run tests
	@echo "$(GREEN)Running tests...$(NC)"
	$(PYTHON) -m pytest tests/ -v

test-coverage: ## Run tests with coverage
	@echo "$(GREEN)Running tests with coverage...$(NC)"
	$(PYTHON) -m pytest tests/ --cov=main --cov-report=html --cov-report=term

# Code Quality
lint: ## Run linting
	@echo "$(GREEN)Running linting...$(NC)"
	flake8 main/ app.py --max-line-length=120
	pylint main/ app.py --disable=C0103,R0903,W0613

format: ## Format code with black
	@echo "$(GREEN)Formatting code...$(NC)"
	black main/ app.py --line-length=120

check: lint test ## Run linting and tests

# Docker Operations
docker-build: ## Build Docker image
	@echo "$(GREEN)Building Docker image...$(NC)"
	$(DOCKER_COMPOSE) build

docker-up: ## Start application with docker-compose
	@echo "$(GREEN)Starting application with Docker...$(NC)"
	$(DOCKER_COMPOSE) up -d
	@echo "$(GREEN)✓ Application started$(NC)"
	@echo "$(YELLOW)Application available at: http://localhost:8000$(NC)"
	@echo "$(YELLOW)pgAdmin available at: http://localhost:5050 (admin@example.com / admin123)$(NC)"

docker-up-dev: ## Start application with development profile
	@echo "$(GREEN)Starting application with development profile...$(NC)"
	$(DOCKER_COMPOSE) --profile development up -d

docker-up-prod: ## Start application with production profile
	@echo "$(GREEN)Starting application with production profile...$(NC)"
	$(DOCKER_COMPOSE) --profile production up -d

docker-down: ## Stop docker-compose
	@echo "$(GREEN)Stopping Docker containers...$(NC)"
	$(DOCKER_COMPOSE) down

docker-down-volumes: ## Stop docker-compose and remove volumes
	@echo "$(GREEN)Stopping Docker containers and removing volumes...$(NC)"
	$(DOCKER_COMPOSE) down -v

docker-logs: ## View docker-compose logs
	@echo "$(GREEN)Viewing Docker logs...$(NC)"
	$(DOCKER_COMPOSE) logs -f

docker-shell: ## Access app container shell
	@echo "$(GREEN)Accessing app container shell...$(NC)"
	$(DOCKER_COMPOSE) exec app bash

docker-psql: ## Access PostgreSQL shell
	@echo "$(GREEN)Accessing PostgreSQL shell...$(NC)"
	$(DOCKER_COMPOSE) exec postgres psql -U postgres -d landing_admin

docker-redis: ## Access Redis CLI
	@echo "$(GREEN)Accessing Redis CLI...$(NC)"
	$(DOCKER_COMPOSE) exec redis redis-cli

# Database Operations
db-init: ## Initialize database
	@echo "$(GREEN)Initializing database...$(NC)"
	$(FLASK) db init

db-migrate: ## Create database migration
	@echo "$(GREEN)Creating database migration...$(NC)"
	$(FLASK) db migrate -m "Database migration"

db-upgrade: ## Apply database migrations
	@echo "$(GREEN)Applying database migrations...$(NC)"
	$(FLASK) db upgrade

db-reset: ## Reset database (WARNING: This will delete all data)
	@echo "$(RED)⚠️  WARNING: This will delete all database data!$(NC)"
	@read -p "Are you sure? (y/N) " -n 1 -r; \
	echo; \
	if [[ $$REPLY =~ ^[Yy]$$ ]]; then \
		echo "$(GREEN)Resetting database...$(NC)"; \
		$(DOCKER_COMPOSE) down -v; \
		$(DOCKER_COMPOSE) up -d postgres redis; \
		sleep 5; \
		$(DOCKER_COMPOSE) up -d app; \
	else \
		echo "$(YELLOW)Database reset cancelled$(NC)"; \
	fi

# Utilities
clean: ## Clean temporary files and cache
	@echo "$(GREEN)Cleaning temporary files...$(NC)"
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type f -name ".coverage" -delete
	find . -type d -name "htmlcov" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +

clean-docker: ## Clean Docker images and containers
	@echo "$(GREEN)Cleaning Docker resources...$(NC)"
	docker system prune -f
	docker image prune -f

backup-db: ## Backup database
	@echo "$(GREEN)Creating database backup...$(NC)"
	mkdir -p backups
	$(DOCKER_COMPOSE) exec postgres pg_dump -U postgres landing_admin > backups/backup_$(shell date +%Y%m%d_%H%M%S).sql
	@echo "$(GREEN)✓ Database backup created in backups/ directory$(NC)"

restore-db: ## Restore database from backup (specify file with FILE=backup.sql)
	@echo "$(GREEN)Restoring database from backup...$(NC)"
	@if [ -z "$(FILE)" ]; then echo "$(RED)Error: Please specify backup file with FILE=backup.sql$(NC)"; exit 1; fi
	$(DOCKER_COMPOSE) exec -T postgres psql -U postgres -d landing_admin < $(FILE)
	@echo "$(GREEN)✓ Database restored from $(FILE)$(NC)"

# Production Deployment
deploy-staging: ## Deploy to staging
	@echo "$(GREEN)Deploying to staging...$(NC)"
	$(DOCKER_COMPOSE) -f docker-compose.yml -f docker-compose.staging.yml up -d

deploy-production: ## Deploy to production
	@echo "$(GREEN)Deploying to production...$(NC)"
	$(DOCKER_COMPOSE) -f docker-compose.yml -f docker-compose.prod.yml up -d

# Monitoring
status: ## Show application status
	@echo "$(GREEN)Application Status$(NC)"
	@echo "$(YELLOW)==================$(NC)"
	$(DOCKER_COMPOSE) ps

logs-app: ## Show app logs only
	$(DOCKER_COMPOSE) logs -f app

logs-db: ## Show database logs only
	$(DOCKER_COMPOSE) logs -f postgres

logs-redis: ## Show redis logs only
	$(DOCKER_COMPOSE) logs -f redis

# Quick shortcuts
up: docker-up ## Alias for docker-up
down: docker-down ## Alias for docker-down
build: docker-build ## Alias for docker-build
logs: docker-logs ## Alias for docker-logs

# Development workflow
dev-setup: setup install ## Complete development setup
dev-start: docker-up ## Start development environment
dev-stop: docker-down ## Stop development environment

# All-in-one commands
full-setup: setup install docker-build docker-up ## Complete setup and start
rebuild: docker-down clean-docker docker-build docker-up ## Rebuild and restart everything

# Show project info
info: ## Show project information
	@echo "$(GREEN)Landing Admin Project Information$(NC)"
	@echo "$(YELLOW)==================================$(NC)"
	@echo "Project: $(PROJECT_NAME)"
	@echo "Python: $(shell python3 --version)"
	@echo "Docker: $(shell docker --version)"
	@echo "Docker Compose: $(shell docker-compose --version)"
	@echo ""
	@echo "$(BLUE)Useful URLs:$(NC)"
	@echo "  Application: http://127.0.0.1:8000/"
	@echo "  Admin Panel: http://127.0.0.1:8000/admin/login/"
	@echo "  API: http://127.0.0.1:8000/api"
	@echo "  pgAdmin: http://localhost:5050"
	@echo ""
	@echo "$(BLUE)Default Admin Login:$(NC)"
	@echo "  Username: admin"
	@echo "  Password: 123456"
	@echo ""
	@echo "$(BLUE)Template Structure:$(NC)"
	@echo "  Admin templates: main/templates/admin/"
	@echo "  Your templates: main/templates/web/ (put your landing page here)"
	@echo "  Admin static: main/static/admin/"
	@echo "  Your static files: main/static/web/ (CSS/JS for your site)"