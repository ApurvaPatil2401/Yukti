# Requirements Document

## Introduction

Yukti – The Guarded IDE is an AI-powered coding mentor designed to prioritize learning and conceptual understanding over speed and productivity. Unlike traditional AI coding tools that provide instant solutions, Yukti enforces a pedagogy-first approach by requiring users to demonstrate conceptual understanding before unlocking code solutions. The system addresses the critical problem of over-dependence on AI tools that leads to shallow learning and poor performance in interviews and debugging scenarios.

## Glossary

- **Yukti_System**: The complete AI-powered coding mentor application
- **Concept_Checker**: Component that validates user understanding of programming concepts
- **Solution_Gate**: Component that controls access to final code solutions based on concept validation
- **Learning_Tracker**: Component that monitors user progress and identifies weak concepts over time
- **Concept_Question**: A question designed to test understanding of a specific programming concept
- **Understanding_Level**: Measured assessment of user's grasp of a concept (weak, moderate, strong)
- **Code_Solution**: The final, correct implementation or bug fix provided by the system
- **Concept_Explanation**: User's natural language description of a programming concept
- **Hint_System**: Component that provides graduated assistance when user understanding is insufficient

## Requirements

### Requirement 1: Core Interaction Flow

**User Story:** As a student, I want to submit coding questions and receive guided learning rather than instant solutions, so that I develop genuine understanding and problem-solving skills.

#### Acceptance Criteria

1. WHEN a user submits a coding question or buggy code, THE Yukti_System SHALL identify the core programming concepts involved
2. WHEN concepts are identified, THE Yukti_System SHALL generate mandatory concept-based questions before providing any code
3. WHEN a user attempts to skip concept questions, THE Yukti_System SHALL prevent access to solutions and redirect to concept validation
4. WHEN all concept questions are answered satisfactorily, THE Solution_Gate SHALL unlock the complete code solution
5. THE Yukti_System SHALL maintain the learning-first principle throughout all interactions

### Requirement 2: Concept Validation and Assessment

**User Story:** As a coding mentor, I want to accurately assess user understanding through natural language explanations, so that I can determine when they're ready for the solution.

#### Acceptance Criteria

1. WHEN a user provides a concept explanation, THE Concept_Checker SHALL evaluate the explanation against established criteria for that concept
2. WHEN an explanation demonstrates insufficient understanding, THE Concept_Checker SHALL classify it as weak and trigger additional support
3. WHEN an explanation demonstrates adequate understanding, THE Concept_Checker SHALL classify it as sufficient and allow progression
4. THE Concept_Checker SHALL assess explanations for accuracy, completeness, and depth of understanding
5. WHEN evaluating explanations, THE Concept_Checker SHALL consider multiple valid ways of expressing the same concept

### Requirement 3: Adaptive Hint and Support System

**User Story:** As a struggling learner, I want to receive graduated hints and simpler questions when I don't understand a concept, so that I can build up to the full understanding step by step.

#### Acceptance Criteria

1. WHEN a user's explanation is classified as weak, THE Hint_System SHALL provide targeted hints related to the specific concept
2. WHEN hints are insufficient, THE Hint_System SHALL break down the concept into simpler sub-questions
3. WHEN providing hints, THE Hint_System SHALL avoid giving away the final solution while guiding toward understanding
4. THE Hint_System SHALL escalate support gradually from gentle nudges to more explicit guidance
5. WHEN a user demonstrates improved understanding after hints, THE Concept_Checker SHALL re-evaluate their readiness

### Requirement 4: Learning Progress Tracking

**User Story:** As a learner, I want the system to remember my weak areas and adapt future interactions accordingly, so that I can focus on improving my specific knowledge gaps.

#### Acceptance Criteria

1. WHEN a user struggles with a concept, THE Learning_Tracker SHALL record the concept as a weak area for that user
2. WHEN a user demonstrates strong understanding of a concept, THE Learning_Tracker SHALL update their proficiency level
3. WHEN generating future questions, THE Yukti_System SHALL prioritize concepts where the user has shown weakness
4. THE Learning_Tracker SHALL maintain historical data on user performance across different programming concepts
5. WHEN a user returns to the system, THE Yukti_System SHALL adapt difficulty and focus based on their tracked progress

### Requirement 5: Solution Access Control

**User Story:** As an educator, I want to ensure students cannot access solutions without demonstrating understanding, so that they develop genuine problem-solving abilities rather than copying code.

#### Acceptance Criteria

1. THE Solution_Gate SHALL prevent access to any code solutions until concept validation is complete
2. WHEN concept validation fails, THE Solution_Gate SHALL remain locked and redirect to additional learning activities
3. WHEN all required concepts are validated, THE Solution_Gate SHALL unlock and provide the complete solution
4. THE Solution_Gate SHALL not provide partial solutions or code snippets during the concept validation phase
5. WHEN a solution is unlocked, THE Yukti_System SHALL provide explanatory comments linking code to the validated concepts

### Requirement 6: Programming Concept Coverage

**User Story:** As a student preparing for technical interviews, I want comprehensive coverage of DSA and debugging concepts, so that I can build strong foundations in core programming areas.

#### Acceptance Criteria

1. THE Yukti_System SHALL support concept validation for fundamental data structures (arrays, linked lists, trees, graphs, hash tables)
2. THE Yukti_System SHALL support concept validation for core algorithms (sorting, searching, recursion, dynamic programming)
3. THE Yukti_System SHALL support concept validation for complexity analysis (time and space complexity, Big O notation)
4. THE Yukti_System SHALL support concept validation for debugging techniques (logical reasoning, edge case analysis, error identification)
5. WHEN new programming concepts are added, THE Yukti_System SHALL integrate them into the existing validation framework

### Requirement 7: Python Language Support

**User Story:** As a Python developer, I want to work with Python-specific concepts and syntax, so that I can learn in my preferred programming language.

#### Acceptance Criteria

1. THE Yukti_System SHALL parse and analyze Python code submissions for syntax and logical errors
2. THE Yukti_System SHALL generate Python-specific concept questions covering language features (list comprehensions, generators, decorators)
3. THE Yukti_System SHALL provide Python code solutions with proper syntax and idioms
4. WHEN validating concepts, THE Yukti_System SHALL accept Python-specific explanations and examples
5. THE Yukti_System SHALL handle Python debugging scenarios including common runtime errors and logical bugs

### Requirement 8: Text-Based Interaction Interface

**User Story:** As a user, I want a clean text-based interface for submitting questions and receiving guidance, so that I can focus on learning without interface distractions.

#### Acceptance Criteria

1. THE Yukti_System SHALL provide a text input interface for code and question submission
2. THE Yukti_System SHALL display concept questions in clear, readable text format
3. THE Yukti_System SHALL accept natural language explanations through text input
4. THE Yukti_System SHALL provide feedback and hints in structured text format
5. WHEN displaying code solutions, THE Yukti_System SHALL format them with proper syntax highlighting and indentation