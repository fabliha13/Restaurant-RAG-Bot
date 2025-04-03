# 🚀 Local AI Agent with RAG & LangChain

## **Overview**
This project implements a **Retrieval-Augmented Generation (RAG)** system using **Llama 3.2** via **Ollama**. The AI agent is designed to extract precise answers from a **custom dataset** containing customer reviews for a restaurant. By integrating **LangChain**, the model efficiently retrieves relevant context before generating responses, ensuring accurate and context-aware outputs.

## **🛠️ Features**
- **🔍 RAG-based Query Handling**: Uses **vector embeddings** to fetch relevant information before generating responses.
- **📖 Custom Dataset Integration**: Extracts insights from a structured dataset of restaurant customer reviews.
- **🧠 Llama 3.2 via Ollama**: Efficiently processes user queries with optimized response generation.
- **⚡ Fast and Local Execution**: No external API calls—everything runs locally for **privacy and speed**.
- **🛠 LangChain-powered Retrieval**: Enhances response accuracy by selecting the most relevant context.
- **🌐 Streamlit Web Interface**: Provides a **user-friendly** web UI for interaction.

## **🚀 Installation & Setup**
### **1️⃣ Prerequisites**
- **Python 3.8+**
- **Ollama installed** ([Installation Guide](https://ollama.com))
- **Required Python libraries**

### **2️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/local-ai-agent.git
cd local-ai-agent
```

### **3️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### **4️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **5️⃣ Run the AI Agent in Terminal**
```bash
python main.py
```

### **6️⃣ Run the AI Agent on Streamlit**
```bash
streamlit run app.py
```
This will launch a **web-based UI** on `localhost` where users can interact with the AI agent.

## **💡 How It Works**
1. **User Inputs Query** → Enters a restaurant-related question.
2. **Vector Search (RAG)** → Retrieves relevant customer reviews from the dataset.
3. **Llama 3.2 Processes Input** → Generates an accurate response based on retrieved context.
4. **Response Displayed** → The AI agent provides an insightful answer.
5. **Streamlit Web Interface** → Users can interact via a web-based UI.


## **🎯 Future Enhancements**
- ✅ Improved ranking for retrieved documents
- ✅ Support for additional datasets
- ✅ Cloud deployment for remote access

## **🤝 Contributing**
Contributions are welcome! Feel free to **fork** this repo, submit PRs, or suggest improvements. 🚀

## **📜 License**
This project is open-source under the **MIT License**.
