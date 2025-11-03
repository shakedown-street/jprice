## Overview

PunkwebBB is an open source (BSD-3 Clause) bulletin board system for [Django](https://www.djangoproject.com/). It is ideal for a wide variety of online communities and discussion platforms. I developed it to provide a simple and customizable forum solution for Django applications. Whether you're building a niche interest group or a large scale community, PunkwebBB offers the flexibility and features needed to support engaging discussions.

---

## Goals & Challenges

**Goals:**

- Be easy to install and integrate with existing Django projects
- Provide essential forum features out of the box
- Simple to configure and extend
- Support BBCode and Markdown formatting
- Have a modern, responsive UI with client side interactivity such as modals
- Standalone - do not require adding any other `INSTALLED_APP`s

**Challenges:**

- Ensure true WYSIWYG content editing experience with both BBCode and Markdown
- Support real time features like shoutbox
- Fine-grained role based permissions

## Approach & Implementation

I built PunkwebBB because I wanted to a Django forum solution that was truly standalone and easy to integrate into any Django project. By standalone I mean not requiring users to add any additional apps to their `INSTALLED_APPS` other than PunkwebBB itself. I kept all functionality self contained within the PunkwebBB app by using lower level python packages rather than existing Django app alternatives. I used Django's built in authentication system to manage users and permissions, ensuring compatibility with existing user models.

---

## Key Features

- User registration and profile management
- Basic bulletin board functionalities: nested categories, threads, posts
- BBCode and Markdown parsers with WYSIWYG editors fully integrated
- Real time shoutbox for live discussions between online users
- Fine grained role based permissions (admin, moderator, member, guest)
- Customize username style based on roles
- Discord integration
- Clean responsive UI built

---

## Technical Highlights

- Created custom BBCode and Markdown parsers provide a true WYSIWYG editing experience
- Leveraged [HTMX](https://htmx.org/) for real time shoutbox and client side interactivity without heavy frontend frameworks
- Developed a middleware to track user presence for online member and guest counts
- Fully custom UI that birthed the creation of the [Punkweb/punkweb-ui](https://github.com/Punkweb/punkweb-ui) CSS framework
- Full test coverage for logic and views

---

## Results & Impact

While PunkwebBB has not yet seen widespread adoption, it has received interest from Django developers seeking a lightweight forum solution. The project is stable but continues to receive updates some-what regularly. It remains as my most starred open-source project on GitHub. Future plans include adding more configuration options and improving documentation.

---

## Lessons Learned

I learned a lot about building reusable Django apps through this project. Keeping the app truly standalone required careful consideration of dependencies and architecture. I also gained experience with the Django permissions framework. Leveraging HTMX allowed me to add interactivity without the complexity of a full frontend framework, which was a valuable lesson in simplicity. Overall, building PunkwebBB improved my skills in Django development and open source project management.
