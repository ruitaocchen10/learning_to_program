"use strict";
async function createUser(user) {
    const response = await fetch("http://localhost:8000/users", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(user),
    });
    const data = await response.json();
    return data;
}
async function getUsers() {
    const response = await fetch("http://localhost:8000/users");
    const data = await response.json();
    return data;
}
