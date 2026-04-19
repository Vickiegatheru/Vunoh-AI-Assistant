# Vunoh Global AI Assistant

An intelligent AI-powered web application that helps Kenyans living abroad manage important tasks back home—sending money, hiring services, and verifying documents.

## Features

- **AI Intent Extraction**: Uses OpenAI to understand customer requests and extract structured data
- **Risk Scoring**: Intelligent risk assessment based on diaspora context (urgency, amounts, verification status)
- **Task Management**: Create, track, and manage tasks with unique codes
- **Multi-Channel Messaging**: Auto-generates WhatsApp, Email, and SMS messages for each task
- **Employee Assignment**: Automatically routes tasks to appropriate teams (Finance, Legal, Operations)
- **Task Dashboard**: Real-time task tracking with status updates

## Tech Stack

- **Backend**: Django 6.0.4 (Python)
- **Frontend**: HTML, CSS, Vanilla JavaScript
- **Database**: SQLite
- **AI**: OpenAI GPT-3.5-turbo
- **Environment**: Virtual Environment (Python 3.12)

## Setup Instructions

### Prerequisites
- Python 3.12+
- pip package manager
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-link>
   cd "Vunoh AI Assistant"
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\Activate.ps1
   # On Mac/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django requests python-dotenv
   ```

4. **Configure environment variables**
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   Open your browser and navigate to `http://127.0.0.1:8000/`

## Project Structure

```
Vunoh AI Assistant/
├── assistant/
│   ├── migrations/          # Database migrations
│   ├── templates/
│   │   └── assistant/
│   │       └── dashboard.html
│   ├── models.py           # Task model definition
│   ├── views.py            # Request processing logic
│   ├── utils.py            # AI integration and processing
│   ├── admin.py
│   ├── apps.py
│   └── tests.py
├── vunoh_project/
│   ├── settings.py         # Django configuration
│   ├── urls.py             # URL routing
│   ├── asgi.py
│   └── wsgi.py
├── db.sqlite3              # Database
├── manage.py               # Django management script
├── .env                    # Environment variables (not in repo)
└── README.md
```

## How It Works

### 1. User Submits Request
Customer enters a request like: "I need to send KES 15,000 to my sister in Kisumu urgently"

### 2. AI Processing
- System prompt designed to extract structured JSON with intent, entities, steps, and messages
- OpenAI GPT-3.5-turbo processes the request
- Fallback to mock responses if API key missing (demo mode)

### 3. Risk Scoring
Risk score calculated based on:
- **Urgency**: +30 points if "urgent" detected
- **Document Verification**: +40 points (higher risk category)
- **Base Risk**: 20 points (all tasks)
- **Total Range**: 20-90 points

### 4. Task Creation
- Generate unique task code: `VNH-XXXXXX`
- Store intent, entities, risk score, steps, messages, and team assignment
- Task appears immediately in dashboard

### 5. Multi-Channel Messages
AI generates three distinct message formats:
- **WhatsApp**: Conversational, emoji, line breaks for readability
- **Email**: Formal, structured, full details and task code
- **SMS**: Under 160 chars, task code and key info only

### 6. Dashboard Display
- View all tasks with status (Pending, In Progress, Completed)
- Update status via dropdown
- See risk scores and team assignments at a glance

## Decisions I Made and Why

### 1. Technology Choices

**Why Django over Flask?**
- More built-in functionality (ORM, admin panel, migration system)
- Requirement mentioned Vunoh uses Django internally
- Better for scaling to a larger application
- Cleaner separation of concerns

**Why SQLite?**
- Perfect for a 4-day project scope
- No external database setup needed
- Easy to create SQL dump for submission
- Can easily migrate to PostgreSQL later

**Why OpenAI over other LLMs?**
- Most reliable and consistent intent extraction
- Well-documented API
- Free tier available
- System prompts work reliably for structured output

### 2. AI System Prompt Design

**What I included:**
- Explicit output format (strict JSON)
- Five specific intents (send_money, hire_service, verify_document, get_airport_transfer, check_status)
- Required fields (entities, steps, messages)
- Three distinct message formats with clear style guidelines

**What I excluded:**
- Complex multi-turn conversation (not needed for one-off requests)
- Sentiment analysis (not required)
- Duplicate intents (kept it simple and clear)

**Why this works:**
- Clear structure makes parsing reliable
- Specific intent list prevents hallucination
- Message style guidelines ensure distinct outputs
- JSON format is parseable and consistent

### 3. Risk Scoring Logic

**Decision: Context-aware, not generic**
Instead of arbitrary point systems, I based scoring on real diaspora scenarios:
- Urgency matters: urgent + money = higher risk
- Document verification is inherently higher risk (legal implications)
- Base score of 20 ensures all tasks are tracked
- Maximum of 90 keeps scores within reasonable range

**Alternative I considered:**
- Machine learning model (too complex for 4 days)
- Simple random scores (meaningless)
- Flat scoring for everything (doesn't reflect reality)

I chose rule-based logic because it's explainable, maintainable, and grounded in business logic.

### 4. Message Generation Strategy

**Decision: Let AI generate all three formats**
Rather than templates, I let the AI understand each format's requirements:
- WhatsApp: "Conversational with emojis"
- Email: "Formal and structured"
- SMS: "Under 160 characters"

**Why this worked:**
- More natural and varied outputs
- AI understands nuance better than templates
- Less code to maintain

### 5. Error Handling Decision

**What didn't work initially:**
- Strict OpenAI requirement would crash the app without API key
- This broke the 4-day testing window

**How I fixed it:**
- Implemented graceful fallback to mock responses
- Mock responses use keyword detection for intent classification
- Same data structure ensures frontend compatibility
- Users can still test full app in "demo mode"

**Why this decision:**
- Enables testing without API delays
- Provides offline functionality
- More resilient application overall

### 6. Task Code Generation

**Decision: Short, memorable codes (VNH-XXXXXX)**
- VNH = Vunoh prefix
- 6 random hex characters = 16.7 million combinations
- Short enough to communicate via phone
- Unique and trackable

Alternative considered: UUIDs (too long for SMS/voice)

### 7. Frontend Simplicity

**Decision: Vanilla JavaScript, no frameworks**
- No build step required
- Simpler deployment
- Meets requirements exactly
- Easier to debug

## Database Schema

```sql
CREATE TABLE assistant_task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_code VARCHAR(12) UNIQUE NOT NULL,
    intent VARCHAR(50) NOT NULL,
    entities JSON NOT NULL,
    risk_score INTEGER NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending',
    steps JSON NOT NULL,
    whatsapp_msg TEXT NOT NULL,
    email_msg TEXT NOT NULL,
    sms_msg TEXT NOT NULL,
    assigned_to VARCHAR(100) NOT NULL,
    created_at DATETIME AUTO_NOW_ADD
);
```

## Sample Data

See `database_dump.sql` for complete schema and 5 sample tasks with full data.

## Deployment

Optional: Deploy to free hosting
- **Railway**: https://railway.app
- **Render**: https://render.com
- **Vercel**: https://vercel.com (frontend only)

## Known Limitations

1. No user authentication (not required for MVP)
2. No email sending (mock stored in DB)
3. No real payment processing (message generation only)
4. Single database (no read replicas)
5. No rate limiting (appropriate for internship project)

## Future Enhancements

- User accounts and history
- Real SMS/Email delivery
- Payment gateway integration
- WhatsApp API integration
- Real employee database
- Advanced analytics dashboard
- Audit trail logging

## Testing

To test the application:
1. Submit requests with different keywords (money, verify, hire, airport)
2. Observe intent extraction accuracy
3. Check risk scores are appropriate
4. Verify messages are in correct format
5. Update task statuses and confirm persistence

## Troubleshooting

**Issue: "OPENAI_API_KEY environment variable not set"**
- Ensure `.env` file exists in project root
- Verify key is correctly copied
- Restart server to reload environment

**Issue: Tasks not appearing in dashboard**
- Run migrations: `python manage.py migrate`
- Check database has data: Open Django admin at `/admin`

**Issue: Port 8000 already in use**
- Use different port: `python manage.py runserver 8001`

## License

Confidential — Vunoh Global AI Internship 2026

## Contact

For questions about this project, contact the Vunoh Global team.
