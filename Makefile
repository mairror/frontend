SHELL := /usr/bin/bash
.DEFAULT_GOAL := help

# AutoDoc
# -------------------------------------------------------------------------
.PHONY: help
help: ## This help. Please refer to the Makefile to more insight about the usage of this script.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
.DEFAULT_GOAL := help

# Docker
# -------------------------------------------------------------------------

# FRONT
# -------------------------------------------------------------------------
.PHONY: build-docker-front
build-docker-front: ## Build the FRONT Dockerfile. Optional variables BUILDKIT, DOCKER_FRONT_IMAGE and DOCKER_FRONT_TAG
	export BUILDKIT=$(or $(BUILDKIT_ENABLED),1) \
		DOCKER_FRONT_IMAGE=$(or $(DOCKER_FRONT_IMAGE),mairror-front) \
		DOCKER_FRONT_TAG=$(or $(DOCKER_FRONT_TAG),test) && \
	docker build -t $$DOCKER_FRONT_IMAGE:$$DOCKER_FRONT_TAG .
.DEFAULT_GOAL := build-docker-front

.PHONY: lint-docker-front
lint-docker-front: ## Lint the FRONT Dockerfile
	docker run --rm -i -v ${PWD}:/hadolint --workdir=/hadolint hadolint/hadolint < Dockerfile
.DEFAULT_GOAL := lint-docker-front

.PHONY: run-docker-front
run-docker-front: ## Run the FRONT isolated. Optional variables BUILDKIT, DOCKER_FRONT_IMAGE and DOCKER_FRONT_TAG
	export BUILDKIT=$(or $(BUILDKIT_ENABLED),1) \
		DOCKER_FRONT_IMAGE=$(or $(DOCKER_FRONT_IMAGE),mairror-front) \
		DOCKER_FRONT_TAG=$(or $(DOCKER_FRONT_TAG),test) && \
	docker run --rm --name $$DOCKER_FRONT_IMAGE --env-file .env -p 8000:8000 $$DOCKER_FRONT_IMAGE:$$DOCKER_FRONT_TAG
.DEFAULT_GOAL := run-docker-front

# Python
# -------------------------------------------------------------------------

# Cache
# -------------------------------------------------------------------------
.PHONY: clean-pyc
clean-pycache: ## Clean pycache files

	find . -name '__pycache__' -exec rm -rf {} +
.DEFAULT_GOAL := clean-pyc

# Tests
# -------------------------------------------------------------------------
.PHONY: test
test: ## Run all test with pytest
	pytest src/tests
.DEFAULT_GOAL := test
