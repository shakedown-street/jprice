## Overview

PunkwebUI is a lightweight open source (BSD-3 Clause) CSS framework that can be used as a standalone minified CSS file or installed via npm for use in frontend build systems. It focuses on sensible classless defaults for semantic HTML, [TailwindCSS](https://tailwindcss.com/) inpsired utility clases, and essential UI components. I handled the full design and implementation of the framework.

---

## Goals & Challenges

**Goals:**

- Facilitate rapid prototyping and development
- Focus on semantic HTML with classless defaults
- Include TailwindCSS inspired utility classes for rapid styling in HTML
- Offer essential UI components (buttons, dialogs, forms, etc.)
- Enable easy theming and customization through CSS variables
- Support both standalone CSS file and npm package installation
- Ensure compatibility with popular frontend frameworks (React, Vue, etc.)
- Support dark mode styling options

**Challenges:**

- Balancing simplicity with flexibility for various use cases
- Designing a coherent set of utility classes without overwhelming users
- Building a theming system that is easy to use and understand
- Maintaining performance and small file size while including useful features
- Ensuring cross-browser compatibility and accessibility standards

---

## Approach & Implementation

The project is built with [SCSS](https://sass-lang.com/) to leverage its features like variables, mixins, and nesting for better organization and maintainability. I structured the framework into several key sections: base styles, utility classes, and components. It uses the TailwindCSS color palette exposed as root CSS variables, ensuring a modern and visually appealing design. The theming system is built around CSS variables, allowing developers to easily customize colors, fonts, and other design aspects without modifying the core CSS.

The base styles provide sensible defaults for HTML elements, ensuring that even without any classes applied, the UI looks clean and modern. The utility classes are inspired by TailwindCSS, allowing developers to quickly apply common styles directly in their HTML. Finally, the components section includes pre-designed UI elements like badges, buttons, inputs, dialogs, and forms.

---

## Key Features

- Classless base styles for semantic HTML
- TailwindCSS inspired utility classes for rapid styling
- Essential UI components (buttons, dialogs, forms, etc.)
- Theming system using CSS variables for easy customization
- Dark mode support
- Available as standalone CSS or npm package

---

## Technical Highlights

- Created a modular SCSS structure for easy maintenance and scalability
- Developed a theming system using CSS variables for straightforward customization
- Implemented dark mode support with a simple data attribute toggle
- Achieved a small file size (~30KB minified) while including essential features

---

## Results & Impact

I have used PunkwebUI in several personal projects including this site and PunkwebBB, demonstrating its versatility and effectiveness. I have found that the classless design and utility classes facilitate rapid prototyping well.

---

## Lessons Learned

Through several design iterations, I learned how to strike a balance between simplicity and flexibility. Initial versions were too complex, so I refocused on core principles of semantic HTML. I also gained experience in building a theming system using CSS variables. Overall, building PunkwebUI gave me a great opportunity to deepen my understanding of CSS architecture and design systems.
