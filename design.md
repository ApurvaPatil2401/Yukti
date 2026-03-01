# Design Document

## Overview

Yukti – The Guarded IDE is a pedagogy-first AI coding mentor designed to enforce conceptual understanding before providing code solutions. The system introduces a guarded learning flow where users must explain programming concepts to unlock solutions, ensuring deep learning rather than superficial copy-pasting.

## System Architecture

The system follows a modular, AI-driven architecture consisting of the following high-level components:

- User Interface Layer
- Concept Analysis Engine
- Concept Question Generator
- Explanation Evaluation Engine
- Hint and Feedback Engine
- Solution Gate
- Learning Progress Tracker

## Component Design

### 1. User Interface Layer
- Accepts code submissions and coding questions
- Displays mandatory concept questions
- Collects natural language explanations from users
- Presents hints, feedback, and unlocked solutions

### 2. Concept Analysis Engine
- Analyzes submitted code or problem statements
- Identifies core programming concepts involved (e.g., recursion, complexity, data structures)
- Sends identified concepts to downstream components

### 3. Concept Question Generator
- Generates concept-specific questions based on identified concepts
- Ensures questions are mandatory before solution access
- Adapts question difficulty based on user history

### 4. Explanation Evaluation Engine
- Uses AI to evaluate free-text explanations
- Assesses correctness, depth, and conceptual clarity
- Classifies understanding as weak, sufficient, or strong

### 5. Hint and Feedback Engine
- Provides graduated hints when understanding is weak
- Breaks concepts into simpler sub-questions if needed
- Avoids revealing final solutions during learning phase

### 6. Solution Gate
- Controls access to the final code solution
- Unlocks solutions only after successful concept validation
- Ensures no partial code is leaked prematurely

### 7. Learning Progress Tracker
- Tracks user performance across concepts
- Stores weak and strong concept areas
- Influences future question difficulty and focus

## Data Flow

1. User submits code or question
2. Concept Analysis Engine detects relevant concepts
3. Concept Question Generator creates mandatory questions
4. User submits explanations
5. Explanation Evaluation Engine assesses understanding
6. Hint Engine assists if needed
7. Solution Gate unlocks solution upon validation
8. Learning Tracker updates user profile

## AI Usage Justification

Artificial Intelligence is essential for:
- Identifying concepts from arbitrary code
- Generating context-aware questions
- Evaluating natural language explanations
- Adapting difficulty dynamically per learner

These tasks cannot be effectively handled using rule-based systems.

## MVP Scope

- Python programming language support
- Text-based interaction
- Focus on DSA and debugging concepts
- Single-user learning flow
