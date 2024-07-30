---
title: "Creating a To-Do List App with Vue 3: A Beginner's Project"
date: 2024-07-25 20:27:12
keywords: "Vue 3, To-Do List, Vue Tutorial, JavaScript, Web Development, Beginner Project"
description: "In this detailed guide, we will embark on creating a simple To-Do list application using Vue 3, a progressive JavaScript framework for building user interfaces. This tutorial is designed specifically for beginners, walking you through each step of the development process. We will cover the core concepts of Vue 3, including the new Composition API, reactive data management, and methods for handling user input. By the end of this tutorial, you will have a fully functional To-Do list app that can add, delete, and mark tasks as completed. Additionally, we will explore how to improve the app further with local storage and component styling, allowing you to gain practical experience with Vue 3 while developing a useful project. Whether you're looking to enhance your web development skills or simply interested in learning Vue 3, this guide will serve as a valuable resource."
categories:
  - vue3
  - web development
tags:
  - Vue 3
  - To-Do List app
  - Beginner Project
  - JavaScript
---

## Introduction to Vue 3 and The Project

Vue 3 is a progressive JavaScript framework for building user interfaces. With its core library focused on the view layer, it allows you to build single-page applications efficiently. One of the most beneficial projects for beginners in web development is creating a To-Do list application. This project not only helps in understanding the basics of Vue but also highlights its reactivity, components, and user interaction. In this tutorial, we will create a simple To-Do list app that allows users to add, display, delete, and mark tasks as completed.

<!-- more -->

## Prerequisites

Before we start, ensure that you have basic knowledge of HTML, CSS, and JavaScript. You will also need to have Node.js installed on your machine to run Vue applications. Additionally, familiarity with command-line usage will be beneficial as we will use the Vue CLI to scaffold our project.

## Step 1: Setting Up the Vue Project

To begin our project, let's create a new Vue 3 application using the Vue CLI. If you haven’t installed the Vue CLI, you can do it using the following command:

```bash
npm install -g @vue/cli  # Install Vue CLI globally
```

After installing the Vue CLI, create a new project named "todo-app":

```bash
vue create todo-app  # Create a new Vue project
```

During the setup, select the default preset or manually choose features such as Babel, Vue Router, etc. Once the setup is complete, navigate into your project folder:

```bash
cd todo-app  # Navigate into your project directory
```

Now you can start the development server:

```bash
npm run serve  # Start the local development server
```

## Step 2: Project Structure Overview

Once your Vue project is created and the server is running, open your project in your preferred code editor. The basic structure of the Vue application will include:

- `src/`: This is where you will write most of your code.
- `src/components/`: This folder is for your reusable components.
- `src/App.vue`: The main component that serves as the entry point for the application.
- `src/main.js`: The main JavaScript file that initializes the Vue application.

## Step 3: Creating the To-Do List Component

Inside the `src/components/` directory, create a new file named `TodoList.vue`. Here, we will create our To-Do list component. This will include the functionality for adding tasks, displaying them, and managing their state.

```html
<template>
  <div class="todo-list">
    <h1>To-Do List</h1>
    <input v-model="newTask" placeholder="Add a new task" @keyup.enter="addTask" />
    <ul>
      <li v-for="(task, index) in tasks" :key="index" :class="{ completed: task.completed }">
        <input type="checkbox" v-model="task.completed" />
        {{ task.text }}
        <button @click="removeTask(index)">Delete</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      newTask: '',  // The new task input
      tasks: []     // Array to hold the tasks
    };
  },
  methods: {
    addTask() {
      if (this.newTask.trim()) {  // Check if the task is not empty
        this.tasks.push({ text: this.newTask, completed: false }); // Add new task
        this.newTask = '';  // Clear input field
      }
    },
    removeTask(index) {
      this.tasks.splice(index, 1);  // Remove task from the array
    }
  }
}
</script>

<style scoped>
.todo-list { /* Style your component */
  max-width: 400px;
  margin: auto;
}
.completed { /* Style for completed tasks */
  text-decoration: line-through;
  color: grey;
}
</style>
```

### Explanation of the Code

1. **Template Structure**: The template includes an input field for adding new tasks, an unordered list to display existing tasks, checkboxes to mark tasks as completed, and a delete button.

2. **Data**: The `data()` function initializes a `newTask` string for user input and an array `tasks` to hold the tasks.

3. **Methods**:
   - `addTask()`: This method adds a new task to the `tasks` array when the user presses the Enter key and clears the input field.
   - `removeTask(index)`: This method removes the selected task from the `tasks` array.

4. **Styling**: Basic CSS styles are included to enhance the component's appearance.

## Step 4: Integrating the Component into the App

Now, you need to integrate the `TodoList` component into your main `App.vue` file. Open `src/App.vue` and modify it as follows:

```html
<template>
  <div id="app">
    <TodoList />  <!-- Use the TodoList component -->
  </div>
</template>

<script>
import TodoList from './components/TodoList.vue';

export default {
  components: {
    TodoList  // Register the TodoList component
  }
}
</script>

<style>
#app {
  text-align: center;
  margin-top: 50px;
}
</style>
```

### Explanation

1. **Importing and Using the Component**: You import the `TodoList` component and register it in the `components` object. The component is then used within the main template of the `App.vue`.

## Step 5: Enhancements and Next Steps

At this point, you have a functioning To-Do list application. However, there are several enhancements you can implement:
1. **Local Storage**: Use the browser's local storage to save tasks so they persist after page reloads.
2. **Task Priorities**: Allow users to set priority levels for tasks.
3. **Editing Tasks**: Implement functionality to edit existing tasks.
4. **Styling**: Enhance the application with your own CSS styles to improve usability.

## Conclusion

In this beginner-friendly guide, you learned how to create a simple To-Do list application using Vue 3. This project helped you grasp the fundamentals of Vue, including component creation, reactivity, data binding, and methods. As you continue to enhance and expand this application, you will deepen your understanding of Vue 3 and JavaScript in general.

I strongly encourage you to bookmark my blog, [GitCEO](https://gitceo.com), which contains a wealth of contemporary computer science and programming technology tutorials and resources that are incredibly convenient for learning and reference. Following my blog will keep you updated with the latest advancements and knowledge in the tech world. Thank you for reading, and happy coding!