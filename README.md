# Tutor Booking App

A lightweight Django app built from a simulated client brief for a small local tutoring service — replacing manual WhatsApp booking coordination with a simple, admin-managed booking system.

## Project Context
This project was built as a requirements-gathering exercise: instead of a fixed spec, I worked from a short, deliberately vague client brief and had to ask clarifying questions before writing any code — deciding what to build (and what *not* to build) based on the client's actual constraints ("keep it simple, budget's tight"), not just technical possibility.

## Features
- Public tutor list with subject and bio
- Tutor detail page with a session request form (no login required for students)
- All bookings start as "Pending" — nothing auto-confirms, matching the client's requirement that they personally review every request
- Full booking management through Django's built-in admin — no custom admin UI was built, since the client's needs (view, confirm, decline) were already well served by Django admin's defaults
- Custom Django admin bulk actions ("Mark as Confirmed" / "Mark as Declined") for handling multiple requests at once
- Real email notifications sent to students automatically when their booking's status changes — covering both single-record edits and bulk admin actions, which use two different underlying Django admin code paths

## Tech Stack
- Python, Django
- SQLite
- Django Admin (customized: `list_display`, `list_filter`, `search_fields`, custom actions)
- SMTP email (Gmail) with credentials handled via environment variables

## Design Decisions
- **No student or tutor accounts** — the client explicitly didn't want login complexity for either group; tutors are added manually by the admin via Django admin
- **No custom "accept/decline" page** — Django's built-in admin already covers this need well, so building a separate interface would have added unnecessary complexity for no real benefit
- **Considered adding a `price` field to tutors, but held off** — the client never mentioned pricing, and adding unrequested scope without checking first isn't a great habit, even in a practice project

## Running Locally
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with:
   ```
   EMAIL_HOST_USER=your-gmail-address@gmail.com
   EMAIL_HOST_PASSWORD=your-gmail-app-password
   ```
   (Use a [Gmail App Password](https://myaccount.google.com/apppasswords), not your normal password)
   
4. Run migrations: `python manage.py migrate`
5. Create an admin account: `python manage.py createsuperuser`
6. Add a few tutors via `/admin/`
7. Start the server: `python manage.py runserver`
8. Visit `http://127.0.0.1:8000/`

*Note: this project isn't deployed live due to hosting platform project limits on the free tier — see my [Django Blog Platform](https://github.com/Hafizatif23/django-blog-app) for a fully deployed example including production database, image storage, and static file configuration.*