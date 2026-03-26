---
description: "/plan <descriptions|design_file>: Initiate planning phase — discuss, structure, and produce a plan document."
---

# Plan Workflow

## Trigger
User initiates planning with `/plan <input>`.

`<input>` can be:
- **口語描述**: 一段自然語言的功能需求 (e.g., `/plan 我想加入一個 Boss 戰系統`)
- **設計文件路徑**: 指向 `design/` 下已存在的文件 (e.g., `/plan design/game/system/戰鬥系統.md`)

## 1. Input Analysis
*   **If 口語描述**: Activate **Game Designer** skill to help structure the idea.
    *   Clarify the requirements with the User.
    *   Ask clarifying questions about scope, visual needs, audio needs.
*   **If 設計文件**: Read the referenced file from `design/`.
    *   Summarize key points back to User to confirm understanding.
    *   Identify any ambiguities or missing information.

## 2. Plan Creation
*   **Action**: Create a markdown file in `.agent/plans/PLAN-<流水號>-<title>.md`.
*   **Content**: Outline the strategy, architecture changes, and a high-level task list.
*   **Template**:
    ```markdown
    # PLAN-[ID]: [Title]
    
    ## Source
    [Link to design file or summary of verbal description]
    
    ## Objective
    [What are we trying to achieve?]
    
    ## Implementation Strategy
    [High-level technical approach]
    
    ## Required Skills
    [Which skills will be needed: Art Director? Developer? Systems Architect?]
    
    ## Task List
    - [ ] Task 1
    - [ ] Task 2
    ```

## 3. Branching
*   **Action**: Checkout to a new branch for the planning process.
*   **Format**: `PLAN-<流水號>/<title>`
*   **Command**: `git checkout -b PLAN-[ID]/[title]`

## 4. 🚧 Confirmation (GATE — 等待 User 審核)
*   **Present**: Show the plan to the User.
*   **Wait**: Do NOT proceed to card creation. User must explicitly invoke `/plan-card` to continue.
