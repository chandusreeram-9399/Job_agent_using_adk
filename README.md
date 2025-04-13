# Job Information Agent 🤖

A smart AI-powered agent that helps users find job openings, check application status, and get detailed information about available positions in a company.

## 🌟 Features

- 🔍 Search for job openings by department, location, and job title
- 📋 Get detailed information about specific positions
- 📊 Check application status
- 🎤 Voice and text interaction support
- 🔄 Real-time job status updates

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Google AI Studio API key
- Virtual environment (recommended)

### Installation

1. Clone the repository:
```bash
git clone  https://github.com/chandusreeram-9399/Job_agent_using_adk.git
cd job-info-agent
```

2. Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install google-adk
```

4. Set up your environment variables:
Create a `.env` file in the `job_info_agent` directory with:
```
GOOGLE_GENAI_USE_VERTEXAI="False"
GOOGLE_API_KEY="your-api-key-here"
```

### Running the Agent

1. Navigate to the project directory
2. Start the agent:
```bash
adk web
```
3. Open your browser and go to `http://localhost:8000`

## 💡 Usage Examples

### Finding Jobs
- "Show me Software Engineer jobs in New York"
- "What positions are available in the Engineering department?"
- "Find remote jobs"

### Getting Job Details
- "Tell me about the Software Engineer position"
- "What are the requirements for the Product Manager role?"

### Checking Application Status
- "What's the status of my application with ID 12345?"

## 🛠️ Project Structure

```
job_info_agent/
├── __init__.py
├── agent.py
└── .env
```

- `agent.py`: Contains the main agent implementation and job database
- `.env`: Configuration file for API keys and settings

## 📚 Job Database

The agent includes a sample job database with positions in:
- Software Engineering
- Product Management
- Data Science

Each job listing includes:
- Title
- Department
- Location
- Status
- Posting Date
- Requirements

## 🔧 Customization

### Adding New Jobs
Edit the `JOB_DATABASE` dictionary in `agent.py` to add new positions:
```python
JOB_DATABASE = {
    "new_position": {
        "title": "New Position",
        "department": "Department",
        "location": "Location",
        "status": "Open",
        "posted_date": "YYYY-MM-DD",
        "requirements": [
            "Requirement 1",
            "Requirement 2"
        ]
    }
}
```

### Modifying Search Logic
The search functions in `agent.py` can be customized to:
- Add new search criteria
- Modify filtering logic
- Change response format

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google ADK for the agent framework
- Gemini AI for the language model
- All contributors who help improve this project 