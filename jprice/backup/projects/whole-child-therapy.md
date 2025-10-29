# Whole Child Therapy Schedule Builder

**Type:** Client Project

**Date:** April 2025

---

## 📖 Overview

A scheduling application built for Whole Child Therapy, a provider of pediatric therapy services. They needed a tool to replace their increasingly unmanageable spreadsheet-based scheduling system. Previously it would take them several weeks to complete their quarterly schedule, and required a lot of training for their staff to create a conflict-free schedule. I was responsible for the full-stack development, including project planning, backend architecture, frontend design, and deployment.

---

## 🎯 Goals & Challenges

**Goals:**

- Efficient technician/client pairing based on several dynamic factors
- Database backed system for managing clients, technicians, availabilities and appointments
- Support all functions of existing spreadsheet system while improving usability

**Challenges:**

- Limited client budget
- Complex scheduling requirements involving multiple constraints
- Custom calendar interface for managing appointments

---

## 🧠 Approach & Implementation

I met with the client to discuss their existing scheduling process and understand their pain points. It was explained that this wasn't simply a matter of matching technicians and clients based off of availability. There was also taking into account factors such as location, therapy type, technician skill levels, and much more. The client also expressed a need for the system to allow you to override the constraints in certain situations, with a comphrehensive warning system to alert the user of potential conflicts.

They provided me with their existing spreadsheets, which had the following problems:

- Information was hard to parse due to the dense format of the sheets
- Finding a matchup was a grueling process and required significant understanding of the constraints
- Adding a new client or technician required updating multiple sheets
- Data inconsistencies were common due to manual entry across different sheets

I designed a relational database schema to represent the various entities and their relationships. I then built out the backend API using Django and Django REST Framework to handle CRUD operations and the matching and warning logic. On the frontend, I used React with shadcn/ui components and TailwindCSS to create a modern interface for managing clients, technicians, availabilities, and appointments. A custom calendar component was developed to visualize and manage appointments effectively.

---

## 💡 Key Features

- User authentication and role-based access
- CRUD operations for clients, technicians, availabilities, and appointments
- Dynamic multi-factor matching algorithm
- Conflict detection and warning system
- Highly optimized REST API
- Custom calendar interface for scheduling

---

## 🧩 Technical Highlights

- Utilized serializer `to_representation` methods for complex nested data structures in API responses.
- Highly optimized database queries with use of `prefetch_related` and `select_related` to minimize query counts.
- Custom middleware that allows switching between multiple schedules via an HTTP request header for sandboxing and archiving old schedules.
- Site-wide polling mechanism to keep appointment data in sync when multiple users are making changes.
- Maintain audit logs of schedule changes for accountability.
- Store client data securely with encryption at rest and in transit.
- Full test coverage for backend logic and API endpoints.

---

## 📊 Results & Impact

After finishing the initial version of the application I recorded a Loom video demonstrating it's capabilities and was told that when the client showed the video to their scheduling team "there was literal shrieks of joy". The client reported that the new system reduced their quarterly scheduling time from several weeks to just a few days. The system takes away much of the cognitive load of scheduling, allowing their team to focus on higher-level tasks. The client was extremely satisfied with the final product and we have continued to work together on adding new features and improvements. They are currently using the system as part of their daily operations.

---

## 🧭 Lessons Learned

I learned the value of deeply understanding client workflows before starting development. Early discussions with the scheduling team helped me identify key pain points and design a system that truly met their needs. This was also the first project I had built using shadcn/ui components and TailwindCSS, which I have since adopted into my standard toolkit when previously I primarily used SCSS and built custom component libraries. Overall, this project was a rewarding experience that strengthened both my technical skills and my ability to collaborate effectively with clients.

<!-- ---

## 🖼️ Visuals

Include screenshots, diagrams, or UI previews (optional but highly recommended): -->
