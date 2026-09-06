# Acrazie Skills Context & Domain Glossary

This document defines the ubiquitous language and domain vocabulary across the skills repository.

## Jenkins Family

**Jenkins Parent**:
The `jenkins-devops-acrazie` skill, responsible for approving, orchestrating, and validating pipeline modifications and production deployments across application repositories.

**Symfony Specialist**:
The `jenkins-symfony-php-acrazie` specialist skill, dedicated to interpreting Symfony application architecture, CI requirements, and runtime dependencies for the Jenkins Parent. It provides CI constraints without directly executing deployment stages.
*Avoid*: Generic PHP specialist, Symfony deployer.

**Python Specialist**:
The `jenkins-python-acrazie` specialist skill, dedicated to Python packaging, testing (pytest/tox), and runtime containerization for Jenkins pipelines.

## Skill Lifecycle & Refinement

**Skill Refiner**:
The interactive feedback workflow (`skill-refiner-acrazie`) that observes real skill usage, records append-only journals under `.skill-refiner/`, and updates living Architectural Decision Records (ADRs).
*Avoid*: Skill Improver (deprecated legacy name).

**Audit Record**:
A formal, read-only technical evaluation artifact created under `docs/audits/` via `audit-repository-acrazie`.
