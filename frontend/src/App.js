import React, { useState, useEffect, useRef } from "react";
import axios from "axios";

function App() {
  const [problems, setProblems] = useState({});
  const [selected, setSelected] = useState("");
  const [messages, setMessages] = useState([]);
  const [answer, setAnswer] = useState("");
  const [solution, setSolution] = useState("");
  const [status, setStatus] = useState("locked");

  const chatEndRef = useRef(null);

  useEffect(() => {
    axios.get("http://localhost:8000/problems")
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

    const res = await axios.post(
      "http://localhost:8000/ask",
      null,
      { params: { problem_key: selected } }
    );

    setMessages([
      {
        role: "mentor",
        content: res.data.question
      }
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

      setMessages([
        ...updatedMessages,
        {
          role: "mentor",
          content: "Excellent. You’ve demonstrated strong conceptual understanding. Unlocking solution."
        }
      ]);
    }
    else if (res.data.status === "continue") {
      setMessages([
        ...updatedMessages,
        {
          role: "mentor",
          content: "Good. Let’s go one level deeper.\n\n" + res.data.question
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
    <div style={{
      minHeight: "100vh",
      backgroundColor: "#0f172a",
      color: "#e2e8f0",
      padding: "30px",
      fontFamily: "Segoe UI"
    }}>
      <h1 style={{ color: "#38bdf8" }}>🧠 Yukti – The Guarded IDE</h1>

      <div style={{ marginBottom: "20px" }}>
        <select
          value={selected}
          onChange={(e) => setSelected(e.target.value)}
          style={{ padding: "8px", background: "#1e293b", color: "white" }}
        >
          <option value="">-- Choose Problem --</option>
          {Object.keys(problems).map((key) => (
            <option key={key} value={key}>{key}</option>
          ))}
        </select>

        <button
          onClick={askQuestion}
          style={{
            marginLeft: "10px",
            padding: "8px 12px",
            background: "#38bdf8",
            border: "none",
            cursor: "pointer"
          }}
        >
          Start
        </button>
      </div>

      {/* Chat */}
      <div style={{
        background: "#7ba1dd",
        padding: "20px",
        height: "350px",
        overflowY: "auto",
        borderRadius: "8px",
        marginBottom: "10px"
      }}>
        {messages.map((msg, index) => (
          <div
            key={index}
            style={{
              marginBottom: "10px",
              display: "flex",
              justifyContent: msg.role === "user" ? "flex-end" : "flex-start"
            }}
          >
            <div style={{
              background: msg.role === "user" ? "#2563eb" : "#334155",
              padding: "10px 15px",
              borderRadius: "15px",
              maxWidth: "70%"
            }}>
              {msg.content}
            </div>
          </div>
        ))}
        <div ref={chatEndRef}></div>
      </div>

      {/* Input */}
      {messages.length > 0 && status !== "unlocked" && (
        <div>
          <input
            type="text"
            value={answer}
            onChange={(e) => setAnswer(e.target.value)}
            placeholder="Explain your understanding..."
            style={{
              width: "80%",
              padding: "10px",
              background: "#1e293b",
              color: "white",
              border: "1px solid #334155"
            }}
          />
          <button
            onClick={submitAnswer}
            style={{
              marginLeft: "10px",
              padding: "10px 15px",
              background: "#38bdf8",
              border: "none",
              cursor: "pointer"
            }}
          >
            Submit
          </button>
        </div>
      )}

      {/* Solution */}
      {status === "unlocked" && (
        <div style={{
          marginTop: "20px",
          background: "#064e3b",
          padding: "20px",
          borderRadius: "8px"
        }}>
          <h3>Unlocked Solution</h3>
          <pre>{solution}</pre>
        </div>
      )}
    </div>
  );
}

export default App;