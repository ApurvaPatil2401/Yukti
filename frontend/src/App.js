import React, { useState, useEffect, useRef } from "react";
import axios from "axios";

function App() {
  const [problems, setProblems] = useState({});
  const [selected, setSelected] = useState("");
  const [messages, setMessages] = useState([]);
  const [answer, setAnswer] = useState("");
  const [solution, setSolution] = useState("");
  const [status, setStatus] = useState("locked");
  const [step, setStep] = useState(0);

  const chatEndRef = useRef(null);

  useEffect(() => {
    axios.get("https://yukti-backend.onrender.com")
      .then(res => setProblems(res.data));
  }, []);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const askQuestion = async () => {
    if (!selected) return;

    setSolution("");
    setStatus("locked");
    setMessages([]);
    setStep(1);

    const res = await axios.post(
      "http://localhost:8000/ask",
      null,
      { params: { problem_key: selected } }
    );

    setMessages([
      { role: "mentor", content: res.data.question }
    ]);
  };

  const submitAnswer = async () => {
    if (!answer.trim()) return;

    const updatedMessages = [
      ...messages,
      { role: "user", content: answer }
    ];

    setMessages(updatedMessages);

    const res = await axios.post(
      "http://localhost:8000/evaluate",
      null,
      {
        params: {
          problem_key: selected,
          user_answer: answer
        }
      }
    );

    if (res.data.status === "unlocked") {
      setSolution(res.data.solution);
      setStatus("unlocked");
      setStep(2);

      setMessages([
        ...updatedMessages,
        {
          role: "mentor",
          content: "Excellent. Concept validated. Unlocking solution."
        }
      ]);
    }
    else if (res.data.status === "continue") {
      setStep(2);

      setMessages([
        ...updatedMessages,
        {
          role: "mentor",
          content: res.data.question
        }
      ]);
    }
    else {
      setMessages([
        ...updatedMessages,
        {
          role: "mentor",
          content: res.data.hint
        }
      ]);
    }

    setAnswer("");
  };

  return (
    <div style={styles.page}>
      <div style={styles.container}>

        <h1 style={styles.title}> Yukti – The Guarded IDE </h1>

        {/* Problem Selector */}
        <div style={styles.selectorRow}>
          <select
            value={selected}
            onChange={(e) => setSelected(e.target.value)}
            style={styles.select}
          >
            <option value="">Select Problem</option>
            {Object.keys(problems).map((key) => (
              <option key={key} value={key}>{key}</option>
            ))}
          </select>

          <button
            onClick={askQuestion}
            style={styles.startButton}
          >
            Start
          </button>
        </div>

        {/* Step Indicator */}
        {step > 0 && (
          <div style={styles.stepIndicator}>
            <div style={{
              ...styles.stepCircle,
              background: step >= 1 ? "#38bdf8" : "#1e293b"
            }}>1</div>

            <div style={styles.stepLine}></div>

            <div style={{
              ...styles.stepCircle,
              background: step >= 2 ? "#38bdf8" : "#1e293b"
            }}>2</div>
          </div>
        )}

        {/* Chat Card */}
        <div style={styles.chatCard}>
          {messages.map((msg, index) => (
            <div
              key={index}
              style={{
                display: "flex",
                justifyContent:
                  msg.role === "user" ? "flex-end" : "flex-start",
                marginBottom: "12px"
              }}
            >
              <div style={{
                ...styles.messageBubble,
                background:
                  msg.role === "user" ? "#2563eb" : "#1e293b"
              }}>
                {msg.content}
              </div>
            </div>
          ))}
          <div ref={chatEndRef}></div>
        </div>

        {/* Input */}
        {messages.length > 0 && status !== "unlocked" && (
          <div style={styles.inputRow}>
            <input
              type="text"
              value={answer}
              onChange={(e) => setAnswer(e.target.value)}
              placeholder="Explain your reasoning..."
              style={styles.input}
            />
            <button
              onClick={submitAnswer}
              style={styles.submitButton}
            >
              Submit
            </button>
          </div>
        )}

        {/* Solution */}
        {status === "unlocked" && (
          <div style={styles.solutionCard}>
            <h3>Unlocked Solution</h3>
            <pre style={{ margin: 0 }}>{solution}</pre>
          </div>
        )}

      </div>
    </div>
  );
}

const styles = {
  page: {
    minHeight: "100vh",
    background: "linear-gradient(135deg, #2b274e, #44486d)",
    color: "#e2e8f0",
    display: "flex",
    justifyContent: "center",
    padding: "40px 20px",
    fontFamily: "Inter, sans-serif",
    transition: "all 0.3s ease"
  },
  container: {
    width: "100%",
    maxWidth: "800px"
  },
  title: {
    color: "#39c4c9",
    marginBottom: "30px",
    textAlign: "center"
  },
  selectorRow: {
    display: "flex",
    gap: "10px",
    marginBottom: "20px"
  },
  select: {
    flex: 1,
    padding: "10px",
    background: "#1e293b",
    color: "white",
    border: "1px solid #334155",
    borderRadius: "6px"
  },
  startButton: {
    padding: "10px 16px",
    background: "#38bdf8",
    border: "none",
    borderRadius: "6px",
    cursor: "pointer",
    fontWeight: "bold"
  },
  stepIndicator: {
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    marginBottom: "20px"
  },
  stepCircle: {
    width: "32px",
    height: "32px",
    borderRadius: "50%",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    fontWeight: "bold",
    transition: "all 0.3s ease"
  },
  stepLine: {
    width: "50px",
    height: "2px",
    background: "#2b2c66"
  },
  chatCard: {
    background: "#191641",
    padding: "20px",
    borderRadius: "10px",
    minHeight: "300px",
    boxShadow: "0 8px 24px rgba(0,0,0,0.4)",
    marginBottom: "15px",
    transition: "all 0.3s ease"
  },
  messageBubble: {
    padding: "10px 14px",
    borderRadius: "15px",
    maxWidth: "75%",
    transition: "all 0.2s ease"
  },
  inputRow: {
    display: "flex",
    gap: "10px"
  },
  input: {
    flex: 1,
    padding: "10px",
    background: "#1c1c36",
    border: "1px solid #334155",
    borderRadius: "6px",
    color: "white"
  },
  submitButton: {
    padding: "10px 16px",
    background: "#1bbd1b",
    border: "none",
    borderRadius: "6px",
    cursor: "pointer",
    fontWeight: "bold"
  },
  solutionCard: {
    marginTop: "20px",
    background: "#064e3b",
    padding: "20px",
    borderRadius: "10px",
    boxShadow: "0 6px 20px rgba(0,0,0,0.3)"
  }
};

export default App;
