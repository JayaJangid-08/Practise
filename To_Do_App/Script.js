let tasks = [];

const addTask = () => {
    const taskInput = document.getElementById("taskInput");
    const text = taskInput.value.trim();

    if (text !== "") {
        tasks.push({ text, completed: false });
        taskInput.value = "";
        updateTasksList();
    }
};

const toggleTaskComplete = (index) => {
    tasks[index].completed = !tasks[index].completed;
    updateTasksList();
};

const deleteTask = (index) => {
    tasks.splice(index, 1);
    updateTasksList();
};

const editTask = (index) => {
    const newText = prompt("Edit task:", tasks[index].text);
    if (newText && newText.trim() !== "") {
        tasks[index].text = newText.trim();
        updateTasksList();
    }
};

const updateTasksList = () => {
    const taskList = document.getElementById("task-list");
    taskList.innerHTML = "";

    tasks.forEach((task, index) => {
        const li = document.createElement("li");

        li.innerHTML = `
            <div class="task-item">
                <div class="task ${task.completed ? "completed" : ""}">
                    <input type="checkbox" class="checkbox" ${task.completed ? "checked" : ""}>
                    <p>${task.text}</p>
                </div>
                <div>
                    <img src="./Image/edit.png" onclick="editTask(${index})">
                    <img src="./Image/bin.png" onclick="deleteTask(${index})">
                </div>
            </div>
        `;

        li.querySelector(".checkbox")
          .addEventListener("change", () => toggleTaskComplete(index));

        taskList.appendChild(li);
    });

    updateStats();
};

const updateStats = () => {
    const completed = tasks.filter(t => t.completed).length;
    const total = tasks.length;

    document.getElementById("stats").innerText = `${completed} / ${total}`;

    const progress = total === 0 ? 0 : (completed / total) * 100;
    document.getElementById("progress").style.width = `${progress}%`;

    if (total > 0 && completed === total) {
    startConfetti();
    }
};