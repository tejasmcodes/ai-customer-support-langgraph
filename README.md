# 🤖 AI-Powered Customer Support Automation System using LangGraph

> IBM Agentic AI Certification Assignment

## 📌 Project Overview

This project implements an **AI-Powered Customer Support Automation System** using **LangGraph**. It automates customer support by classifying customer queries, routing them to specialized support agents, retrieving relevant information from a local knowledge base (RAG), maintaining conversation history using SQLite, and handling high-risk requests through a Human-in-the-Loop approval workflow.

The project demonstrates the concepts of **Agentic AI**, **workflow orchestration**, **retrieval-augmented generation (RAG)**, **persistent memory**, and **supervisory approval**.

---

# 🚀 Features

* ✅ LangGraph Workflow Orchestration
* ✅ Intent Classification
* ✅ Conditional Routing
* ✅ Specialized Support Agents

  * Sales Agent
  * Technical Agent
  * Billing Agent
  * Account Agent
  * Memory Agent
* ✅ Lightweight RAG using Local Knowledge Base
* ✅ SQLite Conversation Memory
* ✅ Human-in-the-Loop Approval
* ✅ Supervisor Agent
* ✅ Local LLM using Ollama (Llama 3.2)

---

# 🏗️ Project Architecture

```text
                START
                  │
                  ▼
        Intent Classifier
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
 Sales      Technical      Billing
                              │
                    Requires Approval?
                       │           │
                       ▼           ▼
                      END    Supervisor
                                  │
                                  ▼
                                 END

     Account ─────────────► END

     Memory ──────────────► END
```

---

# 📂 Project Structure

```text
customer-support-langgraph/
│
├── app.py
├── graph.py
├── agents.py
├── supervisor.py
├── rag.py
├── memory.py
├── llm.py
├── state.py
├── workflow.py
├── requirements.txt
├── README.md
├── memory.db
│
├── data/
│   ├── pricing.txt
│   ├── policy.txt
│   ├── technical.txt
│   └── faq.txt
│
└── screenshots/
```

---

# ⚙️ Technologies Used

| Technology       | Purpose                |
| ---------------- | ---------------------- |
| Python           | Backend Development    |
| LangGraph        | Workflow Orchestration |
| LangChain        | LLM Integration        |
| Ollama           | Local LLM Runtime      |
| Llama 3.2        | AI Response Generation |
| SQLite           | Conversation Memory    |
| Local Text Files | Knowledge Base (RAG)   |

---

# 🔄 Workflow

1. Customer submits a query.
2. Intent Classifier identifies the intent.
3. LangGraph routes the request to the appropriate support agent.
4. The selected agent retrieves relevant context from the knowledge base.
5. Ollama (Llama 3.2) generates the response.
6. Billing requests requiring approval are routed to the Supervisor Agent.
7. Customer conversations are stored in SQLite.
8. Memory Agent retrieves previous conversations when requested.
9. Final response is returned to the customer.

---

# 🧠 Retrieval-Augmented Generation (RAG)

The system implements a lightweight local RAG pipeline.

Knowledge base files:

* `pricing.txt`
* `policy.txt`
* `technical.txt`
* `faq.txt`

Based on the detected intent, the appropriate document is retrieved and supplied as context to the LLM for response generation.

---

# 💾 SQLite Memory

The application stores customer conversations in a SQLite database.

Database:

```text
memory.db
```

Implemented functionality:

* Store customer queries
* Retrieve previous conversation
* Memory-based responses

---

# 👨‍💼 Human-in-the-Loop

Sensitive requests such as:

* Refund
* Subscription Cancellation
* Account Closure
* Compensation

are automatically routed to the **Supervisor Agent** before a final response is returned.

---

# 🤖 Supervisor Agent

The Supervisor Agent reviews and improves responses for sensitive customer requests before approving the final customer-facing response.

---

# 📸 Demonstration Queries

## Sales

```text
What are the pricing plans available for your software?
```

**Expected Route**

```text
Intent Classifier → Sales Agent
```

---

## Account

```text
I forgot my account password.
```

**Expected Route**

```text
Intent Classifier → Account Agent
```

---

## Technical

```text
My application crashes whenever I upload a file.
```

**Expected Route**

```text
Intent Classifier → Technical Agent
```

---

## Billing

```text
I need a refund for my annual subscription.
```

**Expected Route**

```text
Intent Classifier
        ↓
Billing Agent
        ↓
Supervisor Agent
```

---

## Memory

```text
I have a billing issue.
```

Then

```text
What was my previous support issue?
```

**Expected Route**

```text
Intent Classifier → Memory Agent
```

---

# 📷 Sample Execution Results

The following examples demonstrate the execution of the AI-Powered Customer Support Automation System. Corresponding screenshots are included in the `screenshots/` folder and the consolidated **Screenshots.pdf**.

---

## Example 1 – Sales Agent

**Input**

```text
What are the pricing plans available for your software?
```

**Expected Workflow**

```
Intent Classifier → Sales Agent
```

**Output**

* Intent detected as **Sales**
* Query routed to the **Sales Agent**
* Pricing information retrieved from the local knowledge base (RAG)
* Response generated using **Ollama (Llama 3.2)**

📷 **Screenshot:** `screenshots/sales_agent.png`

---

## Example 2 – Account Agent

**Input**

```text
I forgot my account password.
```

**Expected Workflow**

```
Intent Classifier → Account Agent
```

**Output**

* Intent detected as **Account**
* Query routed to the **Account Agent**
* Password recovery instructions generated using the knowledge base

📷 **Screenshot:** `screenshots/account_agent.png`

---

## Example 3 – Technical Agent

**Input**

```text
My application crashes whenever I upload a file.
```

**Expected Workflow**

```
Intent Classifier → Technical Agent
```

**Output**

* Intent detected as **Technical**
* Query routed to the **Technical Agent**
* Technical troubleshooting response generated using RAG

📷 **Screenshot:** `screenshots/technical_support.png`

---

## Example 4 – Billing Agent with Human-in-the-Loop

**Input**

```text
I need a refund for my annual subscription.
```

**Expected Workflow**

```
Intent Classifier
        ↓
Billing Agent
        ↓
Supervisor Agent
```

**Output**

* Intent detected as **Billing**
* Billing Agent identifies the request as requiring approval
* Request routed to the **Supervisor Agent**
* Final approved response returned to the customer

📷 **Screenshot:** `screenshots/billing_human_approval.png`

---

## Example 5 – Memory Agent

### Step 1

**Input**

```text
I have a billing issue.
```

The conversation is stored in the SQLite database.

📷 **Screenshot:** `screenshots/memory_storage.png`

### Step 2

**Input**

```text
What was my previous support issue?
```

**Expected Workflow**

```
Intent Classifier → Memory Agent
```

**Output**

* Previous customer interaction retrieved from SQLite
* Memory Agent returns the stored conversation

📷 **Screenshot:** `screenshots/memory_recall.png`

---

## SQLite Memory Verification

The SQLite database stores customer conversations and enables memory retrieval.

📷 **Screenshot:** `screenshots/sqlite_database.png`

---

## LangGraph Workflow

The LangGraph execution flow showing intent classification, conditional routing, specialized agents, and supervisor approval.

📷 **Workflow Diagram:** `workflow.png`

--- 

## 📈 Results Summary

| Feature               | Status       |
| --------------------- | ------------ |
| Intent Classification | ✅ Successful |
| LangGraph Routing     | ✅ Successful |
| Sales Agent           | ✅ Working    |
| Technical Agent       | ✅ Working    |
| Billing Agent         | ✅ Working    |
| Account Agent         | ✅ Working    |
| Memory Agent          | ✅ Working    |
| RAG Retrieval         | ✅ Working    |
| SQLite Memory         | ✅ Working    |
| Human-in-the-Loop     | ✅ Working    |
| Supervisor Agent      | ✅ Working    |

---

# 📊 Results

The system successfully demonstrates:

* Intent Classification
* Dynamic Agent Routing
* Retrieval-Augmented Generation (RAG)
* SQLite Conversation Memory
* Human-in-the-Loop Approval
* Supervisor Response Validation
* Local LLM Inference using Ollama

---

# 🛠️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd customer-support-langgraph
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

### Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Start Ollama:

```bash
ollama serve
```

Ensure the Llama 3.2 model is available:

```bash
ollama list
```

Run the application:

```bash
python app.py
```

---

# 📁 Submission Contents

* Source Code
* README.md
* Workflow Diagram
* Screenshots PDF
* SQLite Database (`memory.db`)
* Task Output Screenshots

---

# 🎯 Assignment Tasks Covered

| Task                  | Status |
| --------------------- | ------ |
| LangGraph Workflow    | ✅      |
| State Management      | ✅      |
| Intent Classification | ✅      |
| Conditional Routing   | ✅      |
| Specialized Agents    | ✅      |
| RAG Integration       | ✅      |
| SQLite Memory         | ✅      |
| Human-in-the-Loop     | ✅      |
| Supervisor Agent      | ✅      |
| Demonstration         | ✅      |

---

# 📄 License

This project was developed solely for the **IBM Agentic AI Certification Assignment** conducted through **AdroIT Technologies**.
# ai-customer-support-langgraph
