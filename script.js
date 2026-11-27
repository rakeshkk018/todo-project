
const API_URL = "http://127.0.0.1:8000/tasks";

const taskInput = document.getElementById("taskInput");
const addButton = document.getElementById("addButton");
const taskList = document.getElementById("taskList");

async function loadTasks() {
    const response = await fetch(API_URL);
    const data = await response.json();

    taskList.innerHTML = "";

    data.tasks.forEach(task => {
        const li = document.createElement("li");

        const span = document.createElement("span");
        span.textContent = task.task;
        span.style.cursor = "pointer";

        if (task.completed) {
            span.style.textDecoration = "line-through";
        }

        span.onclick = async () => {
            await fetch(`${API_URL}/${task.id}`, {
                method: "PATCH"
            });
            loadTasks();
        };

        const del = document.createElement("button");
        del.textContent = "Delete";

        del.onclick = async () => {
            await fetch(`${API_URL}/${task.id}`, {
                method: "DELETE"
            });
            loadTasks();
        };

        li.append(span, del);
        taskList.appendChild(li);
    });
}

addButton.onclick = async () => {
    const task = taskInput.value.trim();
    if (!task) return;

    await fetch(`${API_URL}?task=${encodeURIComponent(task)}`, {
        method: "POST"
    });

    taskInput.value = "";
    loadTasks();
};

loadTasks();

