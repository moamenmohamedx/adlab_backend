# Agent Governing Principles

This document outlines the core principles, development standards, and operational protocols that all AI agents must adhere to when working on this project. It serves as the primary guide for ensuring consistent, high-quality, and efficient contributions.

---

## 1. Core Philosophy: The 80/20 Principle

-   **Primary Directive**: Your primary goal is to apply the **80/20 principle** to all tasks. Focus on delivering 80% of the value with 20% of the effort.
-   **Avoid Over-Engineering**: Consciously avoid complexity. Prioritize simple, effective, and maintainable solutions over technically elaborate ones. If a simpler approach meets the requirements, it is the correct approach.
-   **Pragmatism Over Perfection**: Strive for clean, functional, and well-tested code. Do not spend excessive time on micro-optimizations or "perfect" solutions unless explicitly required.

---

## 2. Development & Code Style

-   **No Backward Compatibility**: You are not required to maintain backward compatibility. Always use the latest stable versions of libraries, frameworks, and language features to ensure the project remains modern and secure.
-   **Consistency is Key**: Adhere strictly to the existing code style, patterns, and architectural conventions found within the codebase. Before writing new code, review the surrounding files to understand the established style.
-   **Clear Separation of Concerns**: Maintain the strict architectural separation between the `frontend` and `backend` domains. Frontend code should not contain business logic that belongs in the backend, and vice-versa.
-   **Modularity**: Write modular and reusable code. Encapsulate logic within functions, classes, or components with clear, single responsibilities.
-   **Task & Knowledge Management**: All tasks and project knowledge are managed through the Archon MCP server. You must interface with it for all development activities.

---

## 3. Research & Tool Usage Protocol

-   **Current-Day Context**: When conducting research using web search or any other tool, you MUST operate with the current date: **December  2025**. This ensures all information, library versions, and examples are contemporary and relevant.
-   **Purposeful Tooling**: Use tools deliberately. `codebase_search` is for exploration. `grep` is for targeted symbol finding. `run_tests` is for validation. Explain your choice of tool and how it contributes to the task.

---

## 4. Task Execution Protocol

-   **Understand First, Act Second**: Before writing or modifying any code, ensure you have a clear understanding of the task requirements and the relevant parts of the codebase. Use your analysis tools to build context.
-   **Incremental Changes**: Implement changes in small, logical, and testable increments.
-   **Follow Established Patterns**: For common development tasks, such as adding new UI components, API endpoints, or AI tools, you MUST adhere to the procedures outlined in the "Key Implementation Patterns" section of the root `README.md`.
-   **Validate Your Work**: After making changes, always consider the impact. If you modify the backend, run the relevant tests. If you change the frontend, ensure it doesn't break existing UI components.