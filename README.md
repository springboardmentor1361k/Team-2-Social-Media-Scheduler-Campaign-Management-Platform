# Social Media Scheduler & Campaign Management Platform

A web-based Social Media Scheduler and Campaign Management Platform developed as part of the Infosys Virtual Internship.

The platform is designed to help users manage social media accounts, create and schedule posts, organize campaigns, track campaign performance, and generate useful analytics and reports from a centralized platform.

---

## 📌 Project Overview

Managing multiple social media platforms manually can be time-consuming and difficult to organize. This project aims to provide a centralized platform where users can manage their social media activities from a single application.

The system combines:

- User authentication and account management
- Social media account management
- Post creation and management
- Post scheduling
- Campaign management
- Campaign tracking
- Analytics and reporting
- Database management
- Testing and deployment

The project is developed collaboratively by a team of seven members, with each member responsible for a specific technical area.

---

## 🎯 Objectives

The main objectives of this project are:

- Build a centralized social media management platform.
- Allow users to manage social media accounts.
- Provide functionality for creating and managing posts.
- Schedule posts for future publishing.
- Organize social media activities into campaigns.
- Track campaign performance and engagement.
- Generate campaign and performance reports.
- Provide analytics through dashboards.
- Implement secure user authentication.
- Maintain a structured and scalable backend and database.
- Follow collaborative GitHub-based development practices.

---

## ✨ Key Features

### 👤 User Authentication & Management

- User registration
- User login
- Secure authentication
- User account management
- Protected application resources
- User-specific data management

### 📱 Social Media Account Management

- Connect social media accounts
- Manage connected accounts
- Store account-related information
- Manage account associations with posts and campaigns

### 📝 Post Management

- Create posts
- Edit posts
- Delete posts
- Manage post content
- Associate posts with social media accounts
- Track post status

### 📅 Post Scheduling

- Schedule posts for future publication
- Manage scheduled posts
- Track scheduled post status
- Support campaign-based scheduling

### 📢 Campaign Management

- Create campaigns
- Update campaigns
- Delete campaigns
- Manage campaign details
- Associate posts with campaigns
- Track campaign progress

### 📊 Campaign Tracking

- Monitor campaign activities
- Track post performance
- Track engagement
- Analyze campaign results
- Compare campaign performance

### 📈 Analytics

- Engagement analytics
- Audience growth tracking
- Campaign performance analysis
- Social media performance metrics
- Campaign comparison
- ROI-related reporting

### 📄 Reports

- Campaign reports
- Performance reports
- Audience growth reports
- Engagement reports
- Campaign comparison reports
- ROI reports

### 📊 Analytics Dashboard

The platform can provide interactive dashboards for visualizing:

- Campaign performance
- Engagement metrics
- Audience growth
- Post performance
- Campaign comparisons
- Overall social media activity

---

# 🏗️ Project Architecture

The project follows a modular architecture consisting of frontend, backend, database, and testing components.

```text
                    ┌─────────────────────┐
                    │        User         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Frontend       │
                    │      UI / UX        │
                    └──────────┬──────────┘
                               │
                         API Requests
                               │
                               ▼
                    ┌─────────────────────┐
                    │       Backend       │
                    │   REST API Layer    │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       Authentication     Campaigns         Scheduling
              │                │                │
              └────────────────┼────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Database       │
                    │ Users / Posts /     │
                    │ Campaigns / Accounts│
                    └─────────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Analytics & Reports │
                    └─────────────────────┘
