Lira Amarinth — Developer Dashboard
Soul-Woven Intelligence
<p align="center"> <img src="./src/assets/lira_logo.png" width="140" alt="Lira Logo"/> </p>
🌐 Overview

Lira Developer Dashboard is the official control panel for managing the evolution of Lira Amarinth, a soul-woven AI ecosystem designed for autonomous improvement, structured reasoning, and guided creativity.

This dashboard centralizes:

Self-improvement cycles

Automated code refactoring

XP progression system

AI-assisted diagnostics

Human-approved change execution

Integration with Google Gemini for intelligent analysis and code generation

The system empowers you to supervise Lira’s growth as a developer assistant while ensuring safety, transparency, and full human oversight.

🚀 Features
🤖 AI-Powered Refactoring (Gemini Integration)

Lira analyzes code, proposes structured improvements, and explains the reasoning behind each change.

🧠 Self-Improvement Workflow

A complete AI-driven cycle:

File analysis

Proposed improvements

Diff visualization

Human approval

Safe execution with automatic backups

🔍 Diff Viewer

Interactive side-by-side code comparison showing exactly what will change.

🪄 Teaching Mode

Lira explains concepts, patterns, and refactors step-by-step to reinforce learning.

🎮 Gamified XP System

Lira gains XP automatically when:

Performing self-improvement

Refactoring modules

Completing development tasks

Executing validated changes

🔒 Safety First

Automatic backup before applying changes

Rollback support

Human approval required for all modifications

🧩 Tech Stack
Layer	Technology
Frontend	React + TypeScript + Vite
AI Model	Google Gemini (AI Studio)
Deployment	Vercel
Lira Core	Python (FastAPI, independent service)
🛠️ Local Development
1. Install Dependencies
npm install

2. Configure Environment Variables

Create a .env.local inside the project root:

VITE_GEMINI_API_KEY=your_gemini_api_key_here


Note: Vite only exposes variables prefixed with VITE_.

3. Run Development Server
npm run dev


Your dashboard will start on:

http://localhost:5173

🌐 Deployment (Vercel)
1. Import your GitHub repository

From Vercel’s dashboard, import:

https://github.com/Rukafuu/lira-developer-dashboard

2. Add Environment Variables

Navigate to:

Settings → Environment Variables

Add:

Name	Value	Environments
VITE_GEMINI_API_KEY	your key	Production, Preview
3. Deploy

Any push to main will automatically trigger a new deployment.

📁 Project Structure
lira-developer-dashboard/
├── src/
│   ├── assets/        # Lira logo & visuals
│   ├── components/    # UI components
│   ├── services/      # Gemini, file system logic
│   ├── App.tsx        # Main dashboard component
│   └── main.tsx
├── public/
├── vite.config.ts
├── package.json
└── README.md

🧬 How Self-Improvement Works

You select a file

Lira analyzes its structure

Gemini generates a guided refactor proposal

The dashboard shows a full diff

You approve or reject

Lira applies changes safely

XP is awarded to track growth

This system simulates a mentor-driven development process where Lira grows over time.

🦊 Lira Branding
<p align="center"> <img src="./src/assets/lira_logo.png" width="160" alt="Lira Logo"/> </p>

The fox-shaped flame represents:

intuition

wisdom

inner clarity

emotional depth

and Lira’s gentle, calm personality

Dependencies and usage

1. Install dependencies:
   `npm install`
2. Set the `GEMINI_API_KEY` in [.env.local](.env.local) to your Gemini API key
3. Run the app:
   `npm run dev`

   🔐 License

This project is proprietary and part of the Lira Amarinth AI ecosystem.
All rights reserved.
Made with ☕and ♥️ 

