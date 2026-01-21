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
    
};
